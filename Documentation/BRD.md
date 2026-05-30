# Business Requirements Document (BRD)

## 1. Executive Summary
The business requires an automated intelligence layer that can match users to properties based on a complex set of preferences. The objective is to increase user engagement and reduce the churn rate seen in traditional search platforms.

## 2. Business Goals
| ID | Goal | Description | Priority |
| :--- | :--- | :--- | :--- |
| BG.1 | Conversion Lift | Increase the number of users who request a viewing from 10% to 25%. | P0 |
| BG.2 | User Retention | Increase Monthly Active Users (MAU) by providing a "Discovery" feed. | P1 |
| BG.3 | Agent Efficiency | Reduce the time agents spend manually qualifying leads. | P1 |

## 3. Functional Business Requirements
### 3.1 User Profiling
*   **Requirement:** The system must be able to capture and store a nuanced user profile including budget, location, size, and subjective preferences.
*   **Business Value:** Enables the engine to differentiate between a "must-have" and a "nice-to-have."

### 3.2 Matching Logic
*   **Requirement:** The system must rank properties by a "Match Score" rather than just listing them.
*   **Business Value:** Creates a "Concierge" experience for the user, increasing trust in the platform.

### 3.3 Feedback Loop
*   **Requirement:** Users must be able to "Like" or "Dislike" suggested properties.
*   **Business Value:** Provides the ground-truth data necessary to tune the AI model for better accuracy.

## 4. Non-Functional Requirements
*   **Performance:** Match results must be returned in $< 2$ seconds.
*   **Scalability:** The system must support up to 100,000 concurrent users and 1 million listings.
*   **Availability:** 99.9% uptime for the matching API.

## 5. Constraints & Assumptions
*   **Data Quality:** It is assumed that property data is cleaned and standardized via a central API.
*   **User Input:** Assumes users will complete a basic onboarding survey.
