import streamlit as st
import os


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://piratediffusion1.s3.amazonaws.com/renders2/XZR22G/00001-r-pro-lsabv.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size:85px;"><strong>Naachy Reunion :)</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Hmm what does this look like...I wonder :)</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> OKi so save those imagesss, and what i need u to doo is open one of those grind layouts thats a 4 x 3 - incase u no guessed it there gonna be 12 images. ur job is to rearrage baby :)</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000">save the images hehe, anddd youll get it :) </span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1. What day was workshopppyyy dayyy? XX.XX.XXXX <br> 2. hehe first day i got a huggo again 🥰? XX.XX.XXXX <br> 3. What song we started learnning during this monthh ______<br> 4. Anddd what day we find out there oppurtunity for beuomontt? XX.XX.XXXX<br> 5.What day did we find out beaumont was confirmed :) XX.XX.XXXX?<br> 6. What coloreoes es my naacho tshirt heh ______? <br> </span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)


st.markdown("""
Add game here :)
    """)

box1 = st.text_input("1. Type a One-word awnser (ALL CAPS)")

if box1 == ('08.03.2022'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Veryyy niceee :)) me was back :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2. Type a One-word awnser (ALL CAPS)")
if box2 == ('08.03.2022'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">💖💖💖 makey me feel so comfortable :)/span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3. Type a two-word awnser (ALL CAPS)")
if box3 == ('JI HUZOOR'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">yes yessss correctooo :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4.Type a date hehe (MM.DD.YYYY) ")
if box4 == ('08.04.2022'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Bro  ltiearlly the day after heh 💗(Think of it as a synonm for Dark Blue) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. Type a date hehe (MM.DD.YYYY) ")
if box5 == ('08.11.2022'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>We had sm fun :) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box6 = st.text_input("6.  Type a NUMBER (ALL CAPS) ")
if box6 == ('ORANGE'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">💘Hehe correcto :) inetersting coloress</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)



if box1 == '08.03.2022' and box2 == '08.03.2022' and box3 == 'JI HUZOOR' and box4 == '08.04.2022' and box5 == '08.11.2022' and box6 == 'ORANGE':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 30px;">yayayyay good jobby nowww hehe what ____ gem is on that wrong (encrpyt in pigpen cipher heh)?</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box11 = st.text_input("lookly closelyyy")
    if box11 == ('char(80)char(85)char(82)char(80)char(76)char(69)   char(71)char(69)char(77)'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh :) i love you baby :)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[hehe i love u so much :) :heart:]"
                     "https://lh3.googleusercontent.com/CccuItTScjAf--66hIxb5XVW6AE-LzPQSgy_R68judTiQ3rjOdTTKdPmhsipQTt1aIyS7TfsbQXrUkoDpmVfeufSJUucelruhwcNPfgauwbXLZUSJaI-QmJ1gU9iggTOfA6LZ0Mvtn0Eh-1B5WsMjIYSSdWKDm6NZGgHYvZrUrMvQXLheY9ZsK08WteSKibrh3Iyi0pb0asCpcyilgjS6t2EPxdS_HSf32CMRkN5l_FhfcB7GARtiQWp9ZWSdt4o7h9wthOde1elR27YFleIUFNEwTH074G7veQxfShiFWWPUDc37l-_oTkrvbqzBkX9G2zgEkY1h_aF55_xF-5tWACp6devhAFtmLdkeQE3LCdZ2MTNjNrEvtRG7p8tZARJnyIEdmczpROWS1TiZxLzOgV61He-Qk-i6HADE7aDoUkztt5zixMsyM63bdLpW-6lSNslHGAg_F_7dc8lkB7gqymb4UV2W9vnEjGgcFNBaut0NezGphGVFAdxlCYhANkQaIMal9ytAcln_YN9nQnqGKA8l9IEtPwgNaNAmrf05Ip_2YqFxmxoJh57A4vNRUw0gXr3e-JyuXfe02KLP5MJrMOmGnfaE4LlQPfvUmeEDL2g9pQepyUk-BHIXsMmzSuqVP-YbH3qBzmUVQOHrrif6Mwrk9t9dqMvc5M--5BMyde8sZSHJPTZs-40MeNz6tk8EnwP__sDLNsaAeRRSnwArq19_B9dj4Hor6phYil483ZIwoSkZgjAgxpxxsxEWW0WQ0yMzDpp2L_Es2h87JENHaOv230nA6oTh3OLFgbfvFrrdhlUwKyUUInTgGutfDZ0r91zH5eEJUK3tdyHF4eqm9FOfGQYCrG4jqllUysc--eVa6d9hn2wZE-ltF_lWHDYmZ9E0zjVFI3J3l_c0qrmrAKlaRmIJohp_oKTa-alTBS41h5arCJk9Z065C_HoyXxUdbwkqTvzgPbklSc2GjH9Q=w101-h199-s-no?authuser=0")
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