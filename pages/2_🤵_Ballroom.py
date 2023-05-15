import streamlit as st
import os


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://weddingsbythebreakers.com/wp-content/uploads/2012/03/MedBallroom.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size:85px;"><strong>Welcome to the ballroom!</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Hmm what does this look like...I wonder :)</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Hehehe so listen carefully. Todayyy ur gonna be playing an escape rooom :)) Ofc ofc its digitall so rip, but it wont stop meee :heart:</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Gotta warn you though baby this is gonna be a lot harder then the other ones ;) </span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1. Where did we meet first time after robo comppy? (XX.XX.XXXX) <br> 2. Whattt was the first dayyy we get huggie? (XX.XX.XXXX) <br> 3.What was the firsty dayyy we holdyyy handsss?(XX.XX.XXXX)<br> 4. What song we first learnyyy tg hehe _____ _____?<br> 5. Which songy did i singgyyy u on our all nighter hehehhe __ _____ ___ ______ ?<br> 6. How longyyy were we uppo till on our ft call? X hrs and X mins? <br> 7. Who disturbed us >:(   _____ <br> 8. whatd we get in the sky before our trippy? _________ ______<br> 9. who came withy us on our amazing walkkyyyy  __________ ?<br> 10. And finally hehe, whats the three words that i knew that i wanted to say from our day forward? ___ ____ ___   </span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)
st.markdown("""
    """)

box1 = st.text_input("1. Type a Date (ALL CAPS)")

if box1 == ('03.14.2022'):
    original_title4 = '<b><em class      = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correcto :) funny incident ykyk ;) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2.Type a Date (ALL CAPS)")
if box2 == ('05.08.2022'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correctooo :)) eeee goshy 🥰</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3.Type a Date (ALL CAPS))")
if box3 == ('05.01.2022'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correctyy :)) so softy ur hands are 💗</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4. 2 words with a space in between (ALL CAPS)")
if box4 == ('JHOOME GORI'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> CorRRRRrrecto :) hehe we be twirlingg ❤</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. 4 words with spaces in between (ALL CAPS) ")
if box5 == ('A WHOLE NEW WORLD'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>Hehe correctooo :) Aladddinnn goes crazyy :) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box6 = st.text_input("6. X:XX ")
if box6 == ('5:00'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Hehe correcto :) bro ninja.</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box7 = st.text_input("7. One word (CAPS)")
if box7 == ('DADA'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Hehe correcto :) fr this guy -_--__-</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box8 = st.text_input("8. two words with a space (ALL CAPS)")
if box8 == ('FINGER HEART'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Hehe correcto :) so pretty 💝</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box9 = st.text_input("9. One word (CAPS)")
if box9 == ('DUCKLINGS'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">️Hehe correcto :)) tiny tiny kiddos :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box10 = st.text_input("10. hehehe think about it :) - THREE words (_ ____ ___)  :)")
if box10 == ('I LOVE YOU'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Hehe correcto :) I very much do 💖 </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

if box1 == '03.14.2022' and box2 == '05.08.2022' and box3 == '05.01.2022' and box4 == 'JHOOME GORI' and box5 == 'A WHOLE NEW WORLD' and box6 == '5:00' and box7 == 'DADA' and box8 == 'FINGER HEART' and box9 == 'DUCKLINGS' and box10 == 'I LOVE YOU':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> BABY U SOLVED PG1  :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 30px;">What coloroes is that little token I gave u hehe (in binary)? :))</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box11 = st.text_input("(ALLCAPS) with spacesss between bytes")
    if box11 == ('01010111 01001000 01001001 01010100 01000101'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh :) 💜💜💜 i love you baby :) Here ur hinty ;) </span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[Image Hint :) :heart:]"
                     "https://lh3.googleusercontent.com/XH7QAYDoK0NgeKcN9-dWFZmDGIADRYlfzWH3pBvkxQZkxHA4oQE7_lpJVel_vsM2BiVOp4JAmpK_Z0phhfKzPiESc8J_Vt_eCYtH4mS3eLR84tcHzp4SPnty_xTcEmX7E3-jKiUscWeSiFxwW37hDSNotEviUgPYqra52N4UKgT9YFag6p-L8MSLClJNWUHHs7b3oJ2c2INhVrKBIEEIoA8SxXEsws4Z23vHe2m8sZkWWyQrF5nIJ0lskloNRoEwO8yIZ_LJ3OMMDc_VDg6LjFO0JnJDL7rC9FlYNUUI3RgDczOgb0DCN067MU4yyw9SYb3Yc9NfaUPBsovRvcGo72MvG40nEVVsTI2TuuzrGKejtPGaohQoVDrHqJei7kwgOTabiHEjAxEdkdqDJYmWLD1TWl3HHt4sfXOzQKavYqeMW9rgpjZfjLHCj3qceJEbu7tnf1RTf129Xfo3JjpcgHeIK5k5LTPq4v8Qgm6OJhImiDJ8LAEcI6-1cQtw61tdvFUMl8SDfrcqjr0u6Lv_jCaEpNZf0y-huzuPb3gc9QyudYziqcjR9kA0zOv4T7_Sw9_AzBfv25MY67bEoiHvB4iw_GX7Jj5-ZZAqj7JknRLiSsGjOjO0s5mV0NAc22HdpBqUI_RkVM7pFMf0QmCj4b0Px9zHMvwSZP3UxSiZXnOJ2JnpkT8HkH2go4LBNg1H3KhGYWgKqm6mzdMjNGJxyK2pkd1GLenrcX-gS8NuJaIFM6mnk4SVulMIbs1_9GXlJYSUyGDHmcVsCkvVh-EG80V7OcjVgKpHy6eD3ErHnn28jJUw3FHXOS-TeuLEMrr-8k9StP37o6u6OYvUocNxp3FZSCLMKVR0gAeejeRQjKSNIs7SdoeCGcEkblVkbxNhLV_WgndxugvaHYCnqbb7yXUl9S7S17wq_jGqJnz3dS0d6iNj7-S82n-W_qd5Nx7wn7KK5IFIgCJhtvUdFY0Mww=w101-h199-s-no?authuser=0")
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

