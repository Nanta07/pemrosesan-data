import pandas as pd
from utils.load import load_to_csv

def test_load_to_csv(tmp_path):
    df = pd.DataFrame({
        'Title': ['Cool Shirt'],
        'Price': [400000],
        'Rating': [4.5],
        'Colors': [3],
        'Size': ['L'],
        'Gender': ['Male'],
        'Timestamp': ['2024-01-01T00:00:00']
    })

    file_path = tmp_path / "test_output.csv"
    load_to_csv(df, filename=file_path)

    assert file_path.exists(), "File CSV tidak dibuat"
    assert file_path.stat().st_size > 0, "File CSV kosong"

    df_loaded = pd.read_csv(file_path)
    pd.testing.assert_frame_equal(df_loaded, df)