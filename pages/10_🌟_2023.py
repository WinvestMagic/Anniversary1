import streamlit as st
import os


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://piratediffusion1.s3.amazonaws.com/renders2/XY9oVr/00001-r-pro-xjc19.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:White; font-size:85px;"><strong>New Year :)</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Its a newww yrrrrrr</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000">u collected tons of imagess only a couple to goooo :) - happy new yearr</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> u got this this one ez peasy :) </span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1.  Hmm hmm what song we start learning here? ___ _____<br> 2. What songy u learn the Saturday accident happen :( _____ <br> 3. Which day u no come to classy ;-; xx.xx.xxxx<br> 4. What i have on the day ur shoulder not go good :( ____ ______<br> 5. Lol where was i when u snapped me that picture of the hospital monitor at 12:22 AM ___________ ________<br></span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)
st.markdown("""

    """)

box1 = st.text_input("1. Type a TWOO-word awnser (ALL CAPS)")

if box1 == ('SUN ZARA'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correcto :) me missy u babyyyy we get again :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2. Type a One-word awnser (ALL CAPS)")
if box2 == ('SHEILA'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correctooo :)), im saying.... ur actually my sexy sheila 👀</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3. Type DATE awnser (ALL CAPS)")
if box3 == ('01.22.2023'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">ahh man :( me missed u sm</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4.Type type 2 yrs old ")
if box4 == ('ROBO COMP'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> ahh robo robo eeee  </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. Type a 2 words")
if box5 == ('MURTAZAS HOUSE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>correctyy :) i did sleepover and i was like noo ;-;</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)



if box1 == 'SUN ZARA' and box2 == 'SHEILA' and box3 == '01.22.2023' and box4 == 'ROBO COMP' and box5 == 'MURTAZAS HOUSE':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:White; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:White; font-size: 30px;">lol qujickest one yet heh ahh crazy montho (PORTA CIPHER) These C_____ S____ are pretty hehe i hope u like it ? (</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box11 = st.text_input("Gotta listen smhhh")
    if box11 == ('XGKKIOTHFVGE'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh :) i love you baby :)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[hehe i came back >:) :heart:]"
                     "https://lh3.googleusercontent.com/_hs9qVHdXia4EyzEXtvd4ReW1CB14eyU3boFKQqsZ1cYE4Az0jjDRf3LhCIuAH5y5IRtmwqe0f0VlOHB7OrNT1Knr44crtASPDCtFdJvOGiF9bOGczvUgpUztrSgZsBfreNVf-J-kDXyIDlqY_CaEFXJ3P6qGsNNqRn6v02OLSW2du-mHVDKdJC3QOY6qBGyLJ_kaARdtOnIghv4r6zfhA_9_sMPHrVMELULJahMC_ZnPIU3O4XE2pvSG6LJmFhqPCpFSsZTX2yTp0ifkLwPjbGhl-po2_EkJrpwAxHaiLV7oOWcVE0_mvk62v0oiN1VGp0YavglgtxdJVp-uLWarStKUTEVL72OvV3wY0TwUDpLiUZ1YXIDFazDmxeJINAzYWTMrnRacWGrbKJWAw-JOoC34o74nxHTfOTmV9Tm4nGcQkmTqt1dYna3_1gFdU-49A9gbM7wXy8-D5z07bmRtyU-TVkTlZXbBfxvKjcAPGWa1Ws7RRQvI8RV_zeIdRyrH6iXrm8rD-4ZHhFuOI-uUUYTJmDS8wtJ2FJAfA0OS_DHZhmhrFGhtOGX7QT9I-PswsqP9AJJvcjPCT5ybyBO9szVXCtCITElz7aeEuBNhiTPC5UPhoxRncalnUaNPKchVy2ZC12lMKDLaq8UfJrq04hYgJeNyukeI7vc-EO3eJg9RfGzoPjy42Zr1tDcc-VB-zgZ12D3n-rR8xDXpLqG5pukAJ65JdZPl10k_0ejsHf2t7C8YOIsDr0ycKXMEWqkksh6BAVCYJhc8rTfGZHW_ELe3zI1oO5_lX6eZPzjyRMXBlrRU8t0moXeTmUyvO9_Jgn7umUwARUehloPGJAPK_BPwLwrsBfIln5QysGyMbM-4dHYxCPpy3do70H26CBgNAGNvxLy_W2UWTM55Vgn06fbWFOltsvpainX6Q4qjQN5kVtAFbTB7tyGbMgcjbAQUZ0FfVOTcjifW5w-GsQl_A=w101-h199-s-no?authuser=0")
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