# Property Matching Engine: AI-Driven Real Estate Recommendation System

## Executive Summary
The Property Matching Engine is a sophisticated recommendation system designed to move real estate search from a rigid "filter-based" model to a dynamic "preference-based" matching paradigm. By leveraging weighted vector similarity and hard-constraint filtering, the system aligns property features with nuanced user lifestyle preferences to increase lead conversion and reduce search fatigue.

This project demonstrates a full-lifecycle AI Product Engineering approach: from business requirement elicitation (BRD) and product specification (PRD) to algorithmic design and implementation.

---

## 📋 Project Documentation
The core of this project's product strategy is detailed in the `/Documentation` directory. These documents outline the transition from business needs to technical execution:

*   **[Business Requirements Document (BRD)](Documentation/BRD.md):** Defines business goals, high-level requirements, and the economic value of the matching engine.
*   **[Product Requirements Document (PRD)](Documentation/PRD.md):** Detailed functional specifications, user personas, and the "Hard vs. Soft" constraint logic.
*   **[Technical Strategy](Documentation/Technical_Strategy.md):** In-depth explanation of the Weighted Cosine Similarity algorithm, feature engineering, and the proposed technology stack.
*   **[Project Charter](Documentation/Project_Charter.md):** The overarching vision, scope, and stakeholder map.
*   **[Success Metrics & Roadmap](Documentation/Success_Metrics_Roadmap.md):** KPIs for measuring accuracy and a three-phase execution timeline.

---

## ⚙️ Engineering Approach

### The Problem
Traditional search engines use binary filters (e.g., "Price < $500k"). This creates a "cliff effect" where a property at $500,001 is hidden, even if it is a 100% match for all other preferences.

### The Solution: Two-Stage Pipeline
To solve this, the engine implements a two-stage matching pipeline:

1.  **Hard Constraint Filtering:** 
    The system first applies mandatory binary filters (Budget, Minimum Bedrooms) to ensure the results are financially and functionally viable.
    
2.  **Weighted Vector Scoring:** 
    Remaining properties are treated as vectors in a multi-dimensional feature space. The system calculates a match score using a weighted dot product of the user's preference vector and the property's feature vector.
    
    **Mathematical Logic:**
    $\text{Match Score} = \sum (\text{Normalized Property Feature}_i \times \text{User Preference Weight}_i)$

---

## 🛠️ Implementation Details

### Setup and Installation

**Prerequisites:**
- Python 3.10+
- `pandas`, `scikit-learn`, `openpyxl`

**Installation:**
```bash
# Clone the repository
git clone https://github.com/PulugujjuPrasad/Property-Matching.git
cd "Property Matching with User Preferences"

# Install dependencies
pip install -r requirements.txt
```

**Running the Engine:**
```bash
python main.py
```

### Core Components
- `main.py`: Contains the `PropertyMatchEngine` class, handling data normalization, constraint filtering, and ranking logic.
- `Case Study 2 Data (1).xlsx`: The dataset containing property features used for matching.

---

## 📈 Key Performance Indicators (KPIs)
The success of this engine is measured by:
- **Match-to-Lead Conversion:** Increase in the percentage of suggested properties that result in a viewing request.
- **Precision@K:** The accuracy of the top-K recommended properties.
- **User Retention:** The increase in MAU driven by the discovery-based matching experience.
