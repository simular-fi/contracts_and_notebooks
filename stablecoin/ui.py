import seaborn as sns
from mesa.experimental import JupyterViz
from stablecoin.model import BoltzmannWealthModelNetwork

sns.set_theme()


model_params = {
    "num_agents": {
        "type": "SliderInt",
        "value": 100,
        "label": "Number of agents:",
        "min": 100,
        "max": 200,
        "step": 10,
    }
}


def agent_portrayal(agent):
    return {"color": "tab:green"} if agent.wealth > 0 else {"color": "tab:grey"}


def get_ui():
    return JupyterViz(
        BoltzmannWealthModelNetwork,
        model_params,
        measures=["Gini"],
        name="Boltzmann Money Model w/Smart Contracts",
        agent_portrayal=agent_portrayal,
    )
