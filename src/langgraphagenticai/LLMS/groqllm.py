import os
import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input
        
    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY")
            selected_groq_model = self.user_controls_input.get("selected_groq_model")
            if groq_api_key=="" or os.environ.get("GROQ_API_KEY")=="":
                st.error("GROQ API key is missing. Please provide a valid API key.")
                
            llm = ChatGroq(model=selected_groq_model, api_key=groq_api_key)
        except Exception as e:
            raise ValueError(f"Error initializing GroqLLM: {e}")
        return llm
