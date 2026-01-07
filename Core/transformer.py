def transform_text(text, target_format):
    return [
        {"role": "system", "content": "You transform text into a new format."},
        {
            "role": "user",
            "content": f"Transform the following text into {target_format}:\n{text}"
        }
]