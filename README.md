# 📄 Ofcom PDF to CSV Web Tool

A sleek, web-based tool to convert structured Ofcom-style PDF documents into clean CSVs — built for quick AV/event tech workflows.

---

### 🔗 Try It Live

👉 [https://pdf-to-csv-webtool.onrender.com](https://pdf-to-csv-webtool.onrender.com)

Upload an Ofcom PDF, extract licensed frequency data, and download it as a CSV file ready for use.

---

### 🛠️ Features

- 📤 Upload PDF files directly from your browser
- 📊 Extracts frequency data (from page 2 onward)
- 📁 Outputs a clean CSV
- 🌙 Dark mode UI + mobile-friendly
- 💬 SweetAlert spinner feedback
- 🔧 Designed for AV/RF techs using Inclusion Groups

---

### 📥 What to Do After You Download the CSV

Once you’ve converted your PDF and downloaded the CSV:

1. Go to your coordination platform or system
2. Create a new **Inclusion Group**
3. Upload the CSV into that group
4. ✅ Make sure to **assign the correct devices** to the Inclusion Group so the frequencies apply correctly!

> Without adding devices, your coordination will not reflect the CSV data.

---

### 💻 Run Locally (Dev Mode)

```bash
git clone https://github.com/domtrotta/pdf-to-csv-webtool.git
cd pdf-to-csv-webtool
pip install -r requirements.txt
python app.py
