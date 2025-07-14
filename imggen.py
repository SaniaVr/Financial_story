import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_image(prompt):
    image_prompt = f"""Generate a vivid, artistic illustration of this scene:
    {prompt}"""
    try:
        response = model.generate_content(image_prompt)
        return response.text.strip()  # Normally, Gemini doesn't return actual images yet
    except Exception as e:
        return f"[Image error] {e}"