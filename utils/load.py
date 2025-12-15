import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load_to_csv(df: pd.DataFrame, filename: str = "products.csv") -> None:
    """Simpan DataFrame ke file CSV."""
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Data saved to CSV: {filename}")

def load_to_gsheet(df: pd.DataFrame, spreadsheet_name: str = "produk-fashion") -> None:
    """Upload DataFrame ke Google Sheets."""
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "google-sheets-api.json", scope)
    client = gspread.authorize(creds)

    try:
        spreadsheet = client.open(spreadsheet_name)
    except gspread.SpreadsheetNotFound:
        print(f"Spreadsheet '{spreadsheet_name}' tidak ditemukan. Pastikan sudah dibuat dan dibagikan ke service account.")
        return

    worksheet = spreadsheet.sheet1
    worksheet.clear()

    # Update worksheet with header + data
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print(f"Data uploaded to Google Sheets: {spreadsheet_name}")