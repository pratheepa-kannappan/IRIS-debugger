def build_prompt(error_text):
    return f"""
You are an expert Python debugger.

Analyze the following error and respond ONLY in JSON format:

Error:
{error_text}

Format:
{{
  "meaning": "...",
  "causes": ["...", "..."],
  "fix": "...",
  "example": "..."
}}

Keep explanation simple and beginner-friendly.
"""
