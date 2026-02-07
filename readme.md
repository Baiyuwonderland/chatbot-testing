# AI Chatbot

A Streamlit chatbot powered by LangChain with support for multiple AI providers.
Switch between Groq (Llama 3.1) and Google Gemini models via a sidebar dropdown.
Maintains conversation history with custom avatars for a personalized chat experience.

## Setup

### Using uv (Recommended)

[uv](https://docs.astral.sh/uv/) is a fast Python package manager.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Initialize a new project (creates pyproject.toml):**

```bash
uv init
```

**Add dependencies:**

```bash
uv add streamlit python-dotenv langchain-core langchain-groq langchain-google-genai
```

**Create and activate virtual environment:**

```bash
# Create virtual environment
uv venv

# Activate it
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
```

**Install dependencies:**

```bash
# From pyproject.toml (recommended)
uv sync

# Or from requirements.txt
uv pip install -r requirements.txt
```

**Run the app:**

```bash
streamlit run chatbot_groq_gemni_langchain_streamlit.py

# Or without activating the venv
uv run streamlit run chatbot_groq_gemni_langchain_streamlit.py
```


## Configuration

Create a `.env` file with your API keys:

```
GROQ_API_KEY=your_groq_key
GEMINI_API_KEY=your_gemini_key
```

## Cloud App

[https://chatbot-testing-assessment.streamlit.app/](https://chatbot-testing-assessment.streamlit.app/)
