# Case Study: AI-Driven Property Matching Engine
**Role:** Lead AI Product Manager  
**Domain:** PropTech / Real Estate Technology  
**Challenge:** Improving Lead Conversion through Personalized Matching

## 📌 The Problem Space
Traditional real estate search is built on "Hard Filters." This creates a binary experience: a property either matches 100% of the filters or it is hidden. In reality, home buying is a trade-off. A user might be willing to accept a house that is $10k over budget if it has the "Quiet Neighborhood" and "Large Garden" they desperately want.

**The Gap:** There was no system to quantify "lifestyle compatibility" in real-time.

## 🎯 The AI Product Strategy
As the AI PM, my goal was to shift the paradigm from **Search $\rightarrow$ Discovery**. 

### 1. User Centricity & Personas
I identified three core personas to drive the requirements:
- **The Budget Optimizer:** Prioritizes cost and square footage.
- **The Lifestyle Dreamer:** Prioritizes amenities and neighborhood vibe.
- **The High-Net-Worth Investor:** Prioritizes exclusivity and architecture.

### 2. Algorithmic Decisioning
I steered the technical implementation away from simple filtering and toward **Vector Space Modeling**. 
- **Decision:** Implement a two-stage pipeline (Hard Filtering $\rightarrow$ Weighted Scoring).
- **Rationale:** This ensures financial viability while allowing the AI to "rank" the most compatible lifestyle matches, mirroring how a human luxury agent works.

### 3. Defining Success (The North Star)
I defined the success of this product not by "code accuracy," but by **Business Impact**:
- **North Star Metric:** Match-to-Lead Conversion Rate.
- **Guardrail Metric:** Search Latency (Ensuring the vector calculation doesn't slow down the user experience).

## 🛠️ Execution & Delivery
- **Requirement Elicitation:** Authored a comprehensive BRD and PRD to align stakeholders.
- **Technical Oversight:** Managed the implementation of a Weighted Cosine Similarity engine.
- **UX Validation:** Designed and launched an interactive Streamlit portal to allow stakeholders to "feel" the matching logic through a visual UI.

## 📈 Results & Reflections
The resulting engine transforms a static list into a curated recommendation feed. 
**Key Takeaway:** By quantifying subjective preferences, we can reduce "search fatigue" and increase the probability of a user finding their ideal home, directly impacting the bottom line of the real estate agency.
