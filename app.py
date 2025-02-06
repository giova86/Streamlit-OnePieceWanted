import streamlit as st
from streamlit_cropperjs import st_cropperjs
from PIL import Image, ImageDraw, ImageFont
import io
import os
import base64

from wantedposter.wantedposter import (
    WantedPoster,
    VerticalAlignment,
    HorizontalAlignment,
    CaptureCondition,
    Stamp,
    Effect,
)

@st.cache_data(ttl=3600)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def support_icon(
        local_img_path_button,

        local_img_path_telegram,
        target_url_telegram,

        local_img_path_wahtsapp,
        target_url_whatsapp,

        local_img_path_mail,
        target_url_mail
):
    img_format_button = os.path.splitext(local_img_path_button)[-1].replace('.', '')
    bin_str_button = get_base64_of_bin_file(local_img_path_button)

    img_format_telegram = os.path.splitext(local_img_path_telegram)[-1].replace('.', '')
    bin_str_telegram = get_base64_of_bin_file(local_img_path_telegram)
    img_format_whatsapp = os.path.splitext(local_img_path_wahtsapp)[-1].replace('.', '')
    bin_str_whatsapp = get_base64_of_bin_file(local_img_path_wahtsapp)
    img_format_mail = os.path.splitext(local_img_path_mail)[-1].replace('.', '')
    bin_str_mail = get_base64_of_bin_file(local_img_path_mail)

    html_code = f'''
            <style>
                #menuToggle {{
                      display: block;
                      position: fixed;
                      bottom:30px;
                      left:30px;
                      z-index: 1;
                      -webkit-user-select: none;
                      user-select: none;
                }}
                # @media (orientation: portrait) {{
                #         #menuToggle {{
                #             bottom:100px;
                #         }}
                # }}
                # @supports (-webkit-appearance: none) and (not (overflow:-webkit-marquee)) {{
                #         #menuToggle {{
                #             bottom:97px;
                #         }}
                # }}
                #menuToggle a {{
                    text-decoration: none;
                    color: white;
                    transition: color 0.3s ease;
                }}
                #menuToggle a:hover {{
                    color: rgb(236,194,12);
                }}
                #menuToggle input {{
                    display: block;
                    width: 65px;
                    height: 65px;
                    position: absolute;
                    top: -7px;
                    left: -5px;
                    cursor: pointer;
                    opacity: 0; /* hide this */
                    z-index: 2; /* and place it over the hamburger */
                    -webkit-touch-callout: none;
                }}
                #menuToggle .float2 {{
                    display: block;
                    width: 33px;
                    height: 4px;
                    margin-bottom: 5px;
                    position: relative;
                    background: rgb(26,34,44);
                    border-radius: 3px;
                    z-index: 1;
                    transform-origin: 4px 0px;
                    transition: transform 0.5s cubic-bezier(0.77,0.2,0.05,1.0),
                              background 0.5s cubic-bezier(0.77,0.2,0.05,1.0),
                              opacity 0.55s ease;
                }}
                #menuToggle .float:first-child {{
                    transform-origin: 0% 0%;
                }}
                #menuToggle .float:nth-last-child(2) {{
                    transform-origin: 0% 100%;
                }}
                #menuToggle input:checked ~ span {{
                    opacity: 1;
                    transform: rotate(45deg) translate(-2px, -1px);
                    background: white;
                }}
                #menuToggle input:checked ~ span:nth-last-child(3) {{
                    opacity: 0;
                    transform: rotate(0deg) scale(0.2, 0.2);
                }}
                #menuToggle input:checked ~ span:nth-last-child(2) {{
                    transform: rotate(-45deg) translate(0, -1px);
                }}
                #menu {{
                display: flex;
                    flex-direction: row;
                    justify-content: flex-end;
                    align-items: center;
                    border-bottom-right-radius: 55px;
                    border-top-right-radius: 55px;
                    position: absolute;
                    width: 400px;
                    margin: -90px 0 0 -50px;
                    padding: 20px;
                    # padding-top: 125px;
                    background: rgb(26,34,44);
                    list-style-type: none;
                    -webkit-font-smoothing: antialiased;
                    /* to stop flickering of text in safari */
                    transform-origin: 0% 0%;
                    transform: translate(-100%, 0);
                    transition: transform 0.5s cubic-bezier(0.77,0.2,0.05,1.0);
                    }}

                #menu li
                {{
                    padding: 10px 0;
                    font-size: 22px;
                }}
                #menuToggle input:checked ~ ul {{
                    transform: none;
                }}

                .box_keywords {{
                    display: none;
                }}

                #menuToggle .float {{
                    # position:fixed;
                    width:65px;
                    height:65px;
                    # bottom:20px;
                    # left:20px;
                    background-color:#2d78c9;
                    color:#FFF;
                    border-radius:50px;
                    text-align:center;
                    box-shadow: 2px 2px 3px rgb(0 0 0 / 0.2);
                    # transition: transform .2s; /* Animation */
                    margin-left: 20px;
                }}

                #menuToggle .float2 {{
                    # position:fixed;
                    width:65px;
                    height:65px;
                    # bottom:20px;
                    # left:20px;
                    background-color:#2d78c9;
                    color:#FFF;
                    border-radius:50px;
                    text-align:center;
                    box-shadow: 0px 0px 14px rgb(0 0 0 / 0.92);
                    # transition: transform .2s; /* Animation */
                }}

                .float:hover {{
                    background-color:#ffffff;
                }}

                .float img {{
                    width: 55px;
                    height: 55px;
                    margin-top:5px;
                }}
            </style>


            <nav role="navigation">
                <div id="menuToggle">
                    <input type="checkbox" />
                        <img src="data:image/{img_format_button};base64,{bin_str_button}" class="float2"/>
                        <ul id="menu">
                                <a href="https://t.me/thegiova" target="_blank" class="float">
                                <img src="data:image/{img_format_telegram};base64,{bin_str_telegram}" />
                                </a>
                                <a href="https://api.whatsapp.com/send?phone=3494346732&text=Ciao,%20sono%20interessato%20ai%20vostri%20prodotti." target="_blank" class="float">
                                <img src="data:image/{img_format_whatsapp};base64,{bin_str_whatsapp}" />
                                </a>
                                <a href="{target_url_mail}" class="float">
                                <img src="data:image/{img_format_mail};base64,{bin_str_mail}" />
                                </a>
                        </ul>
                </div>
            </nav>

            '''
    return html_code



# --- page configuration ---
st.set_page_config(
    page_title="One Buonty",
    # page_icon="..",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://giovanni.bocchi.com',
        'Report a bug': "https://giovanni.bocchi.com",
        'About': "# Giovanni Bocchi"
    }
)

st.write('')
st.write('')
st.image('static/cappello.png')
st.write('')

# --- contact ---
st.markdown(
    """
    <style>
    # .st-cj {
    #     width: 150%
    # }
    html, body, h1, h2, h3, h4, .streamlit-title, .streamlit-header, [class*="css"] {
        font-family: -apple-system, system-ui, system-ui, "Segoe UI", Roboto, "Helvetica Neue", "Fira Sans", Ubuntu, Oxygen, "Oxygen Sans", Cantarell,
        "Droid Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Lucida Grande", Helvetica, Arial, sans-serif;
    }
    .css-10trblm {
        font-family: -apple-system, system-ui, system-ui, "Segoe UI", Roboto, "Helvetica Neue", "Fira Sans", Ubuntu, Oxygen, "Oxygen Sans", Cantarell,
        "Droid Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Lucida Grande", Helvetica, Arial, sans-serif;;
        color: black;
    }
    #MainMenu {
        visibility: hidden;
    }
    header {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
        height: 0%;
    }
    button[title="View fullscreen"]{
        visibility: hidden;
    }

    .css-1vq4p4l {
        padding-top: 40px;
        padding-left: 40px;
        padding-right: 40px
    }
    h3 {
        color:grey ;
    }
    # .css-1o1ni74 li {
    #     margin-left: 40px;
    # }
    .css-1va15fh {
        background: hsla(0, 0%, 0%, 0) !important;
        border:2px dotted lightgrey !important
    }
    .modebar{
          display: none !important;
    }
    .css-i1t8mj {
        visibility: hidden;
    }
    .block-container {
        max-width: 1200px;
        padding-top: 10px;
        # padding-right: 50px;
        # padding-left: 50px;
        padding-bottom: 80px;

    }
    .css-18ni7ap{
        background-color: hsla(0, 0%, 0%, 0) !important;
    }

    h2 {
        color:#E05C100 ;
    }
    .css-1o1ni74 li {
        margin-left: 40px;
    }
    .css-1va15fh {
        background: hsla(0, 0%, 0%, 0) !important;
        border:2px dotted lightgrey !important
    }
    .modebar{
          display: none !important;
    }
    .css-i1t8mj {
        visibility: hidden;
    }

    .css-18ni7ap{
        background-color: hsla(0, 0%, 0%, 0) !important;
    }

    .element-container.css-1im970p.e1tzin5v3 {
        width: 100%
    }
    .steDownloadButton {
        # background-color: rgb(19, 23, 32) !important;
        color: grey !important;
        border-color: rgb(65, 67, 75) !important;
    }
    .steDownloadButton:hover {
        # background-color: rgb(19, 23, 32) !important;
        color: rgb(252,50,59) !important;
        border-color: rgb(252,50,59) !important;
    }
    .steDownloadButton:active {
        background-color: rgb(252,50,59) !important;
        color: white !important;
        border-color: rgb(252,50,59) !important;
    }
    section[tabindex="0"] {
        overflow-x: hidden;
        # overflow-y: hidden;
    }
    section[tabindex="-1"] {
        overflow-x: hidden;
        # overflow-y: hidden;
    }
    footer{
        visibility: hidden;
            position: relative;
    }
    .viewerBadge_container__1QSob{
        visibility: hidden;
    }
    #MainMenu{
        visibility: hidden;
    }

    section[tabindex="0"] {
        overflow-x: hidden !important;
        # overflow-y: hidden;
    }

    .steDownloadButton {
        display: inline-block !important;
        width: 100% !important;
        text-align: center !important;
        border-top-color: rgba(49, 51, 63, 0.2)!important;
        border-right-color: rgba(49, 51, 63, 0.2)!important;
        border-bottom-color: rgba(49, 51, 63, 0.2)!important;
        border-left-color: rgba(49, 51, 63, 0.2)!important;
        border-radius: 0.5rem !important;
        color: black !important;
    }
    """,
    unsafe_allow_html=True)

# Funzione per convertire l'immagine in formato bytes
def pil_image_to_bytes(image: Image.Image, format='PNG') -> bytes:
    if image is None:
        raise ValueError("L'immagine non è stata generata correttamente!")

    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format=format)
    img_byte_array.seek(0)
    return img_byte_array.read()


file_uploaded = st.file_uploader(
    "Select the image to use as portrait", type=["png", "jpg", "jpeg"]
)

cols = st.columns(3)
with cols[0]:
    first_name = st.text_input("Name")
with cols[1]:
    bounty = st.number_input("Bounty", step=1)
with cols[2]:
    capture_condition_map = {
        "Dead or Alive": CaptureCondition.DEAD_OR_ALIVE,
        "Only Dead": CaptureCondition.ONLY_DEAD,
        "Only Alive": CaptureCondition.ONLY_ALIVE,
    }

    capture_condition_str = st.selectbox(
        "Capture condition", options=capture_condition_map.keys()
    )
    capture_condition = capture_condition_map[capture_condition_str]

filter = st.slider("Filter percentage (optimal value is 21)", 0, 100, 21)

# # Effect
# effect_map = {
#     "Frost": Effect.FROST,
#     "Lightning": Effect.LIGHTNING,
# }
#
# effects_list = st.multiselect("Effects", options=effect_map.keys())
# effects_selected = [effect_map[effect] for effect in effects_list]

# Stamp
# stamp_map = {
#     "None": None,
#     "Warlord": Stamp.WARLORD,
#     "Do not engage": Stamp.DO_NOT_ENGAGE,
#     "Flee on sight": Stamp.FLEE_ON_SIGHT,
# }
#
# stamp_str = st.radio("Stamp", options=stamp_map.keys(), horizontal=True)
# stamp = stamp_map[stamp_str]


# horizontal_align = st.selectbox(
#     "Horizontal alignment", options=("Center", "Left", "Right")
# )
# vertical_align = st.selectbox(
#     "Vertical alignment", options=("Center", "Top", "Bottom")
# )

if file_uploaded:
    file_uploaded = io.BytesIO(file_uploaded.getvalue())
    file_uploaded_2 = file_uploaded.read()  # Leggere l'immagine come bytes
    cols = st.columns(2)

    with cols[0]:
        cropped_pic = st_cropperjs(pic=file_uploaded_2, btn_text="Generate!", key="cropper")
        cropped_pic = io.BytesIO(cropped_pic)
    with cols[1]:
        try:
            wanted_poster = WantedPoster(cropped_pic, first_name, '', bounty)
            transparency = 255 - int(filter*2.55)  # Invert the transparency
            vertical_align_enum = VerticalAlignment('center'.upper())
            horizontal_align_enum = HorizontalAlignment('center'.upper())

            wanted_poster_path = wanted_poster.generate(
                should_make_portrait_transparent=True,
                portrait_transparency_value=transparency,
                capture_condition=capture_condition,
                # effects=effects_selected,
                # stamp=stamp,
            )

            # Apri l'immagine generata e converti in bytes
            with open(wanted_poster_path, "rb") as img_file:
                image_bytes = img_file.read()


            # Show poster preview
            st.image(wanted_poster_path, use_container_width=True)
            # image_bytes = pil_image_to_bytes(wanted_poster_path, format='PNG')  # Converti l'immagine finale in bytes

            # Delete poster
            current_dir = os.getcwd()
            for file in os.listdir(current_dir):
                if file.endswith(".jpg"):
                    os.remove(file)

            st.download_button(
                label="Download",
                data=image_bytes,
                file_name="immagine_finale.jpg",
                mime="image/jpg",
                use_container_width=True
            )
        except:
            st.info('Confirm to generate.')

html_code = support_icon(
    "static/support.png",
    "static/telegram.png",
    "mailto:giovanni.bocchi@gmail.com?subject=One Piece Wanted - Supporto&body=Ciao Supporto!",
    "static/whatsapp.png",
    "mailto:mastro.costruttore@gmail.com?subject=One Piece Wanted - Supporto&body=Ciao Supporto!",
    "static/mail.png",
    "mailto:giovanni.bocchi@gmail.com?subject=One Piece Wanted - Supporto&body=Ciao Supporto!"
)

st.markdown(html_code, unsafe_allow_html=True)