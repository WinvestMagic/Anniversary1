import streamlit as st
import os


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://piratediffusion1.s3.amazonaws.com/renders2/XerbVD/00001-tls-pro-tls1.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:White; font-size:85px;"><strong>My Valentine :heart:</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> :) VALLENTINESS DAYY</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000">hehe u got this my sweetheartt i made this extra longy for uuuu:heart:</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> yes yes now go solve all these ezz :) </span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1.Ahhh what lovey day of the monthy herese ________ ____<br> 2. What i give u hehe for it :) _________ <br> 3. Ahh main robo comp was on what dayy ___________ XX<br>4.  Hehr how long was that call at night 🥰 X HOURS<br> 5.  Remember my phone number now? ____-_____-____<br></span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)
st.markdown("""
    """)

box1 = st.text_input("1. Type a One-word awnser (ALL CAPS)")

if box1 == ('VALENTINES DAY'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">🤎Correcto :) (Not the letter B, think of a synonm of brown color **wood color**)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2. Type a One-word awnser (ALL CAPS)")
if box2 == ('SOFTWARE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">🧡Correctooo :))</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3. Type a One-word awnser (ALL CAPS)")
if box3 == ('FEBURARY 19'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">🧡 Ofc correctooo ;-;</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4. 4 words - seperate with commas (in order) - Locations (ALL CAPS) (W,X,Y,Z)")
if box4 == ('3 HOURS'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> 💙correcto long oneeee :) (Think of it as a synonm for Dark Blue) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. Type a NUMBERSS hehe (MM/DD/YYYY) ")
if box5 == ('346-399-2041'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>💜Hehe correctooo :) the day where it all began :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

if box1 == 'VALENTINES DAY' and box2 == 'SOFTWARE' and box3 == 'FEBURARY 19' and box4 == '3 HOURS' and box5 == '346-399-2041':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 30px;">DOPNE DONEENODENOENNENE (no cipher this time hehe just stright into the ___ heart i gave u :)) what did i give u?</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box11 = st.text_input("Final:What we putting hereehrherher")
    if box11 == ('PURPLE HEART'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh :) i love you baby :)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[We aer for life :heart:]"
                     "https://lh3.googleusercontent.com/E9TE3krSO04XjgMk2-vwkBHhQtiISDXhHn5aaq7OUkl_KQ9VmH-KWXPU9rv1bWDVQ_PX8fXNyNvVdACb6eBXNVQbGc6wjNh3IOg-YttS0vsiByZ-TG-pOB55vt1dtuc_lgo3puAxLpKYIlNMZIKtNBBBY3BjrSltikaLh_TOy0mq0xjKN9ksimz21_o5I-C0C_t-8fvzzQQh0EAXfwU7lM7AMOcLA2OPZtXaGcBzw-_180o2nYAgztXVf5ei0ov6a-wri_N5Ov9Udl66u5QRsGBlIvEjI47dbU0l3OpiN97R1uAeoQaj5YEUE4KE4WjnS_z-al5grz50AvaYdFmkiDh_AJNzlQAZ2xIzuuO52ajnNt_Tex7yisbdrk1CspHsAK1kg4ozWMQKuS6yQ18txd0Wnsr-qhbexFkG2jbQbIhvHlsoapKNmaS0qCbBGjtnMhWqiLkNkl4DezopSeIFu-s1FqBked7c-yx-VJhvA5LCV-lKLBm5vT0comZnpiN0FYYJRU8wrksEu-ottOyGadDvkezQbCqVbWmQwlRmqI7y-QOC-zgRMsuNy2XjF2NHpTmlHC_3-ZtzjAnF3vQbFlKxCRzi2uC8s_v0fSzZwdxH6821UCU_r2Tf3_XyBq9fVpcIXylOCLYq17NfhI5aXL8i-htE8SX9vsuMRz3-IoeTMqzKyhsdJR3kzS5GdDWjIN5iMVTAepvZ8aQyRwuFvHlW1S_5bmKmruvpao-7v3MJbwVW_FtrgDuFBcuD3GYnWlFxOb_b6y4l-ZCkSao6l4msHmTJSyd3NzVQ0azbykellkihcRP_VJ6dL0DuMd3cFo9nHOvw_vUvepw7-V2rHSRROOZk9NjXd8mkrdOBUn41oBJSlw6jy5LNep5QQ4S9QVzLxwI9pWMmYxhJbjpcSXUa0cWAcmlNAkBC0uk-Qc6PO2v84VydnzNa-iV8nlK64C0_5aPHFGlN4VCZytGAXQ=w101-h199-s-no?authuser=0")
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