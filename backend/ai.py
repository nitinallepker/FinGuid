import os

import google.generativeai as genai
from dotenv import load_dotenv

from workflow import FinancialWorkflow
from prompts import SYSTEM_PROMPT

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

workflow = FinancialWorkflow()


def split_response(text):

    answer = text
    question = ""

    if "QUESTION:" in text:

        parts = text.split("QUESTION:")

        answer = (
            parts[0]
            .replace("ANSWER:", "")
            .strip()
        )

        question = parts[1].strip()

        if question.upper() == "NONE":
            question = ""

    return answer, question


def generate_financial_analysis(data):

    prompt = f"""
{SYSTEM_PROMPT}

USER PROFILE

Goal:
{data.get('goal')}

Target Amount:
{data.get('target_amount')}

Timeline:
{data.get('timeline')}

Financial Position:
{data.get('financial_position')}

Your task:

1. Analyze the user's situation.
2. Explain whether the goal appears realistic.
3. Suggest practical approaches.
4. Explain advantages and disadvantages.
5. Give specific examples where useful.
6. Avoid generic advice.
7. Ask ONLY ONE follow-up question if genuinely needed.
8. If enough information exists, return QUESTION: NONE.

Return exactly:

ANSWER:
<analysis>

QUESTION:
<one follow-up question or NONE>
"""

    response = model.generate_content(prompt)

    return response.text


def process_message(message):

    if workflow.stage < 5:

        result = workflow.next_step(message)

        if result == "PROFILE_COMPLETE":

            analysis = generate_financial_analysis(
                workflow.data
            )

            answer, question = split_response(
                analysis
            )

            return {
                "answer": answer,
                "question": question
            }

        return {
            "answer": result,
            "question": ""
        }

    response = model.generate_content(
        f"""
{SYSTEM_PROMPT}

USER PROFILE

Goal:
{workflow.data.get('goal')}

Target Amount:
{workflow.data.get('target_amount')}

Timeline:
{workflow.data.get('timeline')}

Financial Position:
{workflow.data.get('financial_position')}

USER MESSAGE

{message}

Rules:

- Continue the discussion naturally.
- Do not restart the onboarding process.
- Do not ask multiple questions.
- Ask at most ONE follow-up question.
- If no further information is needed, return QUESTION: NONE.
- Be specific and practical.

Return exactly:

ANSWER:
<response>

QUESTION:
<one follow-up question or NONE>
"""
    )

    answer, question = split_response(
        response.text
    )

    return {
        "answer": answer,
        "question": question
    }