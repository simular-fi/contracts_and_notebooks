"""
From the Mesa example: 
https://github.com/projectmesa/mesa-examples/blob/main/examples/boltzmann_wealth_model_network

Modified to use a smart contract for the money exchange

"""

import mesa
import simular
from stablecoin import abi

XFER_AMOUNT = 10**18
INITIAL_BALANCE = 10**18


def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B


class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, wallet, model):
        super().__init__(unique_id, model)
        self.wallet = wallet

    @property
    def wealth(self):
        bal = self.model.contract.balanceOf.call(self.wallet)
        return bal / 10**18  # readability

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self, amount):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        cellmates.pop(cellmates.index(self))  # exclude myself...
        if len(cellmates) > 0:
            other = self.random.choice(cellmates)
            self.model.contract.transfer.transact(
                other.wallet, amount, caller=self.wallet
            )

    def step(self):
        self.move()
        amt = self.model.contract.balanceOf.call(self.wallet)
        if amt > 0:
            if amt < XFER_AMOUNT:
                self.give_money(amt)
            else:
                self.give_money(XFER_AMOUNT)


class BoltzmannWealthModelNetwork(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, num_agents=100, width=10, height=10):
        super().__init__()
        self.num_agents = num_agents
        self.grid = mesa.space.MultiGrid(width, height, True)

        self.schedule = mesa.time.RandomActivation(self)
        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Wealth": lambda _: _.wealth},
        )

        # Setup smart contract specifics
        self.evm = simular.PyEvm()
        self.contract = abi.deploy_and_loan_contract(self.evm)
        wallets = simular.create_many_accounts(self.evm, self.num_agents)

        # Create agents
        for i, w in enumerate(wallets):
            # fund wallet
            self.contract.mint.transact(w, INITIAL_BALANCE, caller=abi.MINTER)
            # create agent
            a = MoneyAgent(i, w, self)
            # add the agent to the scheduler and random node
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

    @property
    def dataframe(self):
        return self.datacollector.get_model_vars_dataframe()

    def run_model(self, n):
        for _ in range(n):
            self.step()
