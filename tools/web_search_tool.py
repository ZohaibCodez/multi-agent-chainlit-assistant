from tavily import TavilyClient
from agents.tool import function_tool

api_key = "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"
tavily_client = TavilyClient(api_key)

@function_tool
def web_search(query: str) -> str:
    """
    Uses Tavily to perform a web search and return a short summary of the top result.
    
    Input: A user question or search keyword (e.g., "Who is the Prime Minister of Pakistan?")
    Output: A brief factual answer or snippet from the top relevant search result.
    """
    response = tavily_client.search(query)
    return response["results"][0]
