# Product Requirements Document (PRD)

## 1. Product Overview
The Property Matching Engine is a recommendation system that calculates the distance between a User's Preference Vector and a Property's Feature Vector to provide a ranked list of ideal homes.

## 2. User Personas
*   **The Optimizer:** Wants the absolute best value for money, carefully weighing every feature.
*   **The Dreamer:** Looking for a specific "vibe" (e.g., "mid-century modern") and is flexible on price.
*   **The Agent:** Needs to see which of their 50 clients are the best fit for a new $1M listing.

## 3. Functional Specifications

### 3.1 Preference Capture System
The system shall provide a UI for users to define:
1.  **Hard Constraints (Binary):**
    *   Price Ceiling (Max Budget)
    *   Min Bedrooms / Min Bathrooms
    *   Geographic Boundary (e.g., Zip code or Radius)
2.  **Soft Preferences (Weighted):**
    *   Users assign weights (1-5) to features such as:
        *   Proximity to Public Transit
        *   Garden/Yard size
        *   Modern Kitchen
        *   Quiet Neighborhood
        *   Parking Availability

### 3.2 Matching Algorithm Specs
*   **Step 1: Filtering.** Remove all properties that violate Hard Constraints.
*   **Step 2: Normalization.** Scale all property features to a range of [0, 1].
*   **Step 3: Weighted Sum.** Calculate the score:
    $$\text{Match Score} = \sum (\text{User Weight}_i \times \text{Property Feature}_i)$$
*   **Step 4: Ranking.** Sort by Match Score descending.

### 3.3 Match Display Requirements
*   **Match Percentage:** Convert the raw score to a percentage (e.g., "92% Match").
*   **Reasoning Engine:** Display the top 3 contributing features (e.g., "Matches your preference for: Large Backyard, Quiet Street").
*   **Thresholding:** Only show properties with a match score $> 70\%$.

## 4. User Stories
| ID | User Story | Acceptance Criteria | Priority |
| :--- | :--- | :--- | :--- |
| US.1 | As a user, I want to exclude homes with HOA fees. | System filters out all properties where `HOA == True`. | P0 |
| US.2 | As a user, I want to prioritize "Quiet Neighborhood" over "Modern Kitchen." | The weight for Quiet Neighborhood is set higher, impacting the final rank. | P1 |
| US.3 | As a user, I want to see why a home is a match. | UI displays a list of matching preferences for each result. | P2 |

## 5. UI/UX Flow
1.  **Onboarding** $\rightarrow$ 2. **Preference Weighting** $\rightarrow$ 3. **Match Calculation** $\rightarrow$ 4. **Ranked Results List** $\rightarrow$ 5. **Feedback (Like/Dislike)**.
