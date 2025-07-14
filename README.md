# Visual Expense Story Generator
### ✨ A Gen-Z-inspired interactive web app that transforms your boring bank statement into a fun, visual, and narrated expense story — complete with category-wise charts and a smart budget breakdown!
---
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/LLM-Gemini-ffca28?logo=google&logoColor=white)](https://ai.google.dev)
[![Deep Translator](https://img.shields.io/badge/Translation-Deep%20Translator-4cae4c)](https://pypi.org/project/deep-translator)
[![Matplotlib](https://img.shields.io/badge/Graphs-Matplotlib-3776AB)](https://matplotlib.org/)
[![gTTS](https://img.shields.io/badge/Text%20To%20Speech-gTTS-lightgrey)](https://pypi.org/project/gTTS/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🔧 Features

* ✨ **Expense Story Generation**

  Uses an LLM (Gemini API) to generate a relatable, fun story based on categorized expenses.

* 🔪 **Smart Categorization**

  Categorizes expenses using AI-driven classification of descriptions.

* 📊 **Visual Charts**

  Category-wise expense bar chart

* 🌍 **Multilingual Support**

  Translate stories to Hindi, Spanish, French, German, and more with Deep Translator.

* 🎤 **Text-to-Speech Narration**

  Audio playback of the expense story using `gTTS`

---



## 📂 Project Structure

```bash
.
├── expense_story_ui.py         # Streamlit UI
├── parser.py                   # CSV parsing and preprocessing
├── gemini_categorizer.py       # Gemini API-based category classification
├── storygen.py                 # LLM story generation logic
├── summary_generator.py        # Text summary for chart and story base
├── requirements.txt            # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/expense-story-generator.git
cd expense-story-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

### 4. Run the app

```bash
streamlit run expense_story_ui.py
```

---

## ⚙️ How It Works

* 📥 Upload CSV: 
Accepts your monthly bank transactions in CSV format and parses the file to categorize each entry based on its description.

* 📊 Visual Insights: 
A category-wise horizontal bar chart is created showing how much you spent on food, shopping, travel, etc., for the month.

* 📖 Expense Story Generation:
A creative story is spun around your expenses using LLM magic. The story mimics a fun, human narration — sometimes sarcastic, sometimes caring — making the budgeting experience feel more like a conversation.

  Example Opening:
  "Aanya’s wallet went through a whole saga this month — and not the kind with a happy ending. From panic-fueled Swiggy cravings at 1 AM to an impulsive ‘just one item’ Amazon spree, her budget totally ghosted her. Clearly, adulting is hard when dopamine hits come with UPI receipts."

* 🌍 Translation & Voice
Translate the story into your favorite language and listen to it aloud.

---

## 🧠 Behind the Scenes

* Gemini: Generates creative summaries and classifies spending categories based on raw descriptions.
* gTTS: Converts stories to natural-sounding speech.
* Deep Translator: Supports multilingual narration.
* Matplotlib: Renders clean, professional graphs.


## ☑️ To-Do / Future Improvements

* 📹 Image or video story generation using Replicate or SDXL
* 🏦 Monthly savings recommendations
* 📥 Support Excel or Google Sheets as input
* 🔔 50-30-20 Budget Rule Comparison with color-coded bars (green: under, red: over)
* ✨ UI animations and downloadable PDF reports

---

## 🚀 Powered By

* [Google Gemini API](https://ai.google.dev)
* [Streamlit](https://streamlit.io)
* [Matplotlib](https://matplotlib.org)
* [gTTS](https://pypi.org/project/gTTS)
* [Deep Translator](https://pypi.org/project/deep-translator)

---


Feel free to fork, star, or contribute! 

"Budgeting doesn’t have to be boring. Make your money talk back — literally!"
