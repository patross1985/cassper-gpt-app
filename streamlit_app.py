import streamlit as st
from streamlit_option_menu import option_menu
import openai
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Cassper GPT", layout="wide")

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Cassper GPT",
        [
            "Chat GPT",
            "Evidence Vault",
            "Timeline",
            "Violation Scanner",
            "Document Builder",
            "FOIP Tools",
            "Alberta Forms",
            "Settings",
        ],
        icons=["chat", "archive", "calendar", "exclamation-circle", "file-text", "folder", "file-earmark", "gear"],
        menu_icon="cast",
        default_index=0,
    )

# Main area content
if selected == "Chat GPT":
    st.title("Chat GPT")
    st.write("Ask legal questions or draft documents using OpenAI's GPT API.")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    user_query = st.text_area("Enter your query:")
    if st.button("Send"):
        if not openai_api_key:
            st.error("API key not set. Please configure OPENAI_API_KEY in your .env file.")
        elif not user_query.strip():
            st.warning("Please enter a query.")
        else:
            with st.spinner("Generating response..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": user_query}],
                    )
                    answer = response["choices"][0]["message"]["content"]
                    st.success(answer)
                except Exception as e:
                    st.error(f"Error: {e}")

elif selected == "Evidence Vault":
    st.title("Evidence Vault")
    st.write("Upload and manage evidence files securely.")
    uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)
    if uploaded_files:
        for f in uploaded_files:
            st.success(f"Uploaded {f.name}.")

elif selected == "Timeline":
    st.title("Timeline")
    st.write("Visualize case timelines and events.")
    # Placeholder for timeline visualization

elif selected == "Violation Scanner":
    st.title("Violation Scanner")
    st.write("Scan documents for potential legal violations.")
    # Placeholder for violation scanning functionality

elif selected == "Document Builder":
    st.title("Document Builder")
    st.write("Generate legal documents and templates.")
    # Placeholder for document builder functionality

elif selected == "FOIP Tools":
    st.title("FOIP Tools")
    st.write("Tools for Freedom of Information and Protection requests.")
    # Placeholder for FOIP tools functionality

elif selected == "Alberta Forms":
    st.title("Alberta Forms")
    st.write("Access Alberta-specific legal forms.")
    # Placeholder for Alberta forms functionality

elif selected == "Settings":
    st.title("Settings")
    st.write("Configure application settings.")
    # Placeholder for settings configuration
