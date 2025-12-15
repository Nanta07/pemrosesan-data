import pandas as pd

def transform_data(df):
    # Hapus baris dengan data penting yang kosong
    df = df.dropna(subset=['Title', 'Price', 'Size', 'Gender'])
    df = df.drop_duplicates()

    # Hapus produk tidak valid
    df = df[~df['Title'].str.contains('Unknown Product', case=False)]

    # Membersihkan dan konversi Price dari USD (string) ke float lalu ke IDR
    df['Price'] = df['Price'].fillna('').astype(str).str.replace('$', '', regex=False)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce') * 16000

    # Membersihkan dan konversi Rating
    if df['Rating'].dtype == 'object':
        df['Rating'] = df['Rating'].str.extract(r'(\d+\.\d+)', expand=False)
        df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

    # Membersihkan dan konversi Colors
    df['Colors'] = df['Colors'].fillna('').astype(str).str.extract(r'(\d+)', expand=False)
    df['Colors'] = pd.to_numeric(df['Colors'], errors='coerce')
    df['Colors'] = pd.to_numeric(df['Colors'], errors='coerce').fillna(0).astype(int)

    # Membersihkan Size dan Gender
    df['Size'] = df['Size'].str.replace('Size: ', '', regex=False)
    df['Gender'] = df['Gender'].str.replace('Gender: ', '', regex=False)

    df = df.dropna(subset=['Price', 'Rating'])

    return df.reset_index(drop=True)