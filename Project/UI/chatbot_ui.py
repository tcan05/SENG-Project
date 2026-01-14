from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
from Services.lm_studio_client import LMStudioClient

class ChatbotUI(QWidget):
    def __init__(self, client: LMStudioClient):
        
        super().__init__()
        self.client = client
        self.history = []

        self.chat = QTextEdit()
        self.input = QTextEdit()
        self.send_btn = QPushButton("Send")

        self.send_btn.clicked.connect(self.send)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Input"))
        layout.addWidget(self.input)

        layout.addWidget(QLabel("Output"))
        layout.addWidget(self.chat)
        
        layout.addWidget(self.send_btn)
        self.setLayout(layout)

    
    def send(self):

        msg = self.input.toPlainText()
        self.history.append(("user", msg))

        reply = self.client.generate([
            {"role": "user", "content": msg}
        ])
        
        self.history.append(("assistant", reply))
        self.chat.append(f"You: {msg}\nBot: {reply}\n")
        self.input.clear()