from pathlib import Path

def save_text(content: str, path: str):
    file_path = Path(path)

    if file_path.exists():
        raise FileExistsError(f"File already exists.")
    
    try:
        file_path.write_text(content, encoding = "utf-8")
    
    except PermissionError:
        raise PermissionError("Permission denied while saving file.")


def open_text(path: str) -> str:
    return Path(path).read_text(encoding = "utf-8")


def save_chat(messages, path: str):

    with open(path, 'w', encoding = 'utf-8') as f:

        for role, msg in messages:

            prefix = "User" if role == "user" else "Bot"
            f.write(f"{prefix}: {msg}\n\n")