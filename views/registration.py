import streamlit as st
from views.functions.get_products import getProduct

st.title("REGISTRATION")

if 'vendor' not in st.session_state:
    st.session_state['vendor'] = []
if 'vendordict' not in st.session_state:
    st.session_state['vendordict'] = {}

vendor_name = st.text_input("Enter vendor's name")
productlist = []

if vendor_name and vendor_name not in st.session_state.vendor:
    st.session_state.vendor.append(vendor_name)
    productlist = getProduct()
    

if productlist:
    option = st.selectbox(
        "Select your product?",
        options=tuple(productlist),
        index=None,
        placeholder="Select from the options below.",
    )
    st.write(f"Selected product: {option}")
else:
    st.write("No products available for this vendor.")
