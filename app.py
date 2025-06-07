
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np

st.set_page_config(page_title="내가 그린 은하는 어떤 은하일까?", layout="centered")

def set_background():
    st.markdown(
        """
        <style>
        body {
            background-color: #0d1117;
            color: #ffffff;
        }
        .stApp {
            background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Hubble_Ultra-Deep_Field_part_detailed.jpg/2560px-Hubble_Ultra-Deep_Field_part_detailed.jpg');
            background-attachment: fixed;
            background-size: cover;
        }
        h1, h2, h3, h4 {
            color: #F2F2F2;
            text-align: center;
        }
        .result-box {
            background-color: rgba(20, 20, 30, 0.7);
            padding: 1.5em;
            border-radius: 10px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

st.markdown("<h1>🌌 내가 그린 은하는 어떤 은하일까?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>은하를 직접 그려보세요! 색상 분석을 통해 어떤 은하와 비슷한지 알려드릴게요.</p>", unsafe_allow_html=True)

canvas_result = st_canvas(
    fill_color="white",
    stroke_width=4,
    stroke_color="black",
    background_color="white",
    height=256,
    width=256,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("🛰️ 분석 시작"):
    if canvas_result.image_data is not None:
        img = canvas_result.image_data.astype(np.uint8)
        st.image(img, caption="🖼️ 당신이 그린 은하")

        r, g, b = img[:, :, 0].mean(), img[:, :, 1].mean(), img[:, :, 2].mean()
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        if b > r and b > g:
            st.markdown("✨ <b>나선형 은하</b>일 가능성이 높아요!", unsafe_allow_html=True)
            st.markdown("🌀 푸른빛은 젊은 별들이 많은 활발한 은하를 의미해요.")
        elif r > b:
            st.markdown("🌟 <b>타원형 은하</b>일 수도 있어요!", unsafe_allow_html=True)
            st.markdown("🔴 붉은 계열은 오래된 별들이 많은 고요한 은하일 수 있어요.")
        else:
            st.markdown("🪐 <b>불규칙 은하</b>일 수도 있어요!", unsafe_allow_html=True)
            st.markdown("🌈 다양한 색상이 섞인 복잡한 구조네요.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("그림을 먼저 그려주세요 ✏️")
