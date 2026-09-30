# TrustCheck – Agentic COD Risk & Address Validation System

🔗 **Live app:** [trustcheck-cod-risk-agent-2gymxp3i5xeksejwqgygjb.streamlit.app](https://trustcheck-cod-risk-agent-2gymxp3i5xeksejwqgygjb.streamlit.app)

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

\`\`\`json
{
  "risk_score": "integer (0-100)",
  "risk_level": "low | medium | high",
  "reason_code": "string explaining the decision",
  "flags": ["array of specific risk indicators"]
}
\`\`\`

## Engineering note: deployment fix

The app originally called Groq's API, which worked locally but returned a
403 "Access denied" error once deployed to Streamlit Cloud. Groq blocks
requests from data-center and cloud IP ranges as an anti-abuse measure,
which affected requests coming from Streamlit's servers even though the
same key worked fine from a local machine. Fixed by migrating to
OpenRouter, which uses the same OpenAI-compatible API shape, so only the
client setup changed — the prompt, schema, and routing logic stayed the
same.

## Tech stack

Python, Streamlit, OpenRouter API (GPT-OSS-120B), JSON Schema

## How to run locally

1. Clone the repo and set up a virtual environment:
\`\`\`
git clone https://github.com/anshikasrivastava167/trustcheck-cod-risk-agent.git
cd trustcheck-cod-risk-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

2. Get a free API key from [openrouter.ai](https://openrouter.ai)

3. Set it as an environment variable:
\`\`\`
export OPENROUTER_API_KEY="your-key-here"
\`\`\`

4. Run the app:
\`\`\`
streamlit run app.py
\`\`\`