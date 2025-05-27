# Search Engine using Exa

## 🔍 Overview

This project is a **desktop GUI search engine** powered by the [Exa API](https://exa.ai), built using **Python** and **Tkinter**. It allows users to search for keywords and fetch relevant links (from Google or general web) in a beautifully styled, scrollable graphical interface.

---

## 🧠 Features

* 🔎 Keyword-based search with Exa API
* 🖥️ Graphical interface using Tkinter
* 🌐 Clickable search results that open in browser
* 🎨 Custom styles for dark mode aesthetic
* 📜 Scrollable results area for better UX

---

## 🚀 Technologies Used

| Tech       | Purpose                     |
| ---------- | --------------------------- |
| Python 3.x | Core programming language   |
| Tkinter    | GUI development             |
| Exa API    | Search engine functionality |
| Webbrowser | To open URLs in browser     |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/joshuahanielgts/search-engine.git
```

### 2. Install dependencies

```bash
pip install exa_py
```

### 3. Run the app

```bash
python app.py
```

---

## 🛠️ Configuration

Replace the API key in the script with your own from [Exa.ai](https://exa.ai):

```python
exa = Exa('YOUR_EXA_API_KEY')
```

---

## 💡 Example

```text
Search term: “AI trends 2025”

Result:
Title: Top AI Trends to Watch in 2025
URL: https://www.google.com/example-link
```

---

## 📚 File Structure

```
exa-tkinter-search/
├── app.py               # Main GUI application
├── README.md            # Project documentation
└── License              # License
```

---
