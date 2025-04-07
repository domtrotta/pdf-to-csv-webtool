# app.py — Flask backend for the PDF to CSV web tool

from flask import Flask, request, send_file, render_template, jsonify
import tempfile
import os
from Ofcom_PDF_to_CSV_Converter import main as convert_pdf_to_csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No PDF file uploaded'}), 400

    pdf_file = request.files['pdf']

    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = os.path.join(tmpdir, pdf_file.filename)
        csv_path = os.path.join(tmpdir, 'output.csv')

        pdf_file.save(pdf_path)

        try:
            convert_pdf_to_csv(pdf_path, csv_path)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        return send_file(csv_path, as_attachment=True, download_name='converted.csv')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
