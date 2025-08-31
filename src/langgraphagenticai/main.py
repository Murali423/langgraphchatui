import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agentic_app():
    """Load the LangGraph Agentic AI Streamlit application."""
    ui_loader = LoadStreamlitUI()
    user_input = ui_loader.load_streamlit_ui()
    if not user_input:
        st.error("Failed to load user input. Please try again.")
        return
    user_message = st.chat_input("Enter your message here...")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
            if not model:
                st.error("LLM model not Present. Please check your configuration.")
                return
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("No use case selected. Please choose a use case.")
                return
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                print(user_message)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Graph setup failed: {e}")
                return
        except Exception as e:
            st.error(f"Error: Graph set up failed- {e}")
            return