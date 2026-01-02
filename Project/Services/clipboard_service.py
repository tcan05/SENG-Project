from PyQt6.QtWidgets import QApplication

def copy_to_clipboard(text: str):

    try:
        QApplication.clipboard().setText(text)
        
    except Exception:
        raise RuntimeError("Clipboard operation failed.")