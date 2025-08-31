from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self,model):
        self.model=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """Builds a basic chatbot using the LangGraph framework.
           This method initializes a state graph with a start and end node, and adds a message node in between. 

        """
        self.chatbot_node = BasicChatbotNode(self.model)
        self.graph_builder.add_node("chat_bot",self.chatbot_node.process)
        self.graph_builder.add_edge(START,"chat_bot")
        self.graph_builder.add_edge("chat_bot",END)

    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        return self.graph_builder.compile()
