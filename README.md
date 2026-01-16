# SENG-Project

## Overview
This project is a desktop-based AI text generation and transformation application built with Python and PyQt6.
It provides a GUI that allows users to interact with a locally hosted LLM via LM Studio.

## Key Features

- Desktop GUI built with PyQt6
- Local LLM integration using LM Studio
- Text transformation tools
- Clipboard support
- Save output to file
- Session history tracking
- Configurable settings via JSON/Python config files

## Requirements

- Python 3.10+
- [LM Studio](https://lmstudio.ai/)
- A local LLM model loaded into LM Studio
- PyQt6
- openai

Install Python dependencies:
```bash
pip install PyQt6 openai
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tcan05/SENG-Project.git
```
2. Navigate to the project directory:
```bash
cd SENG-Project/Project
```
3. Run the application:
```bash
python main.py
```
> Make sure LM Studio is running and a model is loaded before starting the application.

## How To Use

1. Start LM Studio and load a local LLM model
2. Launch the application
3. Select a transformation type
4. Enter text into the input box
5. Click "Run"
6. Copy or save the output

## Architecture

SENG-Project/
│
├── Project/
│   ├── main.py
│   │
│   ├── UI/
│   │   ├── main_window.py
│   │   └── chatbot_ui.py
│   │
│   ├── Core/
│   │   ├── generator.py
│   │   ├── transformer.py
│   │   └── model_manager.py
│   │
│   ├── Services/
│   │   ├── lm_studio_client.py
│   │   ├── clipboard_service.py
│   │   └── file_service.py
│   │
│   ├── Session/
│   │   └── history.py
│   │
│   ├── Utils/
│   │   └── validators.py
│   │
│   ├── Config/
│   │   ├── settings.json
│   │   └── settings.py
│   │
│   └── Assets/
│       └── Screenshots/
│           ├── main_ui.png
│           ├── example_generation.png
│           └── settings.png
│
├── README.md
└── LICENSE

## Known Limitations

- Requires LM Studio to be running locally
- No cloud-based model support
- Performance depends on local hardware

## Contributors

- Team Leader: Tunay Can (UI)
- Ömer Kayra Dündar (UI, Session and Utils)
- Teoman Ünal (UI, Config)
- Alim Barış Sevindik (Core)
- Yuşa Alperen Turak (Services)
- Berkay Avcıoğlu (Services)

## License

This project is licensed under the MIT License.
