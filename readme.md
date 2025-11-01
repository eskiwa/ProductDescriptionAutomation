.

🛍️ AI Product Description Generator

A simple Python script that uses OpenAI’s ChatGPT API to automatically generate engaging e-commerce product descriptions from a CSV file.

Provide a file named products.csv containing product data — including name, category, and features — and the script creates a new CSV file with AI-written descriptions ready for your online store.

🚀 Features

🧠 Uses ChatGPT (gpt-4o-mini) to write professional, natural-sounding product descriptions

📂 Reads data from a simple CSV file (name, category, features)

💾 Automatically saves results in a new file

🔢 Auto-renames output (e.g., products_with_descriptions1.csv, products_with_descriptions2.csv) if a file already exists

⚙️ Lightweight, fast, and fully customizable

⚙️ Setup Instructions

Clone this repository

git clone https://github.com/yourusername/ai-product-description-generator.git
cd ai-product-description-generator

Install dependencies

pip install openai python-dotenv

Create your .env file

OPENAI_API_KEY=your_api_key_here

Prepare your input file
Create a file named products.csv in the same directory with the columns:
name,category,features

Run the script

python generate_descriptions.py

Check your output
Your generated file will appear as:

products_with_descriptions.csv

If it already exists, the script will automatically save as:

products_with_descriptions1.csv
products_with_descriptions2.csv
...

💡 Use Cases

Shopify, WooCommerce, or Etsy sellers

Amazon product listings

Bulk e-commerce content generation

Portfolio or automation demo project

🧑‍💻 Tech Stack

Python 3

OpenAI GPT-4o-mini

CSV (built-in Python library)

📜 License

This project is open-source under the MIT License
.
