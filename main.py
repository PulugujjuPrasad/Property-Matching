import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

class PropertyMatchEngine:
    def __init__(self, data_path):
        print(f"🚀 Loading property data from {data_path}...")
        self.df = pd.read_excel(data_path)
        self.original_df = self.df.copy()
        self.scaler = MinMaxScaler()
        self.numeric_cols = []
        self._prepare_data()

    def _prepare_data(self):
        # Define numerical columns to normalize (Adjust these based on actual Excel headers)
        # Common real estate columns: Price, Sqft, Bedrooms, Bathrooms
        potential_numeric = ['Price', 'SquareFootage', 'Bedrooms', 'Bathrooms', 'YearBuilt']
        self.numeric_cols = [col for col in potential_numeric if col in self.df.columns]

        if not self.numeric_cols:
            print("⚠️ Warning: No standard numerical columns found. Using all numeric types.")
            self.numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()

        # Normalization
        self.df[self.numeric_cols] = self.scaler.fit_transform(self.df[self.numeric_cols])

        # Convert boolean-like columns to 0/1
        bool_cols = [col for col in self.df.columns if 'Has' in col or 'Quiet' in col or 'Garden' in col]
        for col in bool_cols:
            self.df[col] = self.df[col].map({'Yes': 1, 'No': 0, True: 1, False: 0}).fillna(0)

    def match(self, user_preferences):
        """
        user_preferences = {
            'hard_constraints': {'max_price': 500000, 'min_beds': 2},
            'weights': {'Price': 5, 'SquareFootage': 3, 'QuietNeighborhood': 4, 'HasGarden': 2}
        }
        """
        # 1. Apply Hard Constraints (Filtering)
        filtered_df = self.df.copy()
        constraints = user_preferences.get('hard_constraints', {})

        if 'max_price' in constraints:
            filtered_df = filtered_df[self.original_df['Price'] <= constraints['max_price']]
        if 'min_beds' in constraints:
            filtered_df = filtered_df[self.original_df['Bedrooms'] >= constraints['min_beds']]

        if filtered_df.empty:
            return "No properties meet your hard constraints."

        # 2. Weighted Matching
        weights = user_preferences.get('weights', {})
        # Create a weight vector matching the columns of our processed df
        weight_vector = np.array([weights.get(col, 0) for col in self.df.columns])

        # Compute weighted scores
        # Score = Sum(Feature_Value * Weight)
        feature_matrix = self.df.values
        scores = np.dot(feature_matrix, weight_vector)

        # Attach scores to original data
        result_df = self.original_df.loc[filtered_df.index].copy()
        result_df['MatchScore'] = scores

        # Normalize score to percentage (0-100%)
        max_score = np.max(scores) if len(scores) > 0 else 1
        result_df['MatchPercentage'] = (result_df['MatchScore'] / max_score) * 100

        return result_df.sort_values(by='MatchPercentage', ascending=False).head(10)

# ==========================================
# EXECUTION BLOCK
# ==========================================
if __name__ == "__main__":
    # Path to your excel file
    DATA_PATH = "Case Study 2 Data (1).xlsx"

    try:
        engine = PropertyMatchEngine(DATA_PATH)

        # Example User Profile: The "Family Dreamer"
        # Wants a quiet home with a garden, moderate budget, at least 3 beds.
        user_a = {
            'hard_constraints': {
                'max_price': 800000,
                'min_beds': 3
            },
            'weights': {
                'QuietNeighborhood': 5,
                'HasGarden': 4,
                'SquareFootage': 3,
                'Price': 2 # Lower weight means price is less critical if others are high
            }
        }

        print("\n--- Matching Results for User A (The Family Dreamer) ---")
        matches = engine.match(user_a)
        print(matches[['PropertyID', 'Price', 'Bedrooms', 'MatchPercentage']])

    except Exception as e:
        print(f"❌ Error running project: {e}")
        print("\n💡 Tip: Please ensure you have installed requirements: pip install pandas openpyxl scikit-learn")
