import os
import streamlit as st


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://piratediffusion1.s3.amazonaws.com/renders2/Em80M9/00001-v-pro-6039794.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:White; font-size:85px;"><strong>Us :)</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Hmm what does this look like...I wonder :)</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Hehehe so listen carefully. Todayyy ur gonna be playing an escape rooom :)) Ofc ofc its digitall so rip, but it wont stop meee :heart:</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Gotta warn you though baby this is gonna be a lot harder then the other ones ;) </span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1.There something very tiny inside the flash drive, what is it? ____ __ ___ <br> 2. There three crazy things on those earnings that represent us :) guess them :) <br> 3. Final Message? <br></span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)
st.markdown("""
Add game here :)
    """)

box1 = st.text_input("1. Type a One-word awnser (ALL CAPS)")

if box1 == ('MICRO SD CARD'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">🤎Correcto :) (Not the letter B, think of a synonm of brown color **wood color**)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)


if box1 == 'MICRO SD CARD':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:White; font-size: 30px;">Yayayay hehe triple - word awnser about the earing i gave u :) what the three things they represent? seperate with commas</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box2 = st.text_input("1. Type a triple-word awnser with COMMMAS (ALL CAPS)")
    if box2 == ('SUN,MOON,AMYTHEST'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">🤎Correcto :) (Not the letter B, think of a synonm of brown color **wood color**)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh :) i love you baby :)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[We are for life :heart:]"
                     "https://lh3.googleusercontent.com/0iS6LO7RwyrxfurDbfJuFmCAj8_H7N6Okq4LNcfX0MP8InWXHoe-DUcMyqnQLJ0IgcjtrKH5hVXIt1h19JWj6KdHm0yzpnyoTNdVBLObN6pl46h-zD7F8uJcafoFCckBp8b8FCHb32vhKAqbdsdfzRDcjUwA_kln5lcPkRuZjvyXcJobwINWLRqGgjqsfrSjirueSzJdnQ8I7w6VNoGU3AtZ8SQ1wL-UK17HgCmtnPAQgpXq4VFZYkk3MABhB3Zjp86Phs-whARdGG-ET6TGpviLMa4qcTjHg70NArzuXAVVcMN7H3Nz2JOJBvd0R4Vr5rRSSaZESAMxIWJdOrNSNU1nr34LvSwl095mpCcx0_WL5Gd2AySLwoAFAAMZiFZarg9uAsFlGx4UUrcUaLZeigB4hopkqdZiqLuhyRjO1MYWMihXR6cKdoefR8UAnGjUFg3UdmdE0uuVmx9Cdw7O3Obn2nv1dkK7KwIgauhEMUIRbjSKcvN7wfiBxm59rK_ZzjZ3PQdSWkfC3gedot9VlO_C4hDtKpL62BDI_s8t9bZ7k1yc7NTUf7Vi8caXryFFNj2L6FxiGP7n6BOxAEhHLwkqqGZNZaslICRT1vVrNK1LedaBz2M5izeearUESt6v_3wrxRTKrgaeogVvdO15R8ydjl5PjpsG9NBLQ247wZsiFWCHcRHyU6vCwEKgOKEO-giLiS380UPaiF3Rf8NeBX2Pd544ElXNBvW82CWhP9IIvIeQ9PYoDZGC7cmgQKfVk_5tialFuokUS2ckX3-KhH5Y_bgBtAQp4RfGLOVWJyWTgajZ7fl4Yq3LXhAyaylxSG5Bjt1xDmxzyvraN_SmItwop3enubYk1VVkYd_M4mZEvxSrxBoSQLjP9PkhmzznVRE5sH3OlouibT6ge4W4QE8_NTDV59yHhKscCWjLMfVFX5FlqfwSOJCxwZSnoChuLZRv9K1aUaXRf9VUC_-68g=w101-h199-s-no?authuser=0")
        box3 = st.text_input("3. Type a One-word awnser (ALL CAPS)")
        if box3 == ('Always and Forever urs :)'):
            original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">And baby :) That it 💜 Just click "Run" in the Replit :)</span></p></em><b>'
            st.markdown(original_title4, unsafe_allow_html=True)
            st.subheader("[Our Journey :heart:]"
                         "(https://replit.com/join/bwhrsjpyne-ks2007)")
        else:
            original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
            st.markdown(original_title5, unsafe_allow_html=True)
    else:
        original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
        st.markdown(original_title5, unsafe_allow_html=True)


else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

# ----------------------Hide Streamlit footer----------------------------
hide_menu = """
<style>
footer{
        visibility:hidden;
    }
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
# --------------------------------------------------------------------