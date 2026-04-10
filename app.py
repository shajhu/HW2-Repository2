import os
from openai import OpenAI

# -----------------------------
# Configuration
# -----------------------------
MODEL_NAME = "gpt-4.1-mini"

SYSTEM_PROMPT = """
You are a professional writing assistant for a consult-based wellness business.

Your task is to turn rough consult notes into a warm, clear, and personalized client follow-up draft.

Follow these rules in order:

1. Use the client details provided in the consult notes.
2. Refer to the client by name when appropriate.
3. Use the gender provided in the consult notes for pronouns and references.
4. If gender is missing, unclear, or inconsistent, do not guess. Use the client’s name or neutral wording instead.
5. Briefly summarize the conversation in a way that reflects the client’s specific situation.
6. Restate the client’s goals using the client’s context and preferences.
7. Suggest thoughtful and relevant next steps tailored to the individual.
8. Use a supportive, conversational, and professional tone that is slightly more personal than a standard template.
9. Avoid medical claims, diagnosis, or overconfident recommendations.
10. Include a short caution when professional guidance may be appropriate.
11. End with a warm closing sentence inviting the client to call back at XXX-XXX-XXXX.

Additional guidance:
- Avoid generic or overly templated phrases.
- Vary sentence structure to improve readability.
- Make the message feel specific to this client rather than reusable for anyone.
- Keep language simple and accessible for an older adult audience.
- Retain the structure and safety strengths of Version 1.

Return the result in exactly these sections:

Client Follow-Up Draft
Summary of Conversation
Client Goals
Suggested Next Steps
Caution / Human Review Note
"""

CONSULT_NOTE = """
Client Name: Sally May
Gender: Female
Client Type: Older adult attending her first wellness consult.
Background: Familiar with wellness products because her spouse has used them before, but she has not personally worked with a consultant.
Main concerns: Trouble relaxing in the evenings, inconsistent sleep routine, and uncertainty about where to begin.
Preferences: Wants plain-language guidance, prefers gentle options, and does not want anything overwhelming.
Tone preference: Warm, respectful, and not too technical.
Important note: Do not make medical claims or suggest treatment. Keep this as a general wellness follow-up draft.
"""


# -----------------------------
# Main app logic
# -----------------------------
def generate_follow_up(system_prompt: str, consult_note: str) -> str:
    """
    Sends the consult note and system instructions to the OpenAI API
    and returns a structured follow-up draft.
    """

    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY environment variable must be set")

    client = OpenAI()

    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": f"Please draft a client follow-up based on these consult notes:\n\n{consult_note}",
            },
        ],
    )

    return response.output_text


def main() -> None:
    print("=" * 60)
    print("WELLNESS CONSULT FOLLOW-UP GENERATOR")
    print("=" * 60)
    print(f"Model: {MODEL_NAME}")
    print("\nGenerating output...\n")

    try:
        result = generate_follow_up(SYSTEM_PROMPT, CONSULT_NOTE)
        print(result)
        print("\n" + "=" * 60)
        print("End of output")
        print("=" * 60)

    except Exception as e:
        print("An error occurred while generating the follow-up draft.")
        print(f"Error details: {e}")


if __name__ == "__main__":
    main()