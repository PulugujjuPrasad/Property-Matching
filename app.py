import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import plotly.express as px

# Set Page Config
st.set_page_config(page_title="AI Property Matcher", layout="wide", page_icon="🏠")

class PropertyMatchEngine:
    def __init__(self, df):
        self.original_df = df.copy()
        self.df = df.copy()
        self.scaler = MinMaxScaler()
        self._prepare_data()

    def _prepare_data(self):
        # Identify numeric columns for normalization
        potential_numeric = ['Price', 'SquareFootage', 'Bedrooms', 'Bathrooms', 'YearBuilt']
        self.numeric_cols = [col for col in potential_numeric if col in self.df.columns]

        if not self.numeric_cols:
            self.numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()

        # Normalization
        self.df[self.numeric_cols] = self.scaler.fit_transform(self.df[self.numeric_cols])

        # Binary normalization
        bool_cols = [col for col in self.df.columns if 'Has' in col or 'Quiet' in col or 'Garden' in col]
        for col in bool_cols:
            self.df[col] = self.df[col].map({'Yes': 1, 'No': 0, True: 1, False: 0}).fillna(0)

    def match(self, hard_constraints, weights):
        filtered_df = self.df.copy()

        # 1. Hard Filtering
        if 'max_price' in hard_constraints:
            filtered_df = filtered_df[self.original_df['Price'] <= hard_constraints['max_price']]
        if 'min_beds' in hard_constraints:
            filtered_df = filtered_df[self.original_df['Bedrooms'] >= hard_constraints['min_beds']]

        if filtered_df.empty:
            return None

        # 2. Weighted Scoring
        weight_vector = np.array([weights.get(col, 0) for col in self.df.columns])
        feature_matrix = self.df.values
        scores = np.dot(feature_matrix, weight_vector)

        result_df = self.original_df.loc[filtered_df.index].copy()
        result_df['MatchScore'] = scores

        max_score = np.max(scores) if len(scores) > 0 else 1
        result_df['MatchPercentage'] = (result_df['MatchScore'] / max_score) * 100

        return result_df.sort_values(by='MatchPercentage', ascending=False).head(10)

# ==========================================
# STREAMLIT UI
# ==========================================

st.title("🏠 AI Property Matching Engine")
st.markdown("""
Welcome to the **Next-Gen Real Estate Discovery Portal**. Instead of static filters,
this engine uses weighted vector similarity to find properties that match your *lifestyle*.
""")

# Sidebar for Data Upload
st.sidebar.header("⚙️ Data Configuration")
uploaded_file = st.sidebar.file_uploader("Upload Property Data (Excel)", type=["xlsx"])

if uploaded_file:
    df_raw = pd.read_excel(uploaded_file)
    engine = PropertyMatchEngine(df_raw)

    st.sidebar.success("Data loaded successfully!")

    # --- USER PREFERENCE SECTION ---
    st.header("👤 User Preference Profile")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚫 Hard Constraints")
        st.info("Properties that don't meet these criteria will be excluded immediately.")
        max_price = st.number_input("Maximum Budget ($)", value=int(df_raw['Price'].max()))
        min_beds = st.slider("Minimum Bedrooms", 0, 10, 2)

    with col2:
        st.subheader("🎯 Preference Weights")
        st.info("Assign importance to features (1 = Low, 5 = Critical).")

        # Dynamically identify weightable columns (Booleans and important Numerics)
        weightable_cols = [col for col in df_raw.columns if 'Has' in col or 'Quiet' in col or 'Garden' in col or col in ['SquareFootage', 'Price']]

        user_weights = {}
        for col in weightable_cols:
            user_weights[col] = st.slider(f"{col}", 1, 5, 3)

    # --- MATCHING EXECUTION ---
    if st.button("✨ Find My Perfect Match", type="primary"):
        hard_constraints = {'max_price': max_price, 'min_beds': min_beds}

        with st.spinner("Calculating optimal matches..."):
            results = engine.match(hard_constraints, user_weights)

        if results is None:
            st.error("❌ No properties found matching your hard constraints. Please try increasing your budget or decreasing bedroom requirements.")
        else:
            st.balloons()
            st.header("🏆 Your Top Matches")

            # Top Match Metric
            top_score = results.iloc[0]['MatchPercentage']
            st.metric(label="Top Match Accuracy", value=f"{top_score:.1f}%")

            # Results Table
            st.dataframe(results[['PropertyID', 'Price', 'Bedrooms', 'MatchPercentage']].style.format({'MatchPercentage': '{:.1f}%'}))

            # Visualization
            st.subheader("📊 Match Distribution")
            fig = px.bar(results, x='PropertyID', y='MatchPercentage',
                         color='MatchPercentage',
                         color_continuous_scale='Viridis',
                         labels={'MatchPercentage': 'Match Accuracy %'})
            st.plotly_chart(fig, use_container_width=True)

            # Reasoning Section
            st.subheader("🔍 Why these matches?")
            top_features = sorted(user_weights.items(), key=lambda x: x[1], reverse=True)[:3]
            reasons = ", ".join([f"High priority on {f[0]}" for f in top_features])
            st.write(f"These properties were ranked highest because they strongly align with: **{reasons}**.")

else:
    st.warning("Please upload the `Case Study 2 Data (1).xlsx` file in the sidebar to begin.")
    st.image("https://img.freepik.com/free-vector/real-estate-concept-illustration_114360-1238.jpg", width=400)
