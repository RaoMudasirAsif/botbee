import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = "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 "

# Define the chatbot function
def chatbot(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=None
    )
    return response.choices[0].text.strip()

# Set the title and description of the app
st.title("Chatbot")
st.markdown("Welcome to the chatbot! Please enter your query below.")

# User input text box
user_input = st.text_input("User Input")

# Send button
if st.button("Send"):
    # Get the chatbot's response
    bot_response = chatbot(user_input)
    st.text_area("Bot Response", bot_response)
