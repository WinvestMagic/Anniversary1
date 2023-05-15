import streamlit as st
import os


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://as1.ftcdn.net/v2/jpg/02/78/95/34/1000_F_278953450_TF3XYtwWEHlREGWUOTrdE0gM0CrDzmfI.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:White; font-size:85px;"><strong>Dil Se Naach</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> ur bday :)</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> image image image heheheh :)  u connect pieces soon :) ahhh ur bday + dil se ❤💚💛💙💜🤍💗🧡💕💖💝</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Packkeddd monthy gl :) </span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">  1. Hehe what time did i come to ur partyyyy? X:XX <br> 2. What we have right before it it? _______ ______ ______ <br> 3.what color was the secret bag i gave uu? _____ <br> 4. What did i 3d printy u? ______<br> 5. Hehe what we eat for dindin theree? ______:) <br>  6. What color theme was it  💕? ______? <br>  7. Anddd what color was i wearing :) _____? <br>------DIL SE------<br> 8. Lol what song were we practicing with sid lol before we run away? <br> 9. What time we take our sunshine pic :)<br> 10. What was ur firsty song cutie? <br> 11. Hehe hmm hmm we ran away and whats the first thing i did once we ran up the stairs ;) - did smth, and then did smth else ______ ____ _________ ___ _____, ___ _____ ____ ___ <br> 12. What very amazing place did we find ;)_? <br> 13. Hehehe after this we foundd another place ;) <br>  14. And who got us scared lol so we started runninggg?<br>15. Hehe what we do backstageyyy when performance going on <br>16. What did my monki self forget to dooo? </span></p></em><b>'

st.markdown(original_title101, unsafe_allow_html=True)

st.markdown("""
    """)

box1 = st.text_input("1. Time hehe (ALL CAPS)")

if box1 == ('4:30'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correcto :) Yes yes i remmeeber </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2. Type a One-word awnser (ALL CAPS)")
if box2 == ('NAACH'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">saw u twice hehe 🥰</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3. Type a One-word awnser")
if box3 == ('GOLD'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> correctooo heh ;)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4. Type a One-word awnser (ALL CAPS)")
if box4 == ('HEART'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> correcto :)) eeeeee i sorry how it turned out :(</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. Type a One-word awnser (ALL CAPS)")
if box5 == ('PASTA'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>yummy yum yum :) correct :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box6 = st.text_input("6. Type a One-word awnser (ALL CAPS) ")
if box6 == ('PURPLE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">💘gosh hehe :)  i love u :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box7 = st.text_input("7.  Type a Two-word awnser (ALL CAPS)")
if box7 == ('BLUE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Heh correcto that shirt nicey :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box8 = st.text_input("8. Type a One-word awnser (ALL CAPS)")
if box8 == ('SENORITA'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Yesss over that staircase thingyyy </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box9 = st.text_input("9. Type a Time awnser (ALL CAPS)")
if box9 == ('3:32'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">So brighttttttttt and so cute :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box10 = st.text_input("10. Type a One-word awnser (ALL CAPS)")
if box10 == ('BAWARE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> bing bong circus song :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box11 = st.text_input("11. Type a multiple awnser (ALL CAPS)")
if box11 == ('PUSH YOU AGAINST THE WALL, AND THEN KISS U'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> i want rnrnnr >:( heh ur flaming hot 🔥 </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box12 = st.text_input("12. Type a two-word awnser (ALL CAPS)")
if box12 == ('FAMILY RESTROOM'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E" u alr know ;)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box13 = st.text_input("13. Type a one-word awnser (ALL CAPS)")
if box13 == ('HALL'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> we sneaky sneaky :)))))) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box14 = st.text_input("14. Type a two-word awnser (ALL CAPS)")
if box14 == ('MAHESH SIR'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">hehe my goshy wouldve been intersting if he saw us... </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box15 = st.text_input("15. Type a two-word awnser (ALL CAPS)")
if box15 == ('HOLD HANDS'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">hehe this one was amazing 🥰💕💗 </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box16 = st.text_input("16. Type a two-word awnser (ALL CAPS)")
if box16 == ('CHANGE COSTUME'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">oops?</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

if box1 == '4:30' and box2 == 'NAACH' and box3 == 'GOLD' and box4 == 'HEART' and box5 == 'PASTA' and box6 == 'PURPLE' and box7 == 'BLUE' and box8 == 'SENORITA' and box9 == '3:32' and box10 == 'BAWARE' and box11 == 'PUSH YOU AGAINST THE WALL, AND THEN KISS U' and box12 == 'FAMILY RESTROOM' and box13 == 'HALL' and box14 == 'MAHESH SIR' and box15 == 'HOLD HANDS' and box16 == 'CHANGE COSTUME':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 30px;">finishhhhh :) bday and dil se sooo soo muchy we do :) How many sparkly silver thingies on that braclet hehei gave u :)(add a smiley face to ur awnser)</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box17 = st.text_input("Final: Type the number out hehe with a smiley face (in Atbash Cipher) ")
    if box17 == ('12 :)'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Here ur hinty ;)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[Image Hint :)) :heart:]"
                     "https://lh3.googleusercontent.com/YHubqbrIU4k7zRDE5mQr6iVrfojcOxCImgLzz_k96orI5_gMRUluZLZrQ0qeC-wAFcXckGr51Ixec5UbG5w1ZAokPUf66zVFvO8UylEoLH8Tr4945NFubcEU_1yk4nP4wU4Eo6qLGdxh7xxj7JjSBPL_7JtPlxMAGRc1gXZM4V8Zq-Kt7k1OjinfDj9yyL0nBq9IaLMgeLhpWDVzYfGLKFmXCGp5Vo3oLD-ekyfSCpa7kU59xmJbGu8O4i9yB89lc5MW9cCzJbRbrhVnPoGuXKpXpoMQLntLoT8arS2cPXUyl9XH7RyyxQuDGNsgKvmbDoNVVOaq6NxmZKYBRvlxJ_pMyJmyOrhRlX6QOBsnGS9G5b9fV-nveKgaGlpICPjNL1utR8WnYrs63tc77AJZFlg2D0nC53CMR5Ggf280-ZC4NU7z-bbJpOZb7CFn4VdJojdjziNCrE_ao37gp0lcHIaFPEw3ClFmdBhMCSnJy7IxFAWo8jwbHL0GwZW9Rjteq7v0f71GevwQsTdoD3L5QzFdJs7alZLW5U8TKGQG0PalYlLNZvH1Qv-6iCNc4FPpJJ5J6L3n4UuaRyJgBLdZIm92BU5p74JAAtvrrlJLTv0JsgH7ZnPjyTuZeg71ayVGibn_AfPDQj0Jg5p0YZLCK0SS7l9_vtVq1IhVwr2bLhnZp6EWjmKTvYptY-iX0Jr2yNnpPSP0JTVgdIXHNEMfKqAo3XCRU-D3x7OC3V0OTfaCsD3BLiYivLDPW_INWouNXblifs0JYzsq1ZmiPNLFgzjPnyBrntQgEReajuPd2D1Moa5Lgv_8uCJAfuzZeeQGO2EW_vQHjI1lyPNXLu2bfn9hpDFqmnVfMQFC8-YLGz2RxvWau0r1aBXzAH9pOgCA1TYOXxNZJ4Z57OypYKe-JkAlHdvLlJlfKaWOmT8OScieKDJRv-nAhkDHkhQ6fQACJ1hbVBBRZ4sh6kL6G--87w=w101-h199-s-no?authuser=0")
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