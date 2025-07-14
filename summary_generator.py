def generate_summary(df):
    category_totals = df.groupby('Category')['Amount'].sum().to_dict()
    summary_lines = []
    for category, total in category_totals.items():
        top_items = (
            df[df['Category'] == category]
            .sort_values(by='Amount', ascending=False)
            .head(2)['Description']
            .tolist()
        )
        items_str = ', '.join(top_items)
        summary_lines.append(f"{category}: ₹{total:.2f} (e.g., {items_str})")
    return "\n".join(summary_lines)