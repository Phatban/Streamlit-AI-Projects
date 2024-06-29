"""
chatbot.py

This module provides functions to interact with the HugChat chatbot.

Functions:
    initialize_chatbot(email, password): Initialize the HugChat chatbot.
    generate_response(chatbot, prompt): Generate a response from the chatbot.

This module is part of the Chatbot project using Streamlit.
"""

from hugchat import hugchat
from hugchat.login import Login


def initialize_chatbot(email, password):
    """
    Initialize the HugChat chatbot.

    Args:
    email (str): Hugging Face account email.
    password (str): Hugging Face account password.

    Returns:
    hugchat.ChatBot: Initialized chatbot instance.
    """
    sign = Login(email, password)
    cookies = sign.login()
    return hugchat.ChatBot(cookies=cookies.get_dict())


def generate_response(chatbot, prompt):
    """
    Generate a response from the chatbot.

    Args:
    chatbot (hugchat.ChatBot): Initialized chatbot instance.
    prompt (str): User's input prompt.

    Returns:
    str: Chatbot's response.
    """
    return chatbot.chat(prompt)
