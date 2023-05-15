import streamlit as st
import os


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://th-thumbnailer.cdn-si-edu.com/ZLHme_2erCX4Pd_f3btzNT0bLl0=/1000x750/filters:no_upscale()/https://tf-cmsv2-photocontest-smithsonianmag-prod-approved.s3.amazonaws.com/e79de0fb-4dcb-4e10-b221-e5bad3aca8da.jpeg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:White; font-size:85px;"><strong>CWE :)</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Hmm what does this look like...I wonder :)</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> CWEEEEEEEEEEE my gosh hehe so fun :) we did sm tg :)</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> the playyy tooooo, this was fun monthy, hehe enjoy baby 💕💖💝</span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1. Hehe what time was it during our walky vid? X:XX <br> 2. How did i reigister for ittt what was thingy calleddd> ______ ______<br> 3. Did we volunteer? YEE/NAHH , if u no get this right smhhh ur not my niddo >:(<br>4. Hehe where did we sneaky kissy in the carnival ;) _____<br>5. Whereee we runnn awayyy tooo ______?:) <br> 6. Hehe what we watch tg in the grass :) _______? <br> 7. What video video did we get hehe ______  _____? <br>------PLAY TIMEEE------<br> 8. What color was i wearing hehe: _____?<br> 9. Hehe hmmm who wrote the play we watchyy __________?<br> 10. Did we actually watch it ;) YEP/NOPE? <br> 11. Who caught us doin hehehe ;) ________ (simple awnser) <br>12. What i give u on that day :) _____ ____ ______?</span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)
st.markdown("""
Add game here :)
    """)

box1 = st.text_input("1. Time hehe (ALL CAPS)")

if box1 == ('8:48'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correcto :) we stampyy it :) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2. Type a One-word awnser (ALL CAPS)")
if box2 == ('SIGNUP GENIUS'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> oh yess got it randomly fsfs ;)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3. Type a One-word awnser")
if box3 == ('NAHH'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> heh ;)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4. Type a One-word awnser (ALL CAPS)")
if box4 == ('BUSHES'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> i grabbed ur a- and woah. ;) We just too good tggg</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. Type a One-word awnser (ALL CAPS)")
if box5 == ('HILL'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">> the grassy :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box6 = st.text_input("6. Type a One-word awnser (ALL CAPS) ")
if box6 == ('SUNSET'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">hehe :) it soooo pretty 🧡  i love u :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box7 = st.text_input("7.  Type a Two-word awnser (ALL CAPS)")
if box7 == ('KISSY VID'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Heh correcto ofc first of many ;) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box8 = st.text_input("8. Type a One-word awnser (ALL CAPS)")
if box8 == ('GRAY'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> yes yes my collar heh :) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box9 = st.text_input("9. Type a ONEword awnser (ALL CAPS)")
if box9 == ('SHAKESPEARE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">yes this bozo monki smhhh</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box10 = st.text_input("10. Type a One-word awnser (ALL CAPS)")
if box10 == ('NOPE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">hehhhehehhe ;) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box11 = st.text_input("11. Type a One-word awnser (ALL CAPS)")
if box11 == ('TEACHER'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">whoopsies mb teach ;) u feel so good babe 😋 </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box12 = st.text_input("12. Type a Three-word awnser (ALL CAPS)")
if box12 == ('LITTLE RED HEART'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">tiny little gifto for u :) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

if box1 == '8:48' and box2 == 'SIGNUP GENIUS' and box3 == 'NAHH' and box4 == 'BUSHES' and box5 == 'HILL' and box6 == 'SUNSET' and box7 == 'KISSY VID' and box8 == 'GRAY' and box9 == 'SHAKESPEARE' and box10 == 'NOPE' and box11 == 'TEACHER' and box12 == 'LITTLE RED HEART':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:White; font-size: 30px;">finishhhhh :) carnival and play both ina month :) 💜 nowww: What SYMBOL in the middle of that 3d printy silver heart i give u hehe :) (baconian cipher heh)</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box13 = st.text_input("Final: Type the number out hehe with a smiley face (in Baconion Cipher) ")
    if box13 == ('ABAAA ABBAA AABAB ABAAA ABBAA BAABA BABBA BAAAB BABBA ABABB AAAAB ABBAB ABABA'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh moon palace :) Our place place :) Here ur hinty ;)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[Image Hint :)) :heart:]"
                     "https://lh3.googleusercontent.com/RoYqt5ZsRj7sns-tlTD7xL-10sEP6rySqmqPqknRLVEhXO1Iq9pm12vUSrV5LAmu6pbGGbweI-sqsqlXErUGHsNk-CsIev6QxR6z6M1zLMd83vuBYV4oCxApbBv2pcIhcZy9DnrAyIYeKsmpu1s4xNAgK4I7b--v1QlWl_cjQkIqaHrR9c209xjbReFoWUMl01JD6PIqPXuMLOGgrXURTmo4VSC8tcuDXoZrbqBEG1Kf2h31XG-8ZM31HPYqz4k8AfFxe7bcVnFgpQ9eTGuBueVP5fMWlZFq0g2fg5Ur8nZDAbHjVRNvzV-4k_aA5dvJIs4Ihr03Rk_V51a73rcr26yzHhawyyw3hrGbPPdmVW50IxvJoBd2YeN5e6PHkcGEZdjI4S2vtirT9T0wo_-kCEy5ci4GvGj0iurPOLnZ_oG7vYMhhNc9Cl3xsGKBFzcos5Nqd_rc1nYZKjTD3vLkkvwBW_7LC9uruRGlrJFAOywGYYmwXHtkIjfFGtPojsRA1jA3eeW3W33bXHCvvxtXWtzeApF4yfJwEsu--A5Wu08AgNT3oQY1bUXwO32KXC9ok8N8wytzkehorkWIKXWwhcd5enPCUfmHMRiCfJ8GDBT1W5U-B10spHQH2J6ZkTR6wOlnZBP3tRb2IYHS9MCfpnOnr5N-jlmUldkapDCRO1MZP_cX4NpiccTwlMDOoyoYKfwKhC6fcyPDalPc1BuB7b_Sq3Yh15mZka84l7MHN27hOc5ZFiL4DkHgyaN4yaPJbovw46gOP-QnRmViH_lMN7oGBI6Tne52hyp_t7OteFadsdGcZsvv6cPnOMC2LR12GIM5uvN1AP3Z2PcuiO8dfBWobj5iAV_xKDpnLBI_RInN48tIu4nOixDa3jWmpyMSRBXal47-jpdrxaq7wGRZvRyu2Wa26BCqX-6pOBfaRH6CmWLuMNtKVi4YeWd8fu2fGdXWdBsal-R-Q9-9qfu_9Q=w101-h199-s-no?authuser=0")
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