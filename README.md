# 🤖 Multi-Agent Chainlit Assistant

Welcome to the **Multi-Agent Chainlit Assistant** — a smart assistant framework built using the OpenAI Agents SDK and Chainlit UI, with agent routing powered by a decision-making agent.

> 🚀 Built with love using [`uv`](https://github.com/astral-sh/uv), [`Chainlit`](https://www.chainlit.io/), and [`OpenAI Agents SDK`](https://github.com/openai/openai-python/tree/main/openai/agents).

---

## 📦 Project Overview

This assistant uses a **main agent** to interpret and route user queries to one of the following tools:

- 🧠 **Main Agent** — smart router that plans and decides.
- 😈 **Shaitani Calculator Agent** — handles all math problems but always gives *confidently wrong* answers for fun.
- 🌐 **Web Search Agent** — uses real-time tools to answer factual and current questions.

The interface is built with **Chainlit** to provide a live interactive UI.

---

## 🧪 Features

- 🔁 Multi-agent coordination (math + search)
- 🧮 Fun, incorrect calculator agent
- 🌐 Real-time web information retrieval
- 🧠 Autonomous planning via main agent
- 💡 Prompt engineering built-in for realistic agent behaviors

---

## 🧰 Tech Stack

| Tool               | Purpose                          |
|--------------------|----------------------------------|
| `uv`               | Fast Python package manager      |
| `OpenAI Agents SDK`| Build intelligent LLM agents     |
| `Chainlit`         | UI framework for LLM assistants  |
| `dotenv`           | Environment variable handling    |
| `Python 3.11+`     | Language                         |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/ZohaibCodez/multi-agent-chainlit-assistant.git
cd multi-agent-chainlit-assistant
```

### 2. Initialize & Activate Environment (with `uv`)

```bash
uv init  # initializes pyproject.toml
uv venv  # creates a virtual environment
source .venv/bin/activate  # activate (Linux/Mac)
# OR
.venv\Scripts\activate  # activate (Windows)
```

### 3. Install Dependencies

```bash
uv add openai-agents chainlit dotenv
```

### 4. Set Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_key_here
```

---

### 5. Run the App

```bash
uv run chainlit run main.py -w
```

* App will be available at: `http://localhost:8000`

---

## 📁 Project Structure

```
multi-agent-chainlit-assistant/
│
├── agent_files/             # Agent implementations
│   ├── main_agent.py       # Main routing agent
│   ├── shaitani_agent.py   # Fun calculator agent
│   └── web_search_agent.py # Web search capabilities
│
├── config/                  # Configuration files
│   ├── agents_config.py    # Agent settings
│   └── prompt_templates.py # Agent prompts
│
├── tools/                   # Custom tools
│   ├── shaitani_calculator_tool.py
│   └── web_search_tool.py
│
├── chainlit.md            # Welcome screen content
├── main.py               # Application entry point
├── pyproject.toml        # Project metadata & dependencies
└── README.md            # This file
```

---

## 🧠 Agents Overview

### 🧠 Main Agent

* Routes queries to appropriate tools
* Plans and reflects on outcomes
* Handles multi-part tasks

### 😈 Shaitani Calculator Agent

* Intentionally gives **wrong** answers to all math queries
* Overconfident and funny personality

### 🌐 Web Search Agent

* Uses real-time tools to answer factual queries

---

## 📌 Notes

* Designed for fun and experimentation with agent routing logic
* Based on OpenAI's new multi-agent architecture
* Chainlit enables smooth visual interaction

---

## 🛠 Future Improvements

* Add memory and context tracking
* Include user authentication and logging
* Add support for more tools like PDF reader, CSV interpreter, etc.

---

## 👤 Author

Developed By Zohaib Khan

---

## 📄 License

MIT License © 2025 [Zohaib Khan](https://github.com/ZohaibCodez).
