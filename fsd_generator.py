from langchain_openai import ChatOpenAI
import json, os

api_key=os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key = api_key
)

SYSTEM_PROMPT = """
You are an SAP ABAP functional analyst.
Given ABAP code, generate a Functional Specification Document (FSD).
Return STRICT JSON with fields:
title, module, objective, inputs, outputs, business_rules, db_tables, error_handling.
"""

def generate_fsd(abap_code: str) -> dict:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": abap_code}
    ]
    raw = llm.invoke(messages).content
    try:
        return json.loads(raw)
    except Exception:
        return {"error": "Invalid JSON", "raw": raw}
