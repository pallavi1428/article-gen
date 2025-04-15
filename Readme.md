# 📝 Article Generator

A Python script that generates article titles using OpenAI, lets you pick your favorite, and creates a full article in markdown format.

---

## 🚀 Features
- Multiple article title suggestions using OpenAI
- Choose the best title interactively
- Generates a well-structured article in Markdown
- Automatically saves articles with timestamps

---

## ⚙️ Setup

### 1. Clone the repository:
```bash
git clone https://github.com/pallavi1428/article-gen.git
cd article-gen
```

### 2. Create and activate a virtual environment:
**Windows**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**Mac/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root directory and add your OpenAI key:
```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the script:
```bash
python article_generator.py
```

Then follow the prompts to:
- Enter your topic
- Pick the best title from AI suggestions
- Auto-generate and save the article

---

## ✅ Requirements
- Python 3.12
- OpenAI API key

---

## 📌 Notes
- Generated articles are saved inside the `articles/` folder.
- Make sure your `.env` file is set up properly before running the script.

---
