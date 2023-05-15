import streamlit as st
import os


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://prod-be-moon-brand.s3.amazonaws.com/mps_Aerial_Pool_1_b8c745821f.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size:85px;"><strong>Moon Palace!</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Hehe babyyy lookooo our place right outside :)</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Hehehe so listen carefully, that imageee u got on the last pagee, u needa save thatt u still  gonna be playing an escape rooom :)) Ofc ofc its digitall so rip, but it wont stop meee :heart:</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Gotta warn you though baby this is gonna be a lot harder then the other ones ;) , and only gonna keeep getting harderrr, save the images! </span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)

original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1. What colorr was i wearing the first time u saww meeee in cancun :)  _____<br>2. Whats the first thing we did to start off second day :) ______ <br> 3. When we get in the pool tg hehe ;) Day X)<br> 4. Whats the gamee we set the highscore on tgg in wired? <br> 5. What was something delicious we ate in wired? :) _______ ____ ___________ ?<br> 6. Where wereee we going when we had our first kiss :) ______? <br> 7. Which waterpark we take our little detour ;) ______ <br> 8.  Where are parents goo when we went to wired heh ;) _____<br> 9. Hmmm lol which two parents kept sneaking up on us? very sussssy unexpected heh _____(s)<br> 10.  And finally finally, heh, what was the one place out of allll of ittttt ever ever ever, that oneeee place, where i realized that u were the girl i wanted to marry :) ____ </span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)
st.markdown("""
    """)

box1 = st.text_input("1. Type a One-word awnser (ALL CAPS)")

if box1 == ('BLACK'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correcto :) i need new colors ;-;</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2. Type a One-word awnser (ALL CAPS)")
if box2 == ('SUNRISE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">hehe it was so early shinyy :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3. Type a One-word awnser + Number of day (ALL CAPS) ")
if box3 == ('DAY 2'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Say lesssss heh ;)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4. Type a One-word awnser (ALL CAPS)")
if box4 == ('BASKETBALL'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> correcto :)) We just too good tggg 🌹</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. Type a 3-word awnser and spaces (ALL CAPS)")
if box5 == ('ORANGE ICE CREAM'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>yummy yum yum 😋 correct :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box6 = st.text_input("6. Type a One-word awnser (ALL CAPS) ")
if box6 == ('GRAND'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">💘gosh hehe :)  i love u :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box7 = st.text_input("7. Type a One-word awnser (ALL CAPS)")
if box7 == ('NIZUC'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Heh correcto , we took all the detours heh ;) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box8 = st.text_input("8. Type a One-word awnser (ALL CAPS)")
if box8 == ('CLUB'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">❣Hehe they went and partied and we did smth else ;) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box9 = st.text_input("9. Type a One-word awnser (ALL CAPS) include the '(s)' at the enddd")
if box9 == ('DADA(s)'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Theyyy ninjas im telinjggg uuu< (no cap no cap)/span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box10 = st.text_input("10. Type a One-word awnser (ALL CAPS) I love this place 🥰")
if box10 == ('AGRA'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Hehe this one gonna remain forever in my heart :) 💗 </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

if box1 == 'BLACK' and box2 == 'SUNRISE' and box3 == 'DAY 2' and box4 == 'BASKETBALL' and box5 == 'ORANGE ICE CREAM' and box6 == 'GRAND' and box7 == 'NIZUC' and box8 == 'CLUB' and box9 == 'DADA(s)' and box10 == 'AGRA':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 30px;">hehe u finish :) ahh cancun was amazing 💜 nowww: How many stars are on that little moon i gave u :)</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box11 = st.text_input("Final: Type the number out hehe with a smiley face (in Atbash Cipher) ")
    if box11 == ('ULFI :)'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh moon palace :) Our place place :) Here ur hinty ;)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[Image Hint :)) :heart:]"
                     "https://lh3.googleusercontent.com/SJUU1FE6Ro90FX0qqCoGXzlq1ZUh2T6cspfFZEFEIygZAlQ0wAfwh1KHPkY7gS7L9RhqEO6hKz-B_tcHV7pQ1Oj3lwWlQAIfkZBOR6kTvLzFsH2tXKQmwiGvUtrAulut3uRJ56QDp5CZqfViQM8eWssDkoBmU92XJtIHb22gjmszUGRx92FMNDJEEnvBy-AOnsBH97iYLWfyWRe0HfHTKcINuMXAkocHNY8DTkaKHBxabrr9LC-o9j0RMSFkfsrymOW8qSsLPbFDOZ7ceFOwtlOPrfqz5u91GFFHj-Uvo38D6GR8GdjBgJWVB5k1z3T_FBj6GsKHyrAFEzVPVuqMQXj4ayBv2UXt8HWz8FshIrnDJzZyx4Or-wK4NbRCtYbyJu-khpG9SXp-yMdCiocwrwhNztK6teS1CcrN6mI7iBgchpeq280_CFw_N1phzwJ2P2QGlyzMcd1WbQasFrFVjim-nRgildj5Nic-rl89sHjTm7oDYC5NxC6e7xDMDOrbLoaVKs866ya0lHyt2pmR-msMBuf30HUAW88w4nN4byJ2-JbuuPIooWhku81YKd9FCbChCD9WH0EDaf17cRjChFGw81aPd9YZd2UbnypLiF8tjeuOsjMx6dsJzbYbNSfPiYMoJ6UwtInbUFVClNxLpOMNr0JdM-Nru4Ry-E3eysBqLvzsHUy4G0xe5HQiYXirFr89X605oU1v8bIPHTa1zWbaPwWu6NwqKUQ3iqUAs9vvI81H14BlZcun6aaVUF5DiW4Ime5yUtUgtM9yRZkIYh4pwdw7LoUM09ITF9HE9G7bn1VEWmUvXY-PLzybCwMt12A_MGg3aezzPLdmWT7wActgYpkK7l-K8QuqJpgI7Vb0Sxd05x3ljOzsEviEYC8NLbbzVbqVzE-YgWnX6piN0JFnVCfcpSSifm1ZlxglX57Sy5OyO_YR8rgAF0sNla-4SbnJo_YTUbH6LAPL7Xn_Mw=w101-h199-s-no?authuser=0")
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