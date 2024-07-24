import streamlit as st

st.title("Palindrome")

a=st.text_input(label="Enter a string")

print(a)
st.button("Submit")
b=a[::-1]
if(a==b):
    st.write("Palindrome")
else:
    st.write("Not a palindrome")
