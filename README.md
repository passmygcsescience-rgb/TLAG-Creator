# 🎓 GEMS TLAG Lesson Creator

A Streamlit web application for creating professional lesson PowerPoints following the **Teach Like a GEM (TLAG)** methodology.

## Features

- 📚 **Curriculum Browser** - AQA GCSE Science & IB DP Chemistry support
- 🤖 **AI-Powered Generation** - Automatic lesson content using GPT-4
- 📊 **TLAG Structure** - Do Now → Learning Outcome → To Know → I Do/We Do/You Do → Exit Ticket
- 📥 **PowerPoint Export** - Download ready-to-use presentations

## Deployment

This app is deployed on [Streamlit Community Cloud](https://streamlit.io/cloud).

## Setup for Local Development

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create `.streamlit/secrets.toml`:
   ```toml
   OPENAI_API_KEY = "your-api-key-here"
   ```
5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Configuration

For cloud deployment, set the `OPENAI_API_KEY` secret in Streamlit Cloud settings.

---
*Built with ❤️ for GEMS Education*
