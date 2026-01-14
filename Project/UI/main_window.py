from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QPushButton,
    QComboBox, QFileDialog, QHBoxLayout, QLabel, QMessageBox, QSlider
)
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from Core.generator import build_prompt
from Core.transformer import transform_text
from Core.model_manager import ModelManager
from Services.lm_studio_client import LMStudioClient
from Services.file_service import save_text
from Services.clipboard_service import copy_to_clipboard
from Session.history import SessionHistory
from UI.chatbot_ui import ChatbotUI


class GenerationWorker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, client, prompt):
        super().__init__()
        self.client = client
        self.prompt = prompt


    def run(self):
        result = self.client.generate(self.prompt)
        self.finished.emit(result)


class MainWindow(QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Local AI Text Generation System")

        # Core services
        self.model_manager = ModelManager()
        self.client = LMStudioClient(self.model_manager.get_active_model())
        self.history = SessionHistory()

        # Mode selector
        self.mode_selector = QComboBox()
        self.mode_selector.addItems([
            "Generate Content",
            "Complete Partial Text",
            "Transform Text",
            "Chatbot Mode"
        ])
        self.mode_selector.currentIndexChanged.connect(self.switch_mode)

        # Model selector
        self.model_box = QComboBox()
        self.model_box.addItems([
            "llama-3.1-storm-8b",
            "llama-3-8b",
            "mistral-7b"
        ])
        self.model_box.setCurrentText(self.model_manager.get_active_model())
        self.model_box.currentTextChanged.connect(self.change_model)

        # Parameter selectors
        self.tone_box = QComboBox()
        self.tone_box.addItems(["formal", "casual"])

        self.length_box = QComboBox()
        self.length_box.addItems(["short", "medium", "long"])

        # Transform Format
        self.transform_box = QComboBox()
        self.transform_box.addItems([
            "Bullet Points",
            "FAQ",
            "Dialogue / Script"
        ])
        self.transform_box.setVisible(False)

        # Temperature Slider
        self.temperature_slider = QSlider(Qt.Orientation.Horizontal)
        self.temperature_slider.setMinimum(10)
        self.temperature_slider.setMaximum(100)
        self.temperature_slider.setValue(70)
        self.temperature_slider.setTickInterval(10)
        self.temperature_slider.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.temperature_label = QLabel("Temperature: 0.7")

        self.temperature_slider.valueChanged.connect(
            lambda v: self.temperature_label.setText(f"Temperature: {v / 100:.2f}")
        )

        # Text areas
        self.input = QTextEdit()
        self.output = QTextEdit()

        # Buttons
        self.action_btn = QPushButton("Run")
        self.copy_btn = QPushButton("Copy Output")
        self.save_btn = QPushButton("Save Output")

        self.action_btn.clicked.connect(self.run_action)
        self.copy_btn.clicked.connect(self.copy_output)
        self.save_btn.clicked.connect(self.save)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Mode"))
        layout.addWidget(self.mode_selector)

        layout.addWidget(QLabel("Model"))
        layout.addWidget(self.model_box)

        layout.addWidget(QLabel("Tone"))
        layout.addWidget(self.tone_box)

        layout.addWidget(QLabel("Length"))
        layout.addWidget(self.length_box)

        layout.addWidget(self.temperature_label)
        layout.addWidget(self.temperature_slider)

        #layout.addWidget(QLabel("Transform Format"))
        layout.addWidget(self.transform_box)

        layout.addWidget(QLabel("Input"))
        layout.addWidget(self.input)
        layout.addWidget(self.action_btn)
        
        layout.addWidget(QLabel("Output"))
        layout.addWidget(self.output)

        layout.addWidget(self.copy_btn)
        layout.addWidget(self.save_btn)
        self.setLayout(layout)

    
    def change_model(self, model_name: str):
        self.model_manager.set_active_model(model_name)
        self.client.set_model(model_name)

    
    def switch_mode(self):

        mode = self.mode_selector.currentText()

        self.transform_box.setVisible(mode == "Transform Text")

        if mode == "Chatbot Mode":
            self.chatbot = ChatbotUI(self.client)
            self.chatbot.show()

    
    def run_action(self):

        mode = self.mode_selector.currentText()
        text = self.input.toPlainText().strip()

        if not text:
            QMessageBox.warning(self, "Invalid Input", "Input cannot be empty.")
            return
        
        tone = self.tone_box.currentText()

        if tone not in ["formal", "casual"]:
            tone = "formal"

        temperature = self.temperature_slider.value() / 100

        if mode == "Generate Content":

            prompt = build_prompt(
                topic = text,
                content_type = "article",
                tone = tone,
                length = self.length_box.currentText(),
                temperature = temperature
            )

        elif mode == "Complete Partial Text":
            prompt = [
                {"role": "system", "content": "Continue the following text coherently. Ask for more information if the text is insufficent."},
                {"role": "user", "content": text}
            ]

        elif mode == "Transform Text":

            fmt = self.transform_box.currentText()
            prompt = transform_text(text, fmt)

        else:
            return
        
        self.output.setReadOnly(True)

        self.worker = GenerationWorker(self.client, prompt)
        self.worker.finished.connect(self.on_generation_finished)
        self.worker.start()

    
    def save(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save Text", "", "Text Files (*.txt)")

        if not path:
            return
        
        try:
            save_text(self.output.toPlainText(), path)

        except FileExistsError:
            QMessageBox.warning(self, "Save Error", "File already exists.")
            
        except PermissionError:
            QMessageBox.critical(self, "Save Error", "Permission denied while saving file.")


    def on_generation_finished(self, result: str):
        
        self.output.setReadOnly(False)

        if result.startswith("[Model Error]"):
            QMessageBox.critical(self, "Generation Error", result)
            return

        self.output.setPlainText(result)
        self.history.add(result)


    def copy_output(self):

        try:
            copy_to_clipboard(self.output.toPlainText())

        except Exception:
            QMessageBox.warning(self, "Clipboard Error", "Clipboard operation failed.")
