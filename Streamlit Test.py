import streamlit as st

st.title("Danielle's recipes")
st.header("Black bean taco's")

st.markdown(
    """ 
    Probeer deze verukkelijke black bean taco's
     
    """
)
st.header("Ingredienten:")
st.subheader("Tacos:")
st.checkbox("6 medium tortillas")
st.checkbox("50 g walnuts")
st.checkbox("300 g mushrooms")
st.checkbox("400 g of cooked black beans")
st.checkbox("500 g mushrooms")
st.checkbox("20 g of taco spices")
st.subheader("Toppings:")
st.checkbox("3 tomatoes")
st.checkbox("1 cucumber")
st.checkbox("100 g of salad")
st.checkbox("20 g Sambal oelek")
st.checkbox("20 g Pickeled jalapenoes")
if st.button("DEF E opstellingen"):
    st.balloons()
