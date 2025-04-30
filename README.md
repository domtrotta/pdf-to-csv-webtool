# Ofcom PDF to CSV Converter (Web Tool)

This is a self-hosted web tool built with Flask and pdfplumber to extract licensed frequency data from Ofcom-issued PDFs. It scans the entire document and extracts all valid frequencies (e.g., `654.22500 MHz`) into a clean, sorted CSV file.


---

### 🌐 Live Demo
👉 [https://pdf.trottadomenico.co.uk](https://pdf.trottadomenico.co.uk)

[![Website Status](https://img.shields.io/website?url=https%3A%2F%2Fpdf.trottadomenico.co.uk)](https://pdf.trottadomenico.co.uk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

### ✅ Features
- Upload Ofcom PDF files from your browser
- Extracts frequency data using text parsing (regex)
- Cleans, deduplicates, and sorts results
- Exports a downloadable CSV
- Mobile-friendly UI with status popups

---

### 🧪 How to Use
1. Visit the live tool: [https://pdf.trottadomenico.co.uk](https://pdf.trottadomenico.co.uk)
2. Upload your Ofcom-issued frequency schedule (PDF)
3. Click **Convert to CSV**
4. The CSV will download automatically with all valid frequencies extracted

---

### 📥 What to Do After Download
After downloading the CSV:

- Go to your RF coordination or audio software
- Upload the CSV file to your **Inclusion Group**
- Remember to assign your devices to the group so frequencies apply

---

### ⚙ Tech Stack
- Python + Flask
- pdfplumber (no Camelot or Ghostscript needed)
- TailwindCSS for frontend
- SweetAlert2 for interactive feedback
- Gunicorn + Nginx on Ubuntu VPS

---

### 🧑‍💻 Maintained by Dom Trotta
For support or ideas, feel free to reach out or fork the repo.

---

> "Tools like this save time in high-pressure show environments. Built for real workflows, by someone who gets it."
