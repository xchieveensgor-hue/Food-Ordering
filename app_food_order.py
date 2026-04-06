import streamlit as st

st.set_page_config(page_title="Food Order", layout="centered")

st.title("Food Ordering System")
st.markdown("---")

customer_name = st.text_input("Enter Customer Name")
food = st.selectbox("Select Food", options=["Nasi Lemak -- RM5", "Chicken Chop -- RM12", "Burger -- RM8"])
quantity = st.number_input("Quantity", min_value=1, step=1)

if st.button("Order"):
    try:
        if not customer_name.strip():
            st.error("Error: Customer name cannot be empty!")
        elif quantity <= 0:
            st.error("Error: Quantity must be more than 0!")
        else:
            prices = {"Nasi Lemak -- RM5": 5, "Chicken Chop -- RM12": 12, "Burger -- RM8": 8}
            total = prices[food] * quantity
            
            st.success("Order placed!")
            st.write("**Order Details:**")
            st.write(f"Name: {customer_name}")
            st.write(f"Food: {food}")
            st.write(f"Quantity: {quantity}")
            st.write(f"Total: RM{total:.2f}")
    
    except Exception as e:
        st.error(f"Error: {str(e)}")

st.caption("Food Ordering")
