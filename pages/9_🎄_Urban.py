import streamlit as st
import os


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://piratediffusion1.s3.amazonaws.com/renders2/XG5kpY/00001-v-pro-v6035149.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:White; font-size:85px;"><strong>Urban ;)</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> hehe OUR urbannnnn :))))))</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> hehe 2 day expereicneee :) DId eveyrthing hehe heree :) I even got to lay on ur lappy :)</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000">So much 🥰 hehe have fun :)</span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1. Ahh hehe what gamere we played that night with all naachy ppl ____ _________<br> 2. Lol what test we takey ;) ___ ____ ___ <br> 3. What score we get heh ;) XX <br>4. Hmm hmm hehe what did we very much find in urban ;)  ____ ________<br>5. Ahh hehe whatd did i release in ykykyk where 👀👀👀 _____ _______?<br> 6.Ahh hebe what were we watching the first dayy u camee (sunday) ______ <br> 7.What we switch with each other hehe :) _______ <br> 8. Hmm hmm whereee we goo to eatt or more so huggie 🥰 ______<br>  9. Hehe which ppl in the double couples pic :) K____ , N____ , A___ , H___<br> 10. what what made me blush babe __ _______ (what would i call it heh) <br> 11. 11. ahh hehe what songgg u teachy mee and we do tggg ____ ______ <br>12. who popped up during urban found mee ;-; ____ ___________</span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)

st.markdown("""
    """)


box1 = st.text_input("1. 2 words hehe (ALL CAPS)")

if box1 == ('PHOTO ROULETTE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correcto :) - very susssy heh </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2. Type a three-word awnser (ALL CAPS)")
if box2 == ('RICE PURITY TEST'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">ooop very inetsting that there a test..</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3. Type a NUMERO awnser")
if box3 == ('84'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> correctooo heh ;)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4. Type a double-word awnser (ALL CAPS)")
if box4 == ('FAMILY RESTROOM'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> ;) had some fun heh...💝</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. Type a twooe-word awnser (ALL CAPS)")
if box5 == ('CHILD POTION'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>lol only u could ;)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box6 = st.text_input("6. Type a One-word awnser (ALL CAPS) ")
if box6 == ('SOCCER'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">yess argentina wonnnnnn 🎉🎉🎉</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box7 = st.text_input("7.  Type a ONEE-word awnser (ALL CAPS)")
if box7 == ('JACKETS'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">ur so comfyyy🥰🥰🥰... still mine >:( </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box8 = st.text_input("8. Type a One-word awnser (no apostreophre) (ALL CAPS)")
if box8 == ('WENDYS'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">huggie uuuu.. and some more ;) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box9 = st.text_input("9. Type a four word awnser. no spaces (ALL CAPS)")
if box9 == ('KRISH,NIDHI,ADITI,HIRSH'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">lol yes this picutre soo nicee :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box10 = st.text_input("10. Type a TWO-word awnser (ALL CAPS)")
if box10 == ('UR THINGY'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heh....goddamn.</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box11 = st.text_input("11. Type a TWO-word awnser (ALL CAPS)")
if box11 == ('MORNI BANKE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">so fun to do with u baby :) 💗  </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box12 = st.text_input("12. Type a twooo-word awnser (ALL CAPS)")
if box12 == ('MY MOTHER'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">ofc lol ;-;  </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

if box1 == 'PHOTO ROULETTE' and box2 == 'RICE PURITY TEST' and box3 == '84' and box4 == 'FAMILY RESTROOM' and box5 == 'CHILD POTION' and box6 == 'SOCCER' and box7 == 'JACKETS' and box8 == 'WENDYS' and box9 == 'KRISH,NIDHI,ADITI,HIRSH' and box10 == 'UR THINGY' and box11 == 'MORNI BANKE' and box12 == 'MY MOTHER':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:White; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:White; font-size: 30px;">finishhhhh :) hehehheh yay :)Whats that thingy on that little figure mans head called heh :) (SHIFT CIPHER)</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box13 = st.text_input("Final: Type the number out hehe with a smiley face (in SHIFTT Cipher) ")
    if box13 == ('UPQ JCV'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh moon palace :) Our place place :) Here ur hinty ;)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[Image Hint :)) :heart:]"
                     "https://lh3.googleusercontent.com/apw4t5nE_Jxd_oNNDJRlrg22PFuKK8Hd00q7EyDTrPXpohNDwJFGKL-XYyd0tQX3kPZNX3py0S9P2___rXdJiqc7VxCLA4lB9mzk97ogNvxIQfjTcsYWE-665juqRHDzRq9G-_n5xLNzVC9G21d11znE3gZx-SmPNrUOVv4RMcNXBOwdts8WkLWUrW4NxmVZFchbmrmfIfaKocytqDDTjTvLnTOP2g73cY-5uG6QYE9oF7zXfNtB5UuaRLn_ETsAvsLx9VuqVEWprVaGT8dEXabop773Cz1sVipAtehsMqmqPGK0VivKOj9xfVY3GXU8sqAAexIkkz-y9EzkRayB-0XPx3GcjQFMqttSwQO8eSHzZMKhXFDA4e4hiLncWMbxKXKM8LokgcXefm_pH0qYdHjMvIJBPp-HvqUk7lldJrT7RAv1Y_KeYVwSANG0ZmBDHhrvc83pmZ4DfAPL-V__1FENP4wTcXXXJwS-RzXuHlbawhp3caPf8ZCrSXw6-lmbpv98Za3c2SLI94gQYYa0HSCQGVFZNF3B3P8wysSJ4A7VS832iwExk7T-CH-O7Sb44kdjilRoiLeWqADc8hYbeXx4RC1_zBJ67wKlyMcgWAG2c7y10ME1tudf3hth1BDCGUp-fhg5i4P5Q16cixclVQyHLwPXIodd1bEWdLPCmWOewmwfOI5P8kxL7K7uvg1ORhYC3lTl6KA37KyEx7_YY6-Q8djm3Qi7FKbcX_hlEMgy1uCw1_UuPvNCfa-YSlyo3XO9mOdrMDyZj7YzlmjovxD0aGfbegdjBgmijUKstLzKtWiPkoDazr-3OdO5owORn91Meb236UnQr-SG6Td6nMRnd9nU_Ygh-wdSLyICDH9cVMgx5CbgPYzeiJzv4IBd-Wnry64ApdaP221tPXYaGLBu9QA1Gc6CvNoRheqD3uyJIzEsp1OduOJ0ObJWDTog4xuLPqIW6nGfMVaGpJHawg=w101-h199-s-no?authuser=0")
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