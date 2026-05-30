# Success Metrics & Roadmap

## 1. Key Performance Indicators (KPIs)

### 1.1 North Star Metric
**Match-to-Lead Conversion Rate:** The percentage of matched properties that result in a user requesting a viewing.

### 1.2 Secondary Metrics
*   **Precision@5:** How many of the top 5 recommendations are actually liked by the user.
*   **Average Time to Match:** The time elapsed from user profile completion to the first "Like" action.
*   **Satisafaction Score (CSAT):** User rating of the "Match Accuracy" (1-5 stars).

## 2. Implementation Roadmap

### Phase 1: Foundation (Month 1)
- [ ] Define data schema for properties and user profiles.
- [ ] Build basic filtering engine (Hard Constraints).
- [ ] Implement simple weighted sum scoring.
- [ ] Create MVP CLI tool for testing.

### Phase 2: Optimization (Month 2)
- [ ] Implement Weighted Cosine Similarity.
- [ ] Build the User Onboarding UI for preference weighting.
- [ ] Integrate PostgreSQL with pgvector for scaling.
- [ ] Implement "Reasoning Engine" (explaining the match).

### Phase 3: Intelligence & Scale (Month 3)
- [ ] Launch A/B testing against traditional search.
- [ ] Implement the feedback loop (Like/Dislike $\rightarrow$ Weight adjustment).
- [ ] Optimize query latency for $> 1M$ properties.
- [ ] Final Deployment to Production.

## 3. Risk Mitigation
| Risk | Impact | Mitigation Strategy |
| :--- | :--- | :--- |
| **Low Data Quality** | High | Implement a data validation layer that flags "incomplete" listings. |
| **User Overload** | Med | Limit the number of results to the top 10 most relevant matches. |
| **Algorithm Bias** | Med | Regularly audit recommendations to ensure diverse price points are shown. |
