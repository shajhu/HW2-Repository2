# Project Plan

## 1. Project Title

Intake-to-Note Assistant for Pharmacist Review

---

## 2. Target User, Workflow, and Business Value

The target user is a pharmacist reviewing client intake information in a consult-based wellness workflow. The recurring task being improved is the process of organizing intake responses and converting them into a structured review note and draft follow-up communication.

The workflow begins when a completed intake form is submitted and ends when the pharmacist receives:
- a structured review note,
- a draft client-facing follow-up,
- and any flagged items requiring human review.

Improving this workflow matters because pharmacists and similar professionals spend significant time interpreting intake data and documenting consultations. Automating the first-pass organization and drafting process can reduce documentation time, improve consistency, and help ensure that important safety signals are not missed.

---

## 3. Problem Statement and GenAI Fit

This system converts intake form responses into a structured pharmacist review note and a draft client-facing follow-up, while identifying cases that require additional human review.

The key task is summarization, organization, and draft generation from semi-structured inputs. This is a strong fit for generative AI because intake data is often scattered, language-heavy, and inconsistent in format.

A simpler non-GenAI tool (such as a template or rules-based system) would not be sufficient because it cannot adapt to variation in inputs, synthesize context effectively, or generate natural, professional language tailored to the individual case.

---

## 4. Planned System Design and Baseline

The system will be implemented as a small Streamlit application.

The underlying AI call will use a moderate-capability model with explicit output sections to balance response quality, latency, and operational cost.

### Workflow

1. User inputs intake data (via form or pasted text)
2. System processes the input using a structured prompt
3. System outputs:
   - structured pharmacist review note
   - draft client-facing follow-up
   - flagged concerns (if present)
   - review status (standard review vs mandatory human review)

The system does not make final clinical decisions and is intended only to support documentation and initial draft generation.

---

### Course Concepts

**1. Model selection and provider tradeoffs**  
The prototype will target a model that balances structured output quality with cost and latency, such as gpt-4.1-mini. The design emphasizes prompt structure and explicit sections to minimize variability and maximize reliability.

**2. Anatomy of an LLM call**  
The system will use a clear system prompt with output constraints and structured sections. Temperature will be kept low to improve consistency, and the user prompt will include the intake text plus explicit instructions for summary, follow-up, and flagged concerns.

**3. Context engineering**  
Input formatting is important for stable results. The plan will use explicit section headers, clear intake formatting, and optional few-shot examples to help the model interpret varied intake styles. Conversation history is not a core requirement because each intake is processed as a standalone case.

**4. Reasoning models / chain-of-thought prompting**  
The prompt will ask the model to identify potential safety signals and summarize intake details before generating the final draft. This encourages the model to reason through the input and surface relevant concerns rather than producing a shallow response.

**5. Evaluation design**  
A test set will be created with multiple representative intake cases. Outputs will be evaluated using a rubric covering structure, tone, personalization, and safety. The structured prototype will be compared to a simpler prompt-only baseline.

**6. Governance and deployment controls**  
The system will include explicit escalation rules. When higher-risk signals appear (e.g., fall risk, functional impairment), the output will require pharmacist review rather than being treated as a complete recommendation.

The project scope remains narrow and does not include tool use, agent loops, RAG, multi-agent orchestration, or an MCP layer, because the goal is to build a focused, runnable prototype with reliable output and clear evaluation.

---

### Baseline

The baseline will be a simple prompt-only approach using minimal structure.

This baseline reflects a realistic starting point and allows comparison against the structured system to evaluate improvements in consistency, tone, and safety.

---

### App Description

The app will present:
- an intake input interface
- a submission button
- an output panel displaying:
  - structured note
  - draft follow-up
  - flagged concerns
  - review status

The interface will be simple to ensure usability and allow for live demonstration.

---

## 5. Evaluation Plan

Success is defined as producing outputs that:
- are clearly structured,
- reflect intake details accurately,
- maintain a professional and appropriate tone,
- avoid unsafe or overconfident language,
- correctly flag cases requiring human review.

Evaluation criteria will include:
- structure consistency
- personalization accuracy
- tone quality
- safety and escalation behavior
- comparison against baseline output

The test set will include at least 5–6 cases covering normal, edge, and higher-risk scenarios.

Outputs will be compared side-by-side with baseline outputs and assessed using a defined rubric.

---

## 6. Example Inputs and Failure Cases

### Example Inputs

1. **Older adult with sleep concerns and preference for gentle solutions**  
   Intake text: "Client is 68-year-old female, reports difficulty falling asleep due to evening anxiety. Prefers natural, gentle remedies over medications. Has tried chamomile tea with some success. No major health issues reported."

2. **Male client with stress and routine challenges**  
   Intake text: "Client is 45-year-old male, experiencing high work stress leading to irregular sleep and poor eating habits. Interested in stress management techniques and building better daily routines. Open to supplements but prefers evidence-based advice."

3. **Intake with missing demographic information**  
   Intake text: "Client reports chronic fatigue and low energy levels. Age and gender not specified in form. Interested in general wellness strategies for better sleep and energy. No specific preferences mentioned."

4. **Younger client with higher familiarity and expectations**  
   Intake text: "Client is 28-year-old, well-informed about wellness products. Seeks practical, science-backed recommendations for managing stress and improving focus. Prefers direct, actionable advice without overly basic explanations."

5. **Case including fall risk or functional concerns**  
   Intake text: "Client is 72-year-old female, reports recent dizziness and balance issues that have led to a near-fall. Also mentions joint pain affecting mobility. Seeking guidance on safe exercise and fall prevention strategies."

6. **Sparse or incomplete intake**  
   Intake text: "Client wants help with sleep. No other details provided."

---

### Failure Cases

1. Cases with complex medical or medication-related risks that exceed the scope of a wellness consult (e.g., active medication interactions or undiagnosed conditions requiring clinical review)
2. Sparse or contradictory inputs that may lead to generic or weak outputs (e.g., minimal details making it hard to personalize or identify risks)
3. Inputs with potential safety signals that are not clearly flagged (e.g., subtle mentions of mental health concerns or substance use that need escalation)

---

## 7. Risks and Governance

The system may fail by:
- producing overly confident language,
- missing subtle risk indicators,
- generating outputs that appear correct but are incomplete.

The system should not be trusted for:
- diagnosis
- treatment decisions
- high-risk or unclear cases without review

Governance controls include:
- mandatory human review for flagged cases
- avoidance of diagnostic language
- clear positioning as a draft-generation tool
- use of synthetic data only for development

---

## 8. Plan for the Week 6 Check-in

By Week 6, the following will be completed:

- a working Streamlit app with intake input and generated outputs
- a first version of the structured prompt
- initial evaluation cases
- baseline vs structured output comparison on at least one case

This will allow demonstration of:
- core functionality
- early evaluation
- initial improvements over baseline

---

## 9. Pair Request

Not applicable.

---

## Summary of Changes for Final Project Generation

This final project builds on the previous wellness consult follow-up generator repository by maintaining the same narrow workflow focus and expanding it to pharmacist intake review. Key changes include:
- shifting the user to a pharmacist reviewing intake information,
- keeping the workflow narrow and one-document centered (structured review note + follow-up),
- adding explicit governance and human-review controls for higher-risk cases,
- defining a simple Streamlit prototype as the runnable application,
- strengthening evaluation design with a rubric and representative test cases.

The current plan is intended to be the foundation for the final project, with the previous repository serving as the starting point for prompt and evaluation iteration.

Ensure:
- Markdown headers render correctly
- Spacing between sections is consistent
- No broken formatting
- File is clean and readable for GitHub
