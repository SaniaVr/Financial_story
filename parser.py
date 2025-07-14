import pandas as pd

def parse_expense_csv(file_path):
    df = pd.read_csv(file_path)

    # Map CSV column names to expected names
    column_mapping = {
        'Narration / Description': 'Description',
        'Amount (₹)': 'Amount',
        'Balance (₹)': 'Balance',
        'Reference No.': 'Reference Number'
    }
    
    # Rename columns to match expected format
    df = df.rename(columns=column_mapping)
    
    # Check for required columns after renaming
    required_columns = ['Date', 'Description', 'Amount', 'Type', 'Balance', 'Mode', 'Reference Number']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
    df['Description'] = df['Description'].astype(str).str.lower()
    df['Type'] = df['Type'].astype(str).str.lower()
    df = df[df['Type'] == 'debit']
    return df