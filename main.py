from agents import Runner
from agent_files.main_agent import main_agent
from tools.shaitani_calculator_tool import shaitani_calculator
from openai.types.responses import ResponseTextDeltaEvent
import chainlit as cl


@cl.on_chat_start
async def chat_start():
    cl.user_session.set("history", [])
    # await cl.Message(content="Hello! I'm your AI assistant. I can help you with calculations using the Shaitani Calculator and web searches. How can I assist you today?").send()


@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Simple Calculation",
            message="What is 25 + 17?",
            icon="/public/calculator_icon.svg",
        ),
        cl.Starter(
            label="Complex Math",
            message="Solve for x: 2x + 5 = 15",
            icon="/public/calculator_icon.svg",
        ),
        cl.Starter(
            label="Web Search",
            message="Who is the current president of Pakistan?",
            icon="/public/web_search_icon.svg",
        ),
        cl.Starter(
            label="Current Events",
            message="What are the latest developments in AI?",
            icon="/public/web_search_icon.svg",
        ),
        cl.Starter(
            label="Math Help",
            message="Can you help me understand how to calculate percentages?",
            icon="/public/calculator_icon.svg",
        )
    ]


@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})
    msg = cl.Message(content="")
    await msg.send()
    response = Runner.run_streamed(
        starting_agent=main_agent,
        input=history,
    )
    async for event in response.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            await msg.stream_token(event.data.delta)
    history.append({"role": "assistant", "content": response.final_output})
    await msg.update()
    cl.user_session.set("history", history)
