from langgraph.prebuilt import ToolNode
from langchain_community.tools.tavily_search import TavilySearchResults

def get_tools():
    """Function to get the list of tools."""
    tools=[TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """Function to create a ToolNode with the list of tools."""
    return ToolNode(tools=tools)