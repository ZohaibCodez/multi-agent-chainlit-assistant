from agents import Runner
from agent_files.main_agent import main_agent
from openai.types.responses import ResponseTextDeltaEvent
import chainlit as cl


@cl.on_chat_start
async def chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello there, how can i assist you today?").send()


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
    # print(history, "\n")
    await msg.update()
    cl.user_session.set("history", history)
