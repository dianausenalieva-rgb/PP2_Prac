import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

prices = re.findall(r'\d[\d\s]*,\d{2}|\d[\d\s]*', text)
prices_clean = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

products = re.findall(r'\d+\.\s*(.*?)\s+\d+,\d{2}', text)

total_amount = sum(prices_clean)

date_time_match = re.search(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}', text)
date_time = date_time_match.group() if date_time_match else None

payment_match = re.search(r'Банковская карта|Наличные|Card|Cash', text)
payment_method = payment_match.group() if payment_match else None

receipt_data = {
    "products": products,
    "prices": prices_clean,
    "total_amount": total_amount,
    "date_time": date_time,
    "payment_method": payment_method
}

print(json.dumps(receipt_data, indent=4, ensure_ascii=False))