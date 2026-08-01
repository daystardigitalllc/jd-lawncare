---
name: client-brand
description: Custom skill guiding the AI on how to handle brand colors, logo assets, copy tone of voice, and prevent hallucinating company facts.
---

# Brand Integrity & Client Context Skill

## 1. Overview
This skill governs how you process client assets, adhere to brand guidelines, and maintain absolute factual accuracy when writing copy and developing sections. 

---

## 2. Using Client Information & Context
*   **Factual Accuracy:** Never invent, assume, or hallucinate business details. This includes phone numbers, physical addresses, licensing numbers, specific warranties, or team member names.
*   **Defaulting to Template Data:** The file [client-info/business-info.md](file:///./client-info/business-info.md) is your strict database. If a detail is not defined there, mark it as `[MISSING_FACT: details_requested]` in your copy and request the user to provide it.
*   **Business Voice:** Determine the client's tone based on their industry:
    *   *Service Businesses (HVAC, Roofing, Plumbers):* Grounded, trustworthy, authoritative, responsive, and direct.
    *   *Professional Services (Lawyers, Clinics):* Empathetic, expert, clear, reassuring, and highly compliant.
    *   *Aesthetic Brands (Landscapers, Designers):* Creative, modern, details-focused, and premium.

---

## 3. Adhering to Brand Guidelines
*   **Color Hex Tokens:** Read the color tokens in [strategy/design-direction.md](file:///./strategy/design-direction.md). Do not use random colors or default browser colors. Stick strictly to the primary, secondary, and background variables defined in the plan.
*   **Typography Hierarchy:** Pair headers and body copy according to the design direction document (e.g., serif header + sans-serif body). Never introduce a third font family without approval.
*   **Visual Assets:** Use logo files from `assets/logos/` and images from `assets/images/`.

---

## 4. Discovery Protocol for Missing Information
If you encounter missing brand guidelines or business information during any stage:
1.  **Stop writing copy or styling layouts.**
2.  List the specific missing fields clearly (e.g., "Need hex code for Primary Accent Color", "Need licensing numbers for Florida registration").
3.  Ask the user to fill them in [client-info/business-info.md](file:///./client-info/business-info.md) before you resume.
