import os
from openai import OpenAI

# -----------------------------
# Configuration
# -----------------------------
MODEL_NAME = "gpt-4.1-mini"

SYSTEM_PROMPT = """
You are a professional writing assistant for a consult-based wellness business.

Your task is to turn rough consult notes into a warm, clear, plain-language client follow-up draft.

The follow-up draft must:
1. Briefly summarize the conversation
2. Reflect the client's goals or concerns
3. Suggest reasonable next steps
4. Use a supportive, professional tone
5. Avoid medical claims, diagnosis, or overconfident recommendations
6. Add a short caution when the situation may require professional guidance

Write in a way that is appropriate for older adults and easy to understand.
Keep the tone respectful, calm, and concise.

Return the result in exactly these sections:

Client Follow-Up Draft
Summary of Conversation
Client Goals
Suggested Next Steps
Caution / Human Review Note
"""

CONSULT_NOTE = """
Client: Older adult woman attending her first wellness consult.
Background: Familiar with wellness products because her spouse has used them before, but she has not personally worked with a consultant.
Main concerns: Trouble relaxing in the evenings, inconsistent sleep routine, and uncertainty about where to begin.
Preferences: Wants plain-language guidance, prefers gentle options, and does not want anything overwhelming.
Tone preference: Warm, respectful, not too technical.
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

    # Ensure API key exists
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY environment variable must be set")

    client = OpenAI()

    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"Please draft a client follow-up based on these consult notes:\n\n{consult_note}"
            }
        ]
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
