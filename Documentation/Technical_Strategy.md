# Technical Strategy: Matching Algorithm & Implementation

## 1. Architecture Overview
The system will follow a decoupled architecture:
**Data Layer** (SQL/NoSQL) $\rightarrow$ **Preprocessing Layer** (Python/Pandas) $\rightarrow$ **Matching Engine** (Vectorized Ops) $\rightarrow$ **API Layer** (FastAPI).

## 2. Data Science Approach

### 2.1 Feature Engineering
We will treat properties as vectors in a multi-dimensional feature space.
*   **Categorical Features:** (e.g., Neighborhood) $\rightarrow$ One-Hot Encoding.
*   **Numerical Features:** (e.g., Square Footage) $\rightarrow$ Min-Max Scaling to $[0, 1]$.
*   **Boolean Features:** (e.g., Has Pool) $\rightarrow$ $\{0, 1\}$.

### 2.2 The Algorithm: Weighted Cosine Similarity
While a weighted sum is a good start, to handle higher dimensions, we will implement **Weighted Cosine Similarity**.

**The Formula:**
$$\text{Similarity} = \frac{\sum w_i (U_i \cdot P_i)}{\sqrt{\sum w_i^2} \cdot \sqrt{\sum P_i^2}}$$
Where:
*   $U_i$: User's preference for feature $i$.
*   $P_i$: Property's value for feature $i$.
*   $w_i$: Importance weight assigned by user.

### 2.3 Handling the "Cold Start" Problem
For new users with no history:
*   **Default Profiles:** Use regional averages to suggest properties.
*   **Interactive Survey:** Force a 5-question priority survey during signup.

## 3. Technology Stack
*   **Language:** Python 3.11
*   **Data Processing:** Pandas, NumPy
*   **Vector Ops:** Scikit-learn (Cosine Similarity)
*   **API:** FastAPI / Uvicorn
*   **Database:** PostgreSQL with pgvector (for efficient vector search)
*   **Deployment:** Docker $\rightarrow$ AWS ECS

## 4. Validation Strategy
*   **Backtesting:** Use historical "Sold" data. If we knew the user's preferences, would our algorithm have ranked the house they eventually bought as #1?
*   **A/B Testing:** Compare "Traditional Filter Search" vs "AI Matching Search" and measure the Click-Through Rate (CTR) on properties.
