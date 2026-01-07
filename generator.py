def build_prompt(topic, content_type, tone, length, temperature):
    return [
        {"role": "system", "content": "You are a local AI text generator."},
        {
            "role": "user",
            "content": (
                f"Write a {length} {content_type} in a {tone} tone about: {topic}. "
                f"Creativity level: {temperature}."
            )
        }
    ]