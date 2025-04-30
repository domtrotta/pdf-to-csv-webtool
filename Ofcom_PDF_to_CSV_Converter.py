import pdfplumber
import pandas as pd
import re

def extract_frequencies_from_pdf(pdf_path):
    frequencies = []
    pattern = re.compile(r"\b\d{3}\.\d{3,5}\b")

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                matches = pattern.findall(text)
                frequencies.extend(matches)

    # Remove duplicates and sort
    unique_freqs = sorted(set(frequencies), key=lambda x: float(x))
    return unique_freqs

def save_to_csv(data, csv_path):
    df = pd.DataFrame(data, columns=['Licensed Frequency (MHz)'])
    df.to_csv(csv_path, index=False)
    print(f"Data saved to {csv_path}")

def main(pdf_path, csv_path):
    freqs = extract_frequencies_from_pdf(pdf_path)
    save_to_csv(freqs, csv_path)

if __name__ == "__main__":
    pdf_path = "sample.pdf"
    csv_path = "output.csv"
    main(pdf_path, csv_path)

