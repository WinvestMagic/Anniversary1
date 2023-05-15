import streamlit as st
import os


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://www.rd.com/wp-content/uploads/2020/01/GettyImages-1131335393-e1650030686687.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size:85px;"><strong>Travel Montho</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Ahh my travel monthh, i was on a planeee for so longgg</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> hehe oki u should have 2 images by noww, u start to see a pattern later later :heart:</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> U can do this my baby :) lmk if u need helpy hehe :) </span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1. Whereddd i travel firsty? ______<br> 2. What was the name of the city that i went to in portugal ______ <br> 3. lol what was in the background when i called u in the morningg ( my morning ur night) ________<br> 4. when i leaveeeee to travelll XX.XX.XXXX <br> 5. what day did i come backk XX.XX.XXXX ?<br> 6. what montho were we attt :) X? <br> 7. How many notes did i write for vacayyy in Julyy (X)  <br> 8. There was one more interesting note hehe and it was titleddd.....? ______  (space)  _______ :)) <br> </span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)
st.markdown("""
Add game here :)
    """)

box1 = st.text_input("1. Type a One-word awnser (ALL CAPS)")

if box1 == ('PORTUGAL'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">🤎Correcto :) yes yes very nicee walky placee</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2. Type a One-word awnser (ALL CAPS)")
if box2 == ('LISBON'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correctooo :) yuppyy hugeee babyyy</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3. Type a two-word awnser (ALL CAPS)")
if box3 == ('TENNIS COURTS'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">u j too good hehe :)))))) crazy :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4.Type a date hehe (MM.DD.YYYY) ")
if box4 == ('07.12.2022'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> bing bing i left then ;-; (Think of it as a synonm for Dark Blue) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. Type a date hehe (MM.DD.YYYY) ")
if box5 == ('07.22.2022'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>I BACK AYAYAY :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box6 = st.text_input("6.  Type a NUMBER (ALL CAPS) ")
if box6 == ('2'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">💘Hehe correcto :) 60 days down heh :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box7 = st.text_input("7. sPELL OUT  a NUMBER (ALL CAPS)")
if box7 == ('SIX'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correcto :) maybe we could change the "i" out ;))(Fruit--color?)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box8 = st.text_input("8. Type a two-word awnser (ALL CAPS) :) ")
if box8 == ('THE FUTURE :)'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">🤍Hehe correcto :) cant wait to builld it with u :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)


if box1 == 'PORTUGAL' and box2 == 'LISBON' and box3 == 'TENNIS COURTS' and box4 == '07.12.2022' and box5 == '07.22.2022' and box6 == '2' and box7 == 'SIX' and box8 == 'THE FUTURE :)':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 30px;">yayayyay ez finsihh nowww Which airplane did i tell u that token was hehe?</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box11 = st.text_input("Gotta listen smhhh")
    if box11 == ('AIRBUS A320'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh :) i love you baby :)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[hehe i came back >:) :heart:]"
                     "https://lh3.googleusercontent.com/VvPidt3Dpal29pK1xh4k3A3CwJ5VM0xD1T4_N5cYLjuqzByAnklLs9uZBLS0xx4k0HWSuBXZnOJZou0nE3tv4FwOIahY0iXuOyonMQGVigR3tdzxSewTyVEXeaXAwE5bvoLSCXDEClnpq_ZEGNtYIEZ3-1x17fNqwHgo7VYVXGmrKKB0srpgd69oDFAOeOTETnSQejkY8wNA1EeoNySNPVJpq9IyAJCD89HCCMtdh0wGI-8VqgEN7G0Ub_a-bQuvqyU1Dd7OUI82UCywzQVja0Y2TbznFvT7tfVrurMYFbkDaIag_3XYSPtNv8UDvemGItuDiAGY9eavSrW7wbwvcLK1nBWIQqTmUNTgOsbzV4NEqlPeAz-wp5Tw9vHd1TgJ3GngWpkr8760RK3XLXBc7BkeOg0-a1qZjpNKlQnko9EMHtHbrTKszHNaAWGBVeiSRGwJhdgYJobzBQMIGa2wql-gnX65D9Tl9xssyKFXh8JPlBp45pOdM_1jYppRv4pkN5zxKDm3WYapo7xyq6rwKPRbjo_DvDg6ga8bnWZ2DbFg37lfFj2yo9NIup4PtdZs8kooX6cN80nrc0DCrEx4FzhovCoT0UVen0HT_7vX-SMGsd4nWjxdru-6W0zoEM8Sh1AZ4BgBTymhwC4ZRAE7awQvCKAeeWjIt17d6aF3u_6dh94nJCNIMg3BauoLqSSyG0EaHvqw6a7KT27yBifzIP9O4dmxWEih5XN9fxipk_Muqbtn1Y2MCA7OYfjg2AQk55JF4twEX62hCi57y2XvrUZKashuSq5TMIroqvdQTqhXifU1Wp_xpaL9zlnoFFCgr5zYHSw4HXCS_lJ6GpyI8FIfewSN8sAbV90Ny0L5re0nPsmd3Vv5-zQ4PqtBlL25Dxe0ZmXeATrgCuWNbJIGEYOQv3EUHt2fMlnHqOKi8GJg2VYHYmYUGXAbhJB1CAFF84hshj6MfKXeLAqUC59F1A=w101-h199-s-no?authuser=0")
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