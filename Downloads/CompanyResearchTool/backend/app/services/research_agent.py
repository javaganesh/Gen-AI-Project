import json

from app.services.search_service import search_company
from app.services.ollama_service import ask_llm


def create_prompt(company_name: str, search_data: dict) -> str:

    return f"""
You are a professional company research analyst.

Research Company:
{company_name}

Search Results:
{json.dumps(search_data)}

IMPORTANT RULES:

1. Return ONLY valid JSON.
2. Do NOT use markdown.
3. Do NOT use triple backticks.
4. Do NOT explain anything.
5. Do NOT add text before or after JSON.
6. If data is unavailable use null.
7. News should contain 3 to 4 items.
8. Risks should contain 2 to 3 items.

Required JSON Format:

{{
    "overview": "string",

    "key_people": [
        {{
            "name": "string",
            "title": "string"
        }}
    ],

    "news": [
        "string"
    ],

    "financials": {{
        "revenue": null,
        "employee_count": null,
        "market_cap": null,
        "yoy_growth": null
    }},

    "risks": [
        "string"
    ]
}}

Return ONLY JSON.
"""


def clean_llm_response(response: str):

    response = response.strip()

    if response.startswith("```json"):
        response = response.replace("```json", "")

    if response.startswith("```"):
        response = response.replace("```", "")

    if response.endswith("```"):
        response = response.replace("```", "")

    return response.strip()


def research_company(company_name: str):

    try:

        search_data = search_company(company_name)

        prompt = create_prompt(
            company_name,
            search_data
        )

        llm_response = ask_llm(prompt)
        print("\n========== LLM RESPONSE ==========\n")
        print(llm_response)
        print("\n========== END RESPONSE ==========\n")

        cleaned_response = clean_llm_response(
            llm_response
        )

        report_json = json.loads(
            cleaned_response
        )

        return report_json

    except Exception as e:

        print(
            f"Research Agent Error: {str(e)}"
        )

        return {
            "overview": f"Unable to research {company_name}",

            "key_people": [],

            "news": [
                "No news available"
            ],

            "financials": {
                "revenue": None,
                "employee_count": None,
                "market_cap": None,
                "yoy_growth": None
            },

            "risks": [
                "No risk information available"
            ]
        }