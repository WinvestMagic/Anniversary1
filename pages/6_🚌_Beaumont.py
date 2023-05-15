import streamlit as st
import os


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://freerangestock.com/sample/134405/camper-van-and-starry-night-sky.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:White; font-size:85px;"><strong>Beaumont :)</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Hehe pretty background :) andd looky it our bus :DD</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Sosososoo so much images top collect keep going :) It beaumont time :):heart:</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Just gets better and better 🥰</span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1. What was reporting time for beaumontyyy? X:XX<br>2.- Lolo how many in total songosss we dooo for showww? X <br> 3. How many picturess in our album from this monthooo? XX <br> 4. How long drivey to nearsttt hrrhrhr X HOURS? <br> 5. Hehe what the first thingy we did after we got there :) __ ? <br> 6. How far were we from ur mom hehehhehe ____ MILES <br> 7. Whats the thingy that made the little accident we had oopssiesssss ________  <br> 8. Hehe hmmm what was i supposed to unzip on the bus 👀 ________<br> 9. Hehe how long did we very much kiss on that ride ;) ___ _____<br> 10. -What i tell ur mom i was doin ehheheheheh? ____ </span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)
st.markdown("""

    """)
box1 = st.text_input("1. Type a One-word awnser (ALL CAPS)")

if box1 == ('1:30'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correcto :) - oh yes on time very importante </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2. Type a One-word awnser (ALL CAPS)")
if box2 == ('9'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">yeppy and we get more MULAAA 💖</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3. Type a One-word awnser + Number of day (ALL CAPS) ")
if box3 == ('24'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> correctio hehe can u bleive itt :) i lovey :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4. Type a One-word awnser (ALL CAPS)")
if box4 == ('2 HOURS'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> correcto :)) long driveyyyyys</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. Type a 3-word awnser and spaces (ALL CAPS)")
if box5 == ('HUGGY'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>Finally :) made me wait so long >:(</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box6 = st.text_input("6. Type a One-word awnser (ALL CAPS) ")
if box6 == ('100 MILES'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">💘hehehhhehe yessssss far far away :)  i love u :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box7 = st.text_input("7. Type a One-word awnser (ALL CAPS)")
if box7 == ('LIPSTICK'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heh ;) Crazy even saw me shirtless ;) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box8 = st.text_input("8. Type a One-word awnser (ALL CAPS)")
if box8 == ('BLACK'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">matchy :) correcty :) 💕</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box9 = st.text_input("9. Type a One-word awnser (ALL CAPS) include the '(s)' at the enddd")
if box9 == ('DRESS'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">yes i cant belibe i didnt know i could do that -_-</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box10 = st.text_input("10. Type a One-word awnser (ALL CAPS) I love this place 🥰")
if box10 == ('WHOLE TIME'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">goddamn woah. just woah :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box11 = st.text_input("11. Type a One-word awnser (ALL CAPS) I love this place 🥰")
if box11 == ('SLEEPING'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">hi very very funnny hehhehe whoopsiess ;)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

if box1 == '1:30' and box2 == '9' and box3 == '24' and box4 == '2 HOURS' and box5 == 'HUGGY' and box6 == '100 MILES' and box7 == 'LIPSTICK' and box8 == 'BLACK' and box9 == 'DRESS' and box10 == 'WHOLE TIME' and box11 == 'SLEEPING':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:White; font-size: 30px;">hehe u finish :) ahh beaumont was smth else :) 💜 nowww: What color is the little bus token hehe :) (vigenere Cipher good lucky) </p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box14 = st.text_input("Final: Type the number out hehe with a smiley face (in vigenere Cipher Cipher) ")
    if box14 == ('nGmni akr bogpitr Fmeorcbi usxfyyr uiw!'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">hehe the whole ride was j woah. Here ur hinty ;)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[Image Hint :)) :heart:]"
                     "https://lh3.googleusercontent.com/O2F82sJdsuUwHr5RobKhPjdOQM7V2_HI9HF-T2h2LGXMoyshbZtv25pCb1QaxFSRVpchJnOTzTLPBJ7xL6TpAYL660xNbz7VGKqeDeYTHnOvI4inla3BMaMiik8sVpxK69dEEUyQ6eUNkxWOzR0Qj3jd8PsGZW1Le4FxYzU1Mekr_oG5Z2yCSty3w_QMHCtmZSIUrGOdjLsKOYDsAt-lFH_kmsR9eBDTtbUxrmOMtrp0DiMkphVMtQqSh5wWsPrBC0lZN9mfJeV0ejonHNrTLPj0_WefrY727dI8iDnurTK5wTCCJUCdb-J0UCrkgDE_indPPQH-PGteX6YdxTpIIhNItD3CKPe58OF1YxdyNzuTEi2CS2nf6B_a5xK1k1HSEZorX_rJJY5QUlo3Ih7nSDE2zC0v0sM2ew4QP_R2vUtkUwm6xdAL_cPe1feeRu0D0nXkeSEly6EE0hnv2TXk6_t9r929F7RG5jgPH5Sti1LnusF-_a4ten_0lT5Px4dWjLcfGINQbDC3yQb4MsdihF_heIIsvQwIzt2wAFW4TE4ORM-BE-4nL28EaSHszePRWkUl1c3Sjg6trq970GMNCSzUMVg9bsW5rhr1QPuFOmHcLr42LgapyiHr3fk7_sU9RWPKeka08B8BuCNVLunHjKzGvSvr0FQUw48Pytp-aKCP9sGEVjjC1jXdRj3UDrnAJzsiAJ24Kt547rSovtAr7qIlKIfkw3XCDyXCATxN29c_tqyzajIDXlLwBhRNihfv6s8yPmd8C-YbAzBA_LYtVLgLpL-Exp3LXHiRWXmegafdF-uihAKIOcO4rNkcGJl3VzVAgEQmmwlUzh1ay3OeZZtLKnQRvMrK0Ja5ZAFnNhZSWZJJPNc3F04Qp_-lGXglPxZHqX3PcO3qlhOjw48UbLUwrS6vcpuvq3Ffw-F_5xLK63GfHqzlvKQ360Xewgo-d-euZ7j37iFBG6Y-IagaAg=w101-h199-s-no?authuser=0")
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