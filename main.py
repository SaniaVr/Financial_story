from parser import parse_expense_csv
from gemini_categorizer import apply_gemini_categorization
from summary_generator import generate_summary
from storygen import generate_expense_story
from imggen import generate_image


def main():
    print("📥 Parsing CSV...")
    df = parse_expense_csv("expenses.csv")

    print("🔍 Categorizing using Gemini...")
    df = apply_gemini_categorization(df)

    print("🧾 Generating summary...")
    summary = generate_summary(df)
    print("\n--- Expense Summary ---\n", summary)

    print("\n📖 Generating story...")
    story = generate_expense_story(summary)
    print("\n--- Story ---\n", story)

    print("\n🎨 Generating scene descriptions...")
    scenes = story.split("\n\n")[:3]
    for i, scene in enumerate(scenes):
        print(f"\nScene {i+1} Text:\n{scene}")
        image_result = generate_image(scene)
        print(f"Scene {i+1} Visual:", image_result)


if __name__ == "__main__":
    main()