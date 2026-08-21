# TrustCheck – Agentic COD Risk & Address Validation System

## Problem

Cash-on-delivery (COD) orders carry high risk from fake, incomplete, or malformed 
addresses — leading to failed deliveries, return-to-origin (RTO) costs, and revenue 
loss for merchants.

## What it does

TrustCheck is an LLM-powered agent that evaluates address quality *before* dispatch. 
It flags malformed addresses, pincode-locality mismatches, and patterns associated 
with high-RTO orders, returning a structured, schema-enforced risk assessment that 
merchants can act on directly (auto-approve, hold for review, or convert to prepaid).

## Output schema

Every response is validated against this JSON schema:

```json
{
  "risk_score": "integer (0-100)",
  "risk_level": "low | medium | high",
  "reason_code": "string explaining the decision",
  "flags": ["array of specific risk indicators"]
}
```

## How to run

1. Get a free API key from [console.groq.com](https://console.groq.com)
2. Set it as an environment variable: