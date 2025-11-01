import csv
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Input file
input_file = "products.csv"

# Determine output file name (auto-increment if it already exists)
base_name = "products_with_descriptions"
extension = ".csv"
output_file = base_name + extension
counter = 1

while os.path.exists(output_file):
    output_file = f"{base_name}{counter}{extension}"
    counter += 1

print(f"💾 Output file will be saved as: {output_file}\n")

# Open the input CSV
with open(input_file, mode="r", encoding="utf-8") as csv_in:
    reader = csv.DictReader(csv_in)
    fieldnames = reader.fieldnames + ["description"]

    # Open the output CSV
    with open(output_file, mode="w", newline="", encoding="utf-8") as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
        writer.writeheader()

        # Loop through each product
        for row in reader:
            prompt = f"""
            Write a short, engaging product description for an online store.

            Product name: {row['name']}
            Category: {row['category']}
            Features: {row['features']}
            """

            # Generate description using ChatGPT
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system",
                        "content": "You are a professional e-commerce copywriter."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
            )

            description = response.choices[0].message.content.strip()
            row["description"] = description
            writer.writerow(row)

            print(f"✅ Generated description for: {row['name']}")

print(
    f"\n🎉 All product descriptions generated successfully and saved to '{output_file}'")
