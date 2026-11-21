import streamlit as st
import numpy as np

st.title("Danielle's recipes")
st.header("Black bean taco's")

st.markdown(
    """ 
    Probeer deze verukkelijke black bean taco's
     
    """
)


array = np.array([2,20,100,120,5,1,0.25,25,5,15])
if st.button("2 x"):
    array = array*2
if st.button("1 x"):
    array = array
if st.button("0.5 x"):
    array = array*0.5
st.header("Ingredienten:")
st.subheader("Tacos:")
st.checkbox(f"{array[0]} medium tortillas")
st.checkbox(f"{array[1]} g walnuts")
st.checkbox(f"{array[2]} g mushrooms")
st.checkbox(f"{array[3]} g of cooked black beans")
st.checkbox(f"{array[4]} g of taco spices")
st.subheader("Toppings:")
st.checkbox(f"{array[5]} tomatoes")
st.checkbox(f"{array[6]} cucumber")
st.checkbox(f"{array[7]} g of salad")
st.checkbox(f"{array[8]} g Sambal oelek")
st.checkbox(f"{array[9]} g Pickeled jalapenoes")

