# Article Generator

A Python script that generates article titles, lets you select the best one, then creates a full article in markdown format.

## Features
- Generates multiple title options using OpenAI
- Interactive title selection
- Produces well-formatted markdown articles
- Automatically saves articles with timestamps

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/pallavi1428/article.git
   cd article

2. Create and activate virtual environment:
python -m venv .venv
source .venv/Scripts/activate  # Linux/Mac
.\.venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Create .env file:
OPENAI_API_KEY=your_api_key_here

Usage
Run the script: