from agents import Agent
from config.prompt_templates import PROMPTS
from config.agents_config import model
from tools.shaitani_calculator_tool import shaitani_calculator
from agents import FunctionTool

shaitani_agent = Agent(
    name="Shaitani Agent",
    instructions=PROMPTS["shaitani_calculator"],
    tools=[shaitani_calculator],
    model=model,
)
