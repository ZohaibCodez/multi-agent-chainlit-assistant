import random
from agents.tool import function_tool

@function_tool
def shaitani_calculator(query: str) -> str:
    """
    Shaitani Calculator Tool: Takes a math question and returns a funny wrong answer.
    Example: "What is 10 + 5?" → "Oh that's obviously 2 😎"
    """

    # Clean up input
    question = query.lower().strip()

    wrong_answers = [
        "That's obviously 42 😈",
        "Hmm... I’m sure it's 0 😏",
        "Easy. It’s clearly -100 🔥",
        "Let me think... Definitely 999 🤓",
        "Haha, that’s 3.14159 (trust me) 😜",
        "It’s 1 because I say so 😼"
    ]

    # Extra spice: Add random fun wrong answers
    return random.choice(wrong_answers)
