import camelot
import pandas as pd
import re

def extract_tables_from_pdf(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages='2-end', flavor='lattice')
    return tables

def process_table(tables):
    all_data = []
    for table in tables:
        df = table.df

        # Optional: Debug output
        # print("Original DataFrame:")
        # print(df)

        if df.shape[0] > 1:
            df_filtered = df.iloc[1:, 1]  # Second column, skip header

            df_filtered = df_filtered.apply(lambda x: re.sub(r'[^\d.]+', '', x))
            df_filtered = pd.to_numeric(df_filtered, errors='coerce')
            df_filtered = df_filtered.dropna()

            # print("Cleaned DataFrame:")
            # print(df_filtered)

            all_data.extend(df_filtered.tolist())

    return all_data

def save_to_csv(data, csv_path):
    df = pd.DataFrame(data, columns=['Licensed Frequency'])
    df.to_csv(csv_path, index=False)

def main(pdf_path, csv_path):
    tables = extract_tables_from_pdf(pdf_path)
    all_data = process_table(tables)
    save_to_csv(all_data, csv_path)

if __name__ == "__main__":
    # You can test manually with a local file
    sample_pdf = "sample.pdf"
    output_csv = "output.csv"
    main(sample_pdf, output_csv)
