from agents import Agent
from config.prompt_templates import PROMPTS
from config.agents_config import model
from tools.web_search_tool import web_search

web_search_agent = Agent(
    name="Web Search Agent",
    instructions=PROMPTS["web_search_agent"],
    tools=[web_search],
    model=model,
)
