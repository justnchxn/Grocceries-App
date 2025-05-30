import streamlit as st

# Initialize recipes in session state (only once)
if "recipes" not in st.session_state:
    st.session_state.recipes = {
        "Pasta": ["Pasta", "Tomato", "Cheese"],
        "Salad": ["Lettuce", "Tomato", "Cucumber"],
        "Omelette": ["Eggs", "Milk", "Cheese"]
    }

supermarket_items = ["Tomato", "Cheese", "Milk", "Bread", "Eggs", "Lettuce", "Cucumber", "Pasta"]
fridge_items = ["Eggs", "Milk", "Tomato"]

st.set_page_config(page_title="Recipe App", layout="centered")
st.title("🥘 Recipe App")

page = st.sidebar.selectbox("Navigate to:", ["Recipes", "Supermarket", "Fridge"])

if page == "Recipes":
    st.header("📖 Recipes")

    # List existing recipes with remove buttons
    for recipe in list(st.session_state.recipes.keys()):
        cols = st.columns([8, 1])
        cols[0].write(f"**{recipe}**: {', '.join(st.session_state.recipes[recipe])}")
        if cols[1].button("🗑️", key=f"remove_{recipe}"):
            del st.session_state.recipes[recipe]
            st.rerun()

    st.markdown("---")
    st.subheader("Add a new recipe")

    new_recipe_name = st.text_input("Recipe name")
    new_ingredients = st.text_area("Ingredients (comma separated)")

    if st.button("Add recipe"):
        if new_recipe_name.strip() == "":
            st.warning("Please enter a recipe name.")
        elif new_ingredients.strip() == "":
            st.warning("Please enter ingredients.")
        elif new_recipe_name in st.session_state.recipes:
            st.warning("This recipe already exists.")
        else:
            ingredients_list = [i.strip() for i in new_ingredients.split(",") if i.strip()]
            if ingredients_list:
                st.session_state.recipes[new_recipe_name] = ingredients_list
                st.success(f"Added recipe '{new_recipe_name}'!")
                st.rerun()
            else:
                st.warning("Please enter at least one ingredient.")

elif page == "Supermarket":
    st.header("🛒 Supermarket")
    st.write("Available items:")
    st.write(", ".join(supermarket_items))

elif page == "Fridge":
    st.header("🥶 Fridge")
    st.write("Items currently in your fridge:")
    st.write(", ".join(fridge_items))
