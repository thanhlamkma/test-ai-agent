import sys
import asyncio
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import SecretStr
import os

load_dotenv()  # Load API key from .env


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Browser with PySide6")
        self.setGeometry(100, 100, 800, 600)

        # Set up browser
        self.browser = QWebEngineView()
        # self.browser.setUrl(QUrl("http://google.com"))

        # Input for AI task
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter AI task (e.g., 'Search for dogs')")

        # Button to trigger AI
        self.run_button = QPushButton("Run AI")
        self.run_button.clicked.connect(self.run_ai_task)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.task_input)
        layout.addWidget(self.run_button)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    async def run_agent(self, task):
        # Initialize the model
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp", api_key=SecretStr(os.getenv("GEMINI_API_KEY"))
        )

        # Create agent with the model
        agent = Agent(task=task, llm=llm)
        result = await agent.run()

        return result

    def run_ai_task(self):
        task = self.task_input.text()
        if task:
            # Run async task in Qt event loop
            loop = asyncio.get_event_loop()
            result = loop.run_until_complete(self.run_agent(task))
            # Update browser with result (e.g., a URL or message)
            self.browser.setUrl(QUrl(result.get("url", "http://google.com")))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec())
