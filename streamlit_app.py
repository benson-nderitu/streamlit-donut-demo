import streamlit as st
from streamlit_donut import st_donut

st.set_page_config(
    page_title="Streamlit Donut Demo",
    page_icon=":material/donut_large:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def delta_calculate(current_value, previous_value):
    if previous_value == 0:
        return "N/A"
    delta = ((current_value - previous_value) / previous_value) * 100
    return f"{delta:.2f}% YoY"


st.subheader("Streamlit Donut Demo")
col1, col2 = st.columns(2)
col1.subheader("Parameters", divider="gray")
col2.subheader("Donut", divider="gray")

col1, col2, col3 = st.columns([1, 1, 2], gap="large")
with col1:
    label = st.text_input("Label", value="Sales Profit")
    current_value = st.slider("Current Value", min_value=0, max_value=1000, value=200)
    previous_value = st.slider("Previous Value", min_value=0, max_value=1000, value=180)
    delta = delta_calculate(current_value, previous_value)
    value = st.slider("Value", min_value=0, max_value=1000, value=200)
    outOf = st.slider("Out Of", min_value=0, max_value=1000, value=1000)
    units = st.text_input("Units", value="$")
    direction = st.selectbox(
        "Direction", options=["clockwise", "anticlockwise"], index=1
    )

    delta_placeholder = st.empty()


with col2:
    size = st.slider("Size", min_value=100, max_value=500, value=180)
    text_size = st.slider("Text Size", min_value=10, max_value=100, value=50)
    space = st.slider("Space", min_value=0, max_value=50, value=30)
    delta_text_size = st.slider("Delta Text Size", min_value=10, max_value=50, value=18)
    value_text_color = st.color_picker("Value Text Color", value="#000000")
    arc_bg_color = st.color_picker("Arc Background Color", value="#FF4B4B")
    background_stroke_width = st.slider(
        "Background Stroke Width", min_value=1, max_value=50, value=19
    )
    arc_stroke_width = st.slider(
        "Arc Stroke Width", min_value=1, max_value=50, value=19
    )

    rounded = st.toggle("Rounded")
    label_visibility = st.toggle(
        "Label Visibility",
    )
    hide_background = st.toggle("Hide Background")

delta = delta_placeholder.text_input("Delta", value=delta)
with col3:
    st_donut(
        label=label,
        value=current_value,
        outOf=outOf,
        units=units,
        delta=delta,
        space=space,
        size=size,
        text_size=text_size,
        delta_text_size=delta_text_size,
        value_text_color=value_text_color,
        arc_bg_color=arc_bg_color,
        background_stroke_width=background_stroke_width,
        arc_stroke_width=arc_stroke_width,
        direction=direction,
        rounded=rounded,
        label_visibility=label_visibility,
        hide_background=hide_background,
    )
