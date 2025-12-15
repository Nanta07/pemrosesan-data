from utils.extract import extract_data
import pandas as pd

def test_extract_data():
    df = extract_data()
    assert isinstance(df, pd.DataFrame), "Hasil extract_data harus berupa DataFrame"
    assert not df.empty, "DataFrame hasil extract tidak boleh kosong"
    assert {'Title', 'Price', 'Rating', 'Colors', 'Size', 'Gender', 'Timestamp'}.issubset(df.columns), "Kolom tidak lengkap"