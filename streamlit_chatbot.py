import streamlit as st

import openai

openai.api_key ="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"


st.title("MyChatbot")

conversation_history = []

user_input = st.text_input("Enter your Query:")

if user_input:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_input,
        temperature=0.9,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    response1 = response.choices[0]["text"]
    conversation_history.append(f"You: {user_input}")
    conversation_history.append(f"Chatbot: {response1}")

st.header("Conversation history")
for message in conversation_history:
    st.write(message)
