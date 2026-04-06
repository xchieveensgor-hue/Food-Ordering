import streamlit as st

st.set_page_config(page_title="Food Order", layout="centered")

st.title("Food Ordering System")
st.markdown("---")

customer_name = st.text_input("Customer name")
food = st.selectbox("Food Selection", options=["Nasi Lemak", "Chicken Chop", "Burger"])
quantity = st.number_input("Quantity", min_value=1, step=1)

if st.button("Order"):
    try:
        if not customer_name.strip():
            st.error("Error: Customer name is empty, display an error message")
        elif quantity <= 0:
            st.error("Error: Quantity is less than or equal to 0, display an error message")
        else:
            # Map clean names to prices
            prices = {"Nasi Lemak":RM 5, "Chicken Chop": RM 12, "Burger": RM 8}
            total = prices[food] * quantity
            
            st.success("Order placed successfully!")
            st.subheader("Order Information")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Customer name:**")
                st.write("**Food Selection:**")
                st.write("**Quantity:**")
            with col2:
                st.write(customer_name.strip())
                st.write(food)
                st.write(str(quantity))
                st.write(f"RM{total:.2f}")
    
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")

st.caption("FOOD ORDERING")
