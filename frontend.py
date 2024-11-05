import streamlit as st
import requests

st.title("RecipeAI")

# Input field for the data you want to send to Colab
input_data = st.text_input("List some ingredients...")

if st.button("Find Recipes"):
    if input_data:
        # Replace with the ngrok URL provided by Colab
        colab_url = "https://2314-34-23-120-230.ngrok-free.app"
        endpoint_url = f"{colab_url}/run"

        with st.spinner("Waiting for AI response..."):
            # Send the data to Colab API
            response = requests.post(endpoint_url, json={"input": input_data})
        
            if response.status_code == 200:
                result = response.json().get("result")
                st.write("Results: ")
                st.write(result)
            else:
                st.error("Failed to get a response from Colab")
    else:
        st.warning("Please enter some input.")