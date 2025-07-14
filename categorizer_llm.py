import openai
from env import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def classify_description_llm(description):
    prompt = f"""
    Categorize the following transaction into one of the following:
    - Food & Dining
    - Travel & Transport
    - Shopping
    - Utilities
    - Rent & Housing
    - Entertainment & Subscriptions
    - Education
    - Medical
    - Others

    Only return the category name.

    Description: "{description}"
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=20
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"[LLM error] {description}: {e}")
        return "Others"

def apply_llm_categorization(df):
    df['Description'] = df['Description'].astype(str).str.lower().str.strip()
    unique_descs = df['Description'].unique()
    
    print(f"🧠 LLM classifying {len(unique_descs)} unique descriptions...")

    # Efficient lookup using LLM
    desc_to_category = {desc: classify_description_llm(desc) for desc in unique_descs}
    
    df['Category'] = df['Description'].map(desc_to_category)
    return df
