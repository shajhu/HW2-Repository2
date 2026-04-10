# HW2 – Generative AI Workflow Prototype

## Overview
This project implements a simple generative AI workflow using the OpenAI API. The system converts rough consult notes into a structured, plain-language client follow-up draft within a wellness-focused business context.

## Business Workflow
The selected workflow is a **consult note to client follow-up generator**. This reflects a real-world task where consultants translate unstructured notes into clear, supportive, and consistent communication for clients.

## Input and Output

- **Input:** Unstructured consult notes  
- **Output:** Structured follow-up draft with:
  - Client Follow-Up Draft  
  - Summary of Conversation  
  - Client Goals  
  - Suggested Next Steps  
  - Caution / Human Review Note  

## Why This Workflow Matters
Client follow-up communication is repetitive but important for maintaining consistency, clarity, and trust. Automating a first draft reduces time spent on low-value tasks while maintaining a clear human-review boundary for safety and personalization in client-facing communication.

---

## Setup Instructions

```bash
python -m venv .venv
# Command Prompt
.\.venv\Scripts\activate
pip install openai
setx OPENAI_API_KEY "your_api_key_here"
```

After setting the API key, close and reopen your terminal, then run:

```bash
python app.py
```

---

## API Key Setup and Environment Configuration

The OpenAI API key is stored securely using an environment variable rather than being hardcoded into the application:

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

After running this command, the terminal must be restarted for the variable to take effect. The application retrieves the key using:

```python
os.getenv("OPENAI_API_KEY")
```

### Reflection (Version 1)

* The API key setup process was straightforward once understood
* The primary learning point was that environment variables require restarting the terminal
* This approach improves security and keeps sensitive information out of the codebase

---

## Version 1 Summary

### What was built
- A working Python application (`app.py`)
- OpenAI API integration using a structured prompt
- Consistent, section-based output

### Observations
- Output is clear and well-structured
- Tone is appropriate for the intended audience
- Some phrasing is generic and could be more personalized

---

## Revision History

- Setup:
  - Created project structure and virtual environment
  - Installed OpenAI package and configured API access

- Version 1:
  - Built initial LLM workflow prototype
  - Verified successful output generation

- Version 2:
  - Improved personalization and reduced generic phrasing in generated outputs
  - Added explicit client name usage (“Sally May”) to test identity consistency
  - Introduced structured gender handling using a dedicated input field
  - Instructed the model not to guess gender when input is missing or unclear
  - Strengthened tone to be more conversational and client-specific while remaining professional
  - Added callback language inviting the client to follow up at XXX-XXX-XXXX
  - Refined prompt structure to follow a clearer chain of command (identity → context → recommendations → tone → safety → closing)
  - Added evaluation set coverage to capture a missed module/test requirement
  - Created a 5-case evaluation set covering normal, edge, and high-risk scenarios for repeatable, fair testing
  - Validated output using evaluation set and confirmed improvements in personalization, tone, and structure
  - Identified opportunity to improve natural language flow by reducing name repetition
  - Identified need to improve tone naturalness (reduce name repetition)
  - Identified opportunity to introduce more nuanced client scenarios (younger / knowledgeable clients)
  - Recognized need for clearer escalation language in higher-risk situations
  - Adjusted prompts to provide a master prompt resolving disputes between logic
  - Validated Version 2 output and confirmed stronger personalization, improved tone, and consistent structure
  - Identified excessive repetition of the client name as a remaining natural-language issue
  - Identified the need for a gentler “pharmacist-like” professional tone in the next iteration
  - Expanded evaluation planning to include a younger, more knowledgeable client and stronger fall-risk / human-review escalation

---

## Status

Version 2 has been successfully evaluated and documented. Version 3 will focus on reducing name repetition, improving tone naturalness, expanding scenario coverage, and strengthening higher-risk escalation language.

