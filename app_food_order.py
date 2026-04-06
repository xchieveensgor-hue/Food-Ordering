import streamlit as st

st.set_page_config(page_title="Food Ordering System", layout="centered")

st.title("Food Ordering System")

customer_name = st.text_input("Enter Customer Name", placeholder="Enter your name")


food = st.selectbox("Select Food", options=["Nasi Lemak", "Chicken Chop", "Burger"])


quantity = st.number_input("Enter Quantity", min_value=1, step=1, value=1)


if st.button("Order"):
    if not customer_name.strip():
        st.error("Please enter your customer name.")
    elif quantity <= 0:
        st.error("Quantity must be greater than 0.")
    else:
        
        prices = {"Nasi Lemak": 5, "Chicken Chop": 12, "Burger": 8}
        total = prices[food] * quantity

        st.success("Order placed successfully!")

        st.markdown("**----- Order Summary -----**")
        st.write(f"**Customer Name:** {customer_name.strip()}")
        st.write(f"**Food:** {food}")
        st.write(f"**Quantity:** {quantity}")
        st.write(f"**Total Price:** RM {total:.2f}")
