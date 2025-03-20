# NOTE: Python version >= 3.11
python -m venv venv
venv/Script/activate

pip install browser-use
playwright install
pip install langchain_google_genai

py main.py

# Format: Black Formatter