import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re

def extract_data():
    data = []

    # URL untuk halaman pertama berbeda dari halaman lainnya
    urls = ["https://fashion-studio.dicoding.dev/"] + [f"https://fashion-studio.dicoding.dev/page{page}" for page in range(2, 51)]

    for page, url in enumerate(urls, start=1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Gagal mengambil halaman {page}: {e}")
            continue

        soup = BeautifulSoup(response.content, "html.parser")
        products = soup.find_all("div", class_="collection-card")

        if not products:
            print(f"Tidak ada produk ditemukan di halaman {page}.")
            continue

        for product in products:
            try:
                title = product.find("h3", class_="product-title").text.strip()

                price_text = product.find("span", class_="price").text.strip().replace("$", "")
                price = float(price_text)

                all_p = product.find_all("p")

                rating = None
                colors = 0
                size = None
                gender = None

                for p in all_p:
                    text = p.text.strip().lower()

                    if "rating" in text:
                        match = re.search(r'(\d+(\.\d+)?)', text)
                        if match:
                            rating = float(match.group(1))
                    elif "color" in text:
                        match = re.search(r'(\d+)', text)
                        if match:
                            colors = int(match.group(1))
                    elif "size" in text:
                        size = text.replace("size:", "").strip()
                    elif "gender" in text:
                        gender = text.replace("gender:", "").strip()

                # Lewati produk jika ada field penting yang hilang
                if None in [title, price, size, gender]:
                    continue

                data.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Colors": colors,
                    "Size": size,
                    "Gender": gender,
                    "Timestamp": datetime.now().isoformat()
                })

            except AttributeError:
                continue  # Lewati produk yang tidak lengkap

    df = pd.DataFrame(data)
    print(f"Total produk yang diambil: {len(df)}")
    return df