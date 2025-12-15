from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_gsheet

def main():
    raw_data = extract_data()
    print("Total produk yang diambil:", raw_data.shape[0])
    print("Extracted data:", raw_data.shape)

    clean_data = transform_data(raw_data)
    print("Transformed data:", clean_data.shape)

    load_to_csv(clean_data)

    load_to_gsheet(clean_data, spreadsheet_name="produk-fashion")

if __name__ == "__main__":
    main()
