import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_expense_story(summary):
    prompt = f"""
    Based on the user's monthly expense summary below, write a 3-scene creative and funny story:

    {summary}

    Use a Gen Z tone, pop culture references, and emojis. Return clear scene breaks.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Story error] {e}"