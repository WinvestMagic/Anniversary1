import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://t3.ftcdn.net/jpg/05/58/83/74/360_F_558837483_AJQbnalPbXQLpLOS4QQNUncCdDBLJyKo.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

#navbarrr

original_title = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 80px;">Hey again baby :)</p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 50px;">Happy Anniversary Day 💜</p></em><b>'
original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 50px;">and Happy 12 monthos to us 🥰 </p></em><b>'
original_title3 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> i love you like crazy :)</p></em><b>'
original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 30px;"> Time to play a little game?</p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
st.markdown(original_title4, unsafe_allow_html=True)
st.markdown(original_title3, unsafe_allow_html=True)
st.markdown(original_title5, unsafe_allow_html=True)
st.markdown("""
    """)


#----------------------Hide Streamlit footer----------------------------
hide_menu = """
<style>
footer{
        visibility:hidden;
    }
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
#--------------------------------------------------------------------