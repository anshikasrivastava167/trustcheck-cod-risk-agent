import json
import os
from groq import Groq
from schema import RISK_SCHEMA

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def evaluate_address(address: str, pincode: str = "") -> dict:
    prompt = f"""You are a fraud-risk agent for a cash-on-delivery (COD) e-commerce order.
Evaluate this address for delivery risk (malformed text, pincode mismatch, incomplete details, gibberish, PO box, etc).
Address: {address}
Pincode: {pincode}
Respond ONLY with a JSON object matching this schema:
{json.dumps(RISK_SCHEMA, indent=2)}
"""
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
    )
    result = json.loads(response.choices[0].message.content)
    return result

if __name__ == "__main__":
    sample = evaluate_address("House no 12, xyzxyz street, asdf", "000000")
    print(json.dumps(sample, indent=2))
