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

- QC Updates:
  - Removed hardcoded API key
  - Implemented environment variable usage
  - Improved formatting and reproducibility

- Environment Event:
  - Computer crash occurred during file transfer to Repository2
  - Project was reopened and revalidated before continuing

---

## Status

Version 2 is prepared and ready for testing locally. Future iterations will focus on improving tone consistency, edge-case handling, and personalization across multiple client scenarios.

