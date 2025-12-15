import pandas as pd
import numpy as np
import pytest
from utils.transform import transform_data

def test_transform_data():
    raw_data = pd.DataFrame({
        'Title': ['Cool Shirt', 'Unknown Product', None],
        'Price': ['$25.00', '$30.00', '$40.00'],
        'Rating': ['4.5 stars', '4.8 stars', '5.0 stars'],
        'Colors': ['Colors: 3', 'Colors: 5', 'Colors: 2'],
        'Size': ['Size: L', 'Size: M', 'Size: S'],
        'Gender': ['Gender: Male', 'Gender: Female', 'Gender: Unisex'],
        'Timestamp': ['2024-01-01T00:00:00'] * 3
    })

    df = transform_data(raw_data)

    assert df.shape[0] == 1, "Hanya satu baris data valid yang harus tersisa"
    assert df['Price'].iloc[0] == pytest.approx(25.00 * 16000), "Harga tidak dikonversi ke IDR dengan benar"
    assert isinstance(df['Rating'].iloc[0], float), "Rating harus berupa float"
    assert isinstance(df['Colors'].iloc[0], (int, np.integer)), "Colors harus berupa integer"
    assert df['Size'].iloc[0] == 'L', "Size tidak dibersihkan dengan benar"
    assert df['Gender'].iloc[0] == 'Male', "Gender tidak dibersihkan dengan benar"
    assert df['Title'].iloc[0] == 'Cool Shirt', "Judul tidak sesuai"