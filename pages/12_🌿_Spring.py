import os
import streamlit as st


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://cache.desktopnexus.com/thumbseg/2361/2361269-bigthumbnail.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

original_title = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:White; font-size:85px;"><strong>Spring Time</strong></p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Pretty timeee :)</span></p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Almosttt thereeee ahh marchy and apirl :heart:</span></p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
original_title1000 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Lavender; font-size: 20px;"><span style="background-color:#000000"> Nicey monthos :) -  U got this :) too ez :)</span></p></em><b>'
st.markdown(original_title1000, unsafe_allow_html=True)
original_title101 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 20px;"><span style="background-color:#FFFFFF">1. What day did i go got compsss which days? XX.XX.XXXX AND XX.XX.XXXX <br> 2. Hmm hmm u had ur surgery during this weeeekend _______ ________ <br> 3. Lol hehe what color shirt were u wearing when u sent me that snap with ur cast and hugey shirt ______<br>4. What time our last call of March starttt :) XX.XX.XXXX<br> 5. Lol hehe what essay did u help me writey cutie u amazing _______<br> 6. dateee when u saw meee fianlly XX.XX.XXXX<br> 7.How muchy days was i gone for TSA? X<br></span></p></em><b>'
st.markdown(original_title101, unsafe_allow_html=True)
st.markdown("""

    """)

box1 = st.text_input("1. Type a dATES awnser (ALL CAPS)")

if box1 == ('03.25.2023 AND 03.26.2023'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correcto :) thosee were the datess</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2. Type a One-word awnser (ALL CAPS)")
if box2 == ('SPRING BREAK'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">🧡Correctooo :)) ahh hehe yeahh u got it done :) slingy noww</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input("3. Type a One-word awnser (ALL CAPS)")
if box3 == ('GREEN'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">lol u looky like my goofy baby :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4. 4 words - seperate with commas (in order) - Locations (ALL CAPS) (W,X,Y,Z)")
if box4 == ('03.30.2023'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> yesssy yes 🥰 </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5. Type a NUMBERSS hehe (MM/DD/YYYY) ")
if box5 == ('HAMLET'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>me and him dont vibe bruh u j too smartie 💜</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box6 = st.text_input("5. Type a date hehe (MM/DD/YYYY) ")
if box6 == ('04.08.2022'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">>Miller miller :) 💕</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box7 = st.text_input("5. Type a Number hehe (MM/DD/YYYY) ")
if box7 == ('4'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">me wenty for this trippy tooo </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

if box1 == '03.25.2023 AND 03.26.2023' and box2 == 'SPRING BREAK' and box3 == 'GREEN' and box4 == '03.30.2023' and box5 == 'HAMLET' and box6 == '04.08.2022' and box7 == '4':
    original_title12 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 30px;">DOPNE DONEENODENOENNENE (MONO-ALPHABETIC) this time hehe just stright into the smthh silver? what did i give u?</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box11 = st.text_input("Final:What we putting hereehrherher")
    if box11 == ('YSGVTK'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh :) i love you baby :)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[We aer for life :heart:]"
                     "https://lh3.googleusercontent.com/ydINioInP4qGCwWQTSoqcQKMzYQXIuXLN9zIbEPSsZxYBqMs-Dgj7glP2_cRnT-fJfvqRJOTzv00OEsmPnKcvL0NfL9VWKWoGDKp1SqcgRA3TQJ5Stl_O9CjRQIzLwUjOP5Hu_csU3YKDuaiGu5fLMfFFU9Xs1kptZDIuKLJCC8ImQERSJSkEj_aQ3uKULIcMvJ4u_bHPccn-REaxAjRxvsY83bZyh2ssl4uScRdJm5D4NtmIW2WADIJipQCnYUnW8JDkM1THx_M6_O2lam4YfTDuzR__XFMfWgHFgjyBuf_g51mdBc3_qLRU3UzxQJnEz8PcCLVRpQWhx64oBuLDCBSXfKTeykO8fgpBYjCILT8CEH76sVxp7aPbnmpcfcxyM0qit2XEac3jf0PIRNI4t66I1gA693_yYJyZ0RS0lG3oKRrn9HzaQPzgi_9BqTUaSpBvzJgkqaZfmWSHGFrqWEulOb9UE_LKuvdI1HNo1-SUZAftr9ubmGcwo-eWA-MOE7CcHGbXNYseq_i4RdgMY8MDQClOuXlR6lHDunn0BOmjdczuxcfSfG0CVUmFsnQ9RvHpetvhuBBF8HVqBNw4YDGDyIWXjDDRdD9yb4_mrJnMRbw5r-GJndIQC0t_xAayvLAg5DkY9-KwiN2HfxtNnraGraRJne19rC6qSG9hB8DSlzuDrAMYzXiV68075qynZf4XnbfT87IoY2kKTyFHA7wV_8GknfJZSG4oVhzJjkpmUHYPawk8fhM-62NDdtNsrKXZ4AcA_y-A4zCgmlc_XSfN___qK4P8EdK-E-qd3uLWheGZ1z_Fwq83p-nttCGewmptED3CfooL2vNmzKzxyQYeZlKV7N6nOQRxwCYRX880DAbUuLwFx0tKz28xXYZ8P9_rD6jdNgm8de8a0RMpBb21s3tpzB8lKQymtD7T8S_OHG-Yiowh78qTdnZ0VjOm-DNn4EozFFTIrxXsSbuMg=w101-h199-s-no?authuser=0")
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