from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def classify_description_gemini(description):
    prompt = f"""
    Classify the following transaction description into one of these categories:
    - Food & Dining
    - Travel & Transport
    - Shopping
    - Utilities
    - Rent & Housing
    - Entertainment & Subscriptions
    - Education
    - Medical
    - Others

    Return only the category name.

    Description: "{description}"
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip().split("\n")[0]
    except Exception as e:
        print(f"Error with description '{description}': {e}")
        return "Others"

def apply_gemini_categorization(df):
    df['Description'] = df['Description'].astype(str).str.lower().str.strip()
    unique_descs = df['Description'].unique()
    print(f"🔎 Gemini categorizing {len(unique_descs)} unique descriptions...")
    desc_to_category = {desc: classify_description_gemini(desc) for desc in unique_descs}
    df['Category'] = df['Description'].map(desc_to_category)
    return df

print("🔐 Loaded Gemini API key:", os.getenv("GOOGLE_API_KEY"))
# Ensure the API key is set