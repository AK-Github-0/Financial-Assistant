import pandas as pd

def load_excel(file_path: str) -> pd.DataFrame:
    return pd.read_excel(file_path)

def analyze_data(df: pd.DataFrame) -> dict:
    summary = {
        'total_rows': len(df),
        'columns': list(df.columns),
        'mean_values': df.mean(numeric_only=True).to_dict(),
        'sum_values': df.sum(numeric_only=True).to_dict()
    }
    return summary
