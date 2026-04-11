# Prompt Iteration

## Version 1 Prompt

The initial prompt instructed the model to act as a professional writing assistant for a wellness-based consult workflow. It focused on transforming rough consult notes into a structured client follow-up draft.

Key instructions included:
- Summarize the conversation
- Reflect client goals
- Suggest reasonable next steps
- Maintain a supportive and professional tone
- Avoid medical claims or diagnoses
- Include a caution or human-review note

---

## Version 1 Performance

### Observed Behavior
The model prioritized consistency and safety over creativity, producing outputs that were dependable but occasionally lacked specificity.

### What Version 1 did well
- Produced clear, structured output with consistent sections  
- Maintained a respectful and appropriate tone  
- Avoided medical claims and stayed within safe boundaries  
- Included a useful caution / human review section  

### What still needs improvement
- Some phrasing was generic and not highly personalized  
- Output did not strongly reflect the uniqueness of the client  
- Tone, while appropriate, could feel slightly templated  
- Suggested next steps could be more tailored to the individual  

### Prompt Design Insight
The Version 1 prompt focused heavily on structure and safety, which resulted in consistent but somewhat generic outputs. This highlights the tradeoff between reliable structure and meaningful personalization in early prompt design.
---

## Planned Improvements for Version 2

- Increase personalization based on client context  
- Reduce generic phrasing and repetitive language  
- Strengthen alignment between client concerns and recommendations  
- Improve warmth and conversational tone while maintaining professionalism  

---

## Planned Improvements for Version 3

- Reduce repetition of the client’s name to improve natural flow
- Limit name usage to 1–2 times (preferably beginning and/or closing)
- Maintain personalization without sounding redundant
- Adjust tone to feel more like professional human communication (e.g., pharmacist or wellness consultant)
- Further reduce templated phrasing
- Improve variation in sentence structure
- Maintain safety, structure, and clarity from Version 2  

---

## Revision History Note

- The project setup was briefly interrupted by a computer crash while moving files into the final `Repository2` folder  
- Work resumed by reopening the repository in VS Code and revalidating the environment, files, and workflow  
- Development continued with prompt documentation and iteration tracking


## Version 2 Prompt

The Version 2 prompt builds on Version 1 by improving personalization, reducing generic phrasing, and strengthening the connection between the client’s specific context and the follow-up message.

### Full Prompt

You are a professional writing assistant for a consult-based wellness business.

Your task is to turn rough consult notes into a warm, clear, and personalized client follow-up draft.

The follow-up draft must:

1. Briefly summarize the conversation in a way that reflects the client’s specific situation  
2. Clearly restate the client’s goals using their context and preferences  
3. Suggest thoughtful and relevant next steps tailored to the individual  
4. Use a supportive, conversational, and professional tone (10–20% more personal than a standard template)  
5. Refer to the client by name when appropriate and maintain correct gender references  
6. Avoid medical claims, diagnosis, or overconfident recommendations  
7. Include a short caution when the situation may require professional guidance  
8. Include a closing sentence that invites the client to follow up using the phone number: XXX-XXX-XXXX  

Additional guidance:
- Avoid generic or overly templated phrases (e.g., “consider trying” repeated excessively)  
- Vary sentence structure to improve readability  
- Make the message feel specific to this client rather than reusable for anyone  
- Keep language simple and accessible for an older adult audience  

Client Details to Incorporate:
- Name: Sally May  
- Gender: Female  
- First-time consult client  
- Familiar with wellness products through spouse, but not personally experienced  
- Main concerns: difficulty relaxing in the evenings and inconsistent sleep routine  
- Preferences: gentle, simple, non-overwhelming approach  
- Tone preference: warm, respectful, plain-language  

Return the result in exactly these sections:

Client Follow-Up Draft  
Summary of Conversation  
Client Goals  
Suggested Next Steps  
Caution / Human Review Note  

## Version 2 Prompt

Version 2 retained the structure and safety strengths of Version 1 while improving personalization and context use.

### Key updates
- Added explicit client name handling using “Sally May”
- Added gender handling based on a provided input field rather than name-based guessing
- Instructed the model to use neutral wording if gender is missing or unclear
- Increased warmth and personalization while keeping a professional tone
- Reduced generic phrasing
- Added a callback line using XXX-XXX-XXXX

### Reason for change
Version 1 was clear and safe, but some phrasing felt generic and not fully tailored to the client. Version 2 was designed to preserve reliability while improving specificity, tone, and identity consistency.

### Version 2 Design Insight

Version 2 focused on improving personalization while preserving the structure and safety constraints of Version 1. By explicitly introducing client identity (name and gender) and adding instructions to avoid generic phrasing, the prompt aims to produce outputs that feel more tailored and less templated. The addition of a callback line also improves real-world usability by introducing a clear next action for the client.

### Version 3 Design Insight

Version 3 will focus on refining tone and naturalness. While Version 2 improved personalization, it introduced slight redundancy through repeated name usage. The next iteration aims to balance personalization with professional communication norms, making outputs feel more natural and human while preserving clarity and safety.

## Version 3 Prompt Improvements

- Adjust tone to reflect a "gentle pharmacist" style: professional, calm, knowledgeable, and reassuring without sounding overly clinical
- Reduce repetition of the client’s name (limit to 1–2 uses maximum, preferably opening and/or closing)
- Maintain personalization while improving natural conversational flow
- Further reduce templated or repetitive phrasing
- Improve sentence variation and readability
- Strengthen safety awareness by identifying higher-risk situations (e.g., fall risk, severe symptoms)
- Introduce escalation language when appropriate (e.g., recommending professional review)

### Version 3 Design Insight

Version 3 focuses on refining natural communication quality while maintaining structure and safety. The goal is to balance personalization with professional tone, similar to how a pharmacist or experienced wellness consultant would communicate. This iteration also introduces clearer escalation pathways for higher-risk scenarios, ensuring the system remains safe and responsible in more complex cases.

## Version 3 Planned Improvements

- Reduce repetition of the client’s name to 1–2 uses maximum
- Refine tone to feel like a gentle pharmacist: calm, professional, reassuring, and knowledgeable
- Preserve personalization without sounding templated
- Strengthen safety language for higher-risk scenarios such as fall risk or concerning functional impairment
- Add a human-review message indicating that a highly trained professional may review the case when appropriate
- Maintain structure, safety, and clarity from Version 2

### Version 3 Design Insight

Version 3 will focus on improving natural communication quality while preserving the strengths of Version 2. The goal is to make the output sound more like a skilled human professional, while also improving escalation language for cases that may require additional review.

## Version 3 Prompt

### Key Improvements
- Reduced repetition of the client’s name (limited to 1–2 uses)
- Introduced “gentle pharmacist” tone (professional, calm, reassuring)
- Improved natural conversational flow
- Reduced templated phrasing
- Strengthened sentence variation and readability
- Added identification of higher-risk concerns (e.g., fall risk)
- Introduced human-review escalation language
- Maintained structure and safety from Version 2

### Version 3 Design Insight

Version 3 focuses on improving natural communication quality while preserving structure and safety. The goal is to make outputs feel more like a skilled human professional, similar to a pharmacist or experienced wellness consultant. This iteration also introduces clearer escalation pathways for higher-risk scenarios and reinforces a human-in-the-loop safety approach.

### Additional Version 3 Insight

Version 3 demonstrated that improving tone and naturalness significantly enhances usability in client-facing scenarios. However, it also highlighted that communication style should adapt based on the intended audience. Future iterations could introduce dynamic tone control depending on whether the output is intended for clients, internal staff, or documentation.

## Final Notes
Version 3 is implemented and ready for evaluation. The final implementation is documented below.

### Final Prompt Used (Version 3)

```text
You are a professional writing assistant for a consult-based wellness business.

Your task is to turn rough consult notes into a warm, clear, and personalized client follow-up draft.

Follow these rules in order:

1. Use the client details provided in the consult notes.
2. Refer to the client by name naturally, but limit name usage to 1–2 times maximum.
3. Use the gender provided in the consult notes for pronouns and references.
4. If gender is missing or unclear, do not guess. Use the client’s name or neutral wording instead.
5. Briefly summarize the conversation in a way that reflects the client’s specific situation.
6. Restate the client’s goals using their context and preferences.
7. Suggest thoughtful and relevant next steps tailored to the individual.
8. Use a tone similar to a gentle pharmacist: calm, professional, knowledgeable, and reassuring without being overly clinical.
9. Avoid medical claims, diagnosis, or overconfident recommendations.
10. Identify potential higher-risk concerns (e.g., fall risk, significant sleep disruption, or functional impact) when present.
11. When appropriate, include language indicating that a highly trained professional may review the situation to ensure safe and personalized guidance.
12. Include a short caution when professional guidance may be appropriate.
13. End with a warm closing sentence inviting the client to call back at XXX-XXX-XXXX.

Additional guidance:
- Avoid generic or overly templated phrases.
- Vary sentence structure to improve readability.
- Keep the message natural and human-like, not repetitive.
- Maintain structure, clarity, and safety from previous versions.

Return the result in exactly these sections:

Client Follow-Up Draft
Summary of Conversation
Client Goals
Suggested Next Steps
Caution / Human Review Note
```

