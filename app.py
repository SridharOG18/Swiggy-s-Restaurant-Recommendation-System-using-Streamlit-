import streamlit as st
import pandas as pd
import pickle

# Page configuration
st.set_page_config(
    page_title="Restaurant Recommender",
    page_icon="🍽️",
    layout="wide",
)

# Custom CSS for Swiggy-like Aesthetic
st.markdown("""
    <style>
        /* Body and General Styling */
        body {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ff5722; /* Swiggy orange */
        }
        .block-container {
            padding: 1rem 2rem;
        }
        /* Horizontal Filters Styling */
        .horizontal-filters {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #ffffff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .horizontal-filters .stSelectbox, .horizontal-filters .stSlider {
            flex: 1;
            margin: 0 10px;
        }
        /* Restaurant Cards Styling */
        .restaurant-card {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 10px;
            text-align: left;
        }
        .restaurant-card h3 {
            color: #ff5722;
            margin-bottom: 10px;
        }
        .restaurant-card p {
            margin: 5px 0;
            color: #333333;
        }
        /* Footer Styling */
        .footer {
            margin-top: 20px;
            text-align: center;
            color: #777777;
        }
    </style>
""", unsafe_allow_html=True)

# Load data and models
@st.cache_data
def load_data():
    cleaned_data = pd.read_csv("D:/Swiggy_Proj/Swiggy_Stremlit/cleaned_data.csv")
    encoded_data = pd.read_csv("D:/Swiggy_Proj/Swiggy_Stremlit/encoded_data.csv")
    with open("D:/Swiggy_Proj/Swiggy_Stremlit/label_encoders.pkl", "rb") as f:
        label_encoders = pickle.load(f)
    return cleaned_data

try:
    cleaned_data = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Horizontal Filter Options
st.markdown('<div class="horizontal-filters">', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    selected_city = st.selectbox("City", ["All"] + list(cleaned_data["city"].unique()))
with col2:
    selected_cuisine = st.selectbox("Cuisine", ["All"] + list(cleaned_data["cuisine"].unique()))
with col3:
    price_range = st.slider("Price Range (₹)", 100, 300, (100, 300))
with col4:
    min_rating = st.slider("Minimum Rating", 1.0, 5.0, 3.5)

st.markdown('</div>', unsafe_allow_html=True)

# Filter restaurants
def filter_restaurants(data):
    mask = pd.Series(True, index=data.index)
    if selected_city != "All":
        mask &= data["city"] == selected_city
    if selected_cuisine != "All":
        mask &= data["cuisine"].str.contains(selected_cuisine, case=False, na=False)
    mask &= data["cost"].between(price_range[0], price_range[1])
    mask &= data["rating"] >= min_rating
    return data[mask]

filtered_data = filter_restaurants(cleaned_data)

# Display Restaurant Cards
st.title("🍴 Sridhar's Recommended Restaurants")
st.markdown("Find your perfect dining spot based on your preferences! 🍽️")

if not filtered_data.empty:
    cols = st.columns(3)  # Grid layout with 3 cards per row
    for index, row in filtered_data.iterrows():
        with cols[index % 3]:
            st.markdown(f"""
                <div class="restaurant-card">
                    <h3>{row['name']}</h3>
                    <p>📍 <b>Location:</b> {row['city']}</p>
                    <p>🍴 <b>Cuisine:</b> {row['cuisine']}</p>
                    <p>⭐ <b>Rating:</b> {row['rating']} (Based on {row['rating_count']} reviews)</p>
                    <p>💰 <b>Price:</b> ₹{row['cost']}</p>
                </div>
            """, unsafe_allow_html=True)
else:
    st.warning("No restaurants match your criteria. Please adjust the filters.")

# Footer
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown("""
    <div class="footer">
        Built by <b>Sridhar</b>. Powered by Streamlit.
    </div>
""", unsafe_allow_html=True)
