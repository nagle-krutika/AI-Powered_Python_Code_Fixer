from openai import OpenAI
import streamlit as st

file = open("Keys/new_key.txt")
key = file.read()

client = OpenAI(api_key = key)

st.title("AI-Powered Python Code Fixer")

user_input = st.text_area("Enter python code", height=200)

if st.button("Generate") == True:
    st.snow()
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a python code fixer.
                                                Given a python code should analyze the submitted code and identify potential bugs, errors or areas of improvement.
                                                First give the suggestion for fixes in numbered format with title "Suggestion Fixes" and then corrected code with tile "Corrected Code"."""},
                {"role": "user", "content": user_input}
            ]
        )
        
    st.write(response.choices[0].message.content)
