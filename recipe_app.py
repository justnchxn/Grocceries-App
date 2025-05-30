import streamlit as st

# Sample data
recipes = {
    "Pasta": ["Pasta", "Tomato", "Cheese"],
    "Salad": ["Lettuce", "Tomato", "Cucumber"],
    "Omelette": ["Eggs", "Milk", "Cheese"]
}

supermarket_items = ["Tomato", "Cheese", "Milk", "Bread", "Eggs", "Lettuce", "Cucumber", "Pasta"]
fridge_items = ["Eggs", "Milk", "Tomato"]

# App title
st.set_page_config(page_title="Recipe App", layout="centered")
st.title("🥘 Recipe App")

# Sidebar navigation
page = st.sidebar.selectbox("Navigate to:", ["Recipes", "Supermarket", "Fridge"])

# Page content
if page == "Recipes":
    st.header("📖 Recipes")
    for name, ingredients in recipes.items():
        st.subheader(name)
        st.write(", ".join(ingredients))

elif page == "Supermarket":
    st.header("🛒 Supermarket")
    st.write("Available items:")
    st.write(", ".join(supermarket_items))

elif page == "Fridge":
    st.header("🥶 Fridge")
    st.write("Items currently in your fridge:")
    st.write(", ".join(fridge_items))
