# imagegen.py

import replicate
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
replicate_client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

# Define styles
STYLE_OPTIONS = {
    "Default (no style)": "",
    "Cinematic": ", cinematic lighting, dramatic scene",
    "Pixar": ", pixar style, 3D animated, cheerful",
    "Surreal": ", surreal, dreamlike, high contrast colors",
    "Cyberpunk": ", neon lights, futuristic, cyberpunk setting",
    "Watercolor Painting": ", watercolor style, soft brush strokes"
}

def generate_image_replicate(prompt, style_modifier=""):
    try:
        full_prompt = prompt.strip() + style_modifier
        output = replicate_client.run(
            "black-forest-labs/flux-kontext-pro:89ab24c38c3ef0d881ff861e2cbb3b80f4f70e8b7db728f8f98ad4f168b3e317",
            input={
                "prompt": full_prompt,
                "width": 1024,
                "height": 1024,
                "num_inference_steps": 25,
                "guidance_scale": 7.5,
                "scheduler": "K_EULER_ANCESTRAL"
            }
        )
        return output[0]  # Return the image URL
    except Exception as e:
        return f"[Image error] {e}"
