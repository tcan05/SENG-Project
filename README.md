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
cd Project
```
3. Run the application:
```bash
python main.py
```
> Make sure LM Studio is running and a model is loaded before starting the application.

## Contributors

- Team Leader: Tunay Can (UI)
- Ömer Kayra Dündar (UI, Session and Utils)
- Teoman Ünal (UI, Config)
- Alim Barış Sevindik (Core)
- Yuşa Alperen Turak (Services)
- Berkay Avcıoğlu (Services)
