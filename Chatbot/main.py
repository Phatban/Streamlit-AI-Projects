"""
main.py

This is the main module for the Chatbot application using Streamlit.
It provides the user interface and integrates the chatbot functionality.

Functions:
    main(): Run the Streamlit application.

This module depends on the chatbot module for HugChat interaction functionality.
"""

import streamlit as st
from chatbot import initialize_chatbot, generate_response


def main():
    """
    Main function to run the Streamlit app for the chatbot.
    """
    st.title('Simple Chatbot')

    # Sidebar for Hugging Face credentials
    with st.sidebar:
        st.title('Login HugChat')
        hf_email = st.text_input('Enter E-mail:')
        hf_pass = st.text_input('Enter Password:', type='password')

    if not (hf_email and hf_pass):
        st.warning('Please enter your Hugging Face account credentials!')
    else:
        st.success('Proceed to chat with the bot!')

        # Initialize session state for chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("What is your question?"):
            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate chatbot response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    chatbot = initialize_chatbot(hf_email, hf_pass)
                    response = generate_response(chatbot, prompt)
                    st.markdown(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
