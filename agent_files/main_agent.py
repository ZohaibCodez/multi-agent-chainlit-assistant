import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents import Agent, Runner
from agent_files.shaitani_agent import shaitani_agent
from agent_files.web_search_agent import web_search_agent
from config.prompt_templates import PROMPTS
from config.agents_config import model

main_agent = Agent(
    name="Main Assistant",
    instructions=PROMPTS["main_agent"],
    handoffs=[shaitani_agent, web_search_agent],
    model=model,
)
