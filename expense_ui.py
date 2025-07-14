# expense_story_ui.py

import streamlit as st
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import tempfile
import os
import numpy as np
from gtts import gTTS
from deep_translator import GoogleTranslator

from parser import parse_expense_csv
from gemini_categorizer import apply_gemini_categorization
from summary_generator import generate_summary
from storygen import generate_expense_story

st.set_page_config(page_title="Visual Expense Story Generator", layout="centered")
st.title("📖 Visual Expense Story Generator")
st.markdown("Upload your monthly bank statement to get a fun, Gen Z-style expense story.")

# Language selection for text-to-speech
lang_options = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de"
}
selected_lang = st.selectbox("🌐 Select narration language", list(lang_options.keys()))
lang_code = lang_options[selected_lang]

# Session state to preserve data
if "story" not in st.session_state:
    st.session_state.story = None
if "df" not in st.session_state:
    st.session_state.df = None
if "summary" not in st.session_state:
    st.session_state.summary = None
if "translated_story" not in st.session_state:
    st.session_state.translated_story = None

uploaded_file = st.file_uploader("📄 Upload CSV File", type="csv")

if uploaded_file and st.session_state.story is None:
    try:
        content_str = uploaded_file.getvalue().decode("utf-8").strip()
        if not content_str:
            st.error("⚠️ Uploaded file is empty.")
        else:
            content = StringIO(content_str)
            raw_df = pd.read_csv(content)
            st.subheader("🧾 Raw Data Preview")
            st.dataframe(raw_df.head())

            content.seek(0)
            df = parse_expense_csv(content)
            st.success("CSV parsed and normalized successfully!")

            with st.spinner("Classifying with Gemini..."):
                df = apply_gemini_categorization(df)

            summary = generate_summary(df)
            story = generate_expense_story(summary)

            st.session_state.df = df
            st.session_state.summary = summary
            st.session_state.story = story
            st.session_state.translated_story = story  # Default to English

            st.subheader("📊 Expense Summary")
            st.text(summary)

            st.subheader("📈 Category-wise Expense Chart")
            category_totals = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
            fig, ax = plt.subplots()
            category_totals.plot(kind='barh', ax=ax, color='skyblue')
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")

# Display previously generated story and allow TTS in selected language
if st.session_state.story:
    st.subheader("🎙️ Your Expense Story")

    if lang_code != "en":
        with st.spinner("Translating story..."):
            try:
                st.session_state.translated_story = GoogleTranslator(source='auto', target=lang_code).translate(st.session_state.story)
            except Exception:
                st.warning("⚠️ Translation failed. Showing original story.")
                st.session_state.translated_story = st.session_state.story
    else:
        st.session_state.translated_story = st.session_state.story

    st.markdown(st.session_state.translated_story.replace("\n", "  \n"))

    # Text-to-speech with selected language
    tts = gTTS(text=st.session_state.translated_story, lang=lang_code)
    temp_path = os.path.join(tempfile.gettempdir(), "story_audio.mp3")
    tts.save(temp_path)
    st.audio(temp_path, format="audio/mp3")

    # st.subheader("💰 Budget Split vs Actual")
    # income = st.number_input("Enter your total monthly income (in ₹):", min_value=0, value=50000, step=1000)
    # if income > 0 and st.session_state.df is not None:
    #     df = st.session_state.df
    #     total_spent = df['Amount'].sum()

    #     recommended = {
    #         "Needs (50%)": 0.5 * income,
    #         "Wants (30%)": 0.3 * income,
    #         "Savings (20%)": 0.2 * income
    #     }

    #     actual = {
    #         "Needs (50%)": df[df['Category'].isin(["food", "bills", "utilities", "groceries"])]
    #                             ['Amount'].sum(),
    #         "Wants (30%)": df[df['Category'].isin(["shopping", "entertainment", "travel", "eating out"])]
    #                             ['Amount'].sum(),
    #         "Savings (20%)": max(income - total_spent, 0)
    #     }

    #     st.subheader("📉 50-30-20 Budget Comparison (Color-coded)")

    #     comp_df = pd.DataFrame({"Recommended": recommended, "Actual": actual})
    #     diff = comp_df["Actual"] - comp_df["Recommended"]

    #     labels = comp_df.index
    #     x = np.arange(len(labels))
    #     width = 0.35

    #     color_list = ["green" if v <= 0 else "red" for v in diff]

    #     fig2, ax2 = plt.subplots()
    #     ax2.bar(x - width/2, comp_df["Recommended"], width, label='Recommended', color='lightgray')

    #     for i in range(len(labels)):
    #         ax2.bar(x[i] + width/2, comp_df["Actual"].iloc[i], width,
    #                 label='Actual' if i == 0 else "", color=color_list[i])

    #     ax2.set_ylabel("Amount (₹)")
    #     ax2.set_title("Actual vs Recommended Budget")
    #     ax2.set_xticks(x)
    #     ax2.set_xticklabels(labels)
    #     ax2.legend()

    #     st.pyplot(fig2)
    #     st.write("**💡 Tip:** Green = within budget, Red = overspent**")

st.markdown("---")
st.caption("Built with ❤️ using Gemini, gTTS, Matplotlib, Deep Translator + Streamlit")
