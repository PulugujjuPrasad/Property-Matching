# Property Matching Engine: AI-Driven Real Estate Recommendation System

## Executive Summary
The Property Matching Engine is a sophisticated recommendation system designed to move real estate search from a rigid "filter-based" model to a dynamic "preference-based" matching paradigm. By leveraging weighted vector similarity and hard-constraint filtering, the system aligns property features with nuanced user lifestyle preferences to increase lead conversion and reduce search fatigue.

---

## 🌐 Visual Interactive Portal (UI/UX)
To provide a professional client-facing experience, this project includes a **Streamlit Interactive Dashboard**. 

### How to launch the Visual Portal:
1. **Install requirements:** `pip install -r requirements.txt`
2. **Run the UI:** 
   ```bash
   streamlit run app.py
   ```
3. **Experience:** The portal allows clients to upload data, adjust their a-priori preferences using sliders, and see their top-matching properties visually ranked with real-time percentage scores.

---

## 📋 Project Documentation
The core of this project's product strategy is detailed in the `/Documentation` directory:

*   **[Business Requirements Document (BRD)](Documentation/BRD.md)**
*   **[Product Requirements Document (PRD)](Documentation/PRD.md)**
*   **[Technical Strategy](Documentation/Technical_Strategy.md)**
*   **[Project Charter](Documentation/Project_Charter.md)**
*   **[Success Metrics & Roadmap](Documentation/Success_Metrics_Roadmap.md)**

---

## ⚙️ Engineering Approach

### The Solution: Two-Stage Pipeline
1.  **Hard Constraint Filtering:** Ensures results are financially and functionally viable (Budget, Size).
2.  **Weighted Vector Scoring:** Calculates a match score using a weighted dot product of user preferences and property features.
    $$\text{Match Score} = \sum (\text{Normalized Property Feature}_i \times \text{User Preference Weight}_i)$$

---

## 🛠️ Implementation Details

### Setup and Installation
```bash
git clone https://github.com/PulugujjuPrasad/Property-Matching.git
cd "Property Matching with User Preferences"
pip install -r requirements.txt
```

### Running the Project
- **Interactive UI (Recommended for Clients):** `streamlit run app.py`
- **CLI Backend (For Developers):** `python main.py`

---

## 📈 Key Performance Indicators (KPIs)
- **Match-to-Lead Conversion:** Increase in viewing requests.
- **Precision@K:** Accuracy of top-K recommendations.
- **User Retention:** Increase in MAU driven by discovery.
