[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://donut-metric-demo.streamlit.app/)
[![PyPI version](https://badge.fury.io/py/streamlit-donut.svg)](https://pypi.org/project/streamlit-donut/)

`streamlit-donut` is a Streamlit component for rendering customizable donut charts/metrics. This package allows you to easily create visually appealing donut charts/metrics in your Streamlit applications.

## Installation

You can install the package using pip:

```sh
pip install streamlit-donut
```

![image](https://github.com/user-attachments/assets/1f6ed68e-1cea-4e4e-b109-c378660ea459)

# Usage

Here is an example of how to use the st_donut function in your Streamlit application:

```sh
import streamlit as st
from streamlit_donut import st_donut

# Example
st_donut(
    label="Project Completion",
    value=89,
    outOf=100,
    units="days",
    size=150,
    value_text_color="purple",
    text_size=24,
    background_stroke_width=10,
    arc_stroke_width=20,
    direction="clockwise",
    delta="90%",
    rounded=True,
    label_visibility=True,
    hide_background=True,
)

```

## Parameters

- `label` (str): The label for the donut chart/metric.
- `value` (float): The current value to be displayed on the donut chart/metric.
- `outOf` (float, optional): The maximum value of the donut chart/metric. Default is 100.
- `units` (str, optional): The units to be displayed next to the value. Default is an empty string.
- `delta` (str, optional): The delta value to be displayed below the main value. Default is None.
- `space` (int, optional): The vertical space between the main value and the delta value. Default is 30.(`px`)
- `size` (int, optional): The size of the donut chart/metric. Default is 180. (`px`).
- `direction` (Literal["clockwise", "anticlockwise"], optional): The direction of the donut chart/metric. Default is "clockwise".
- `text_size` (int, optional): The font size of the main value. Default is 50.(`px`)
- `delta_text_size` (int, optional): The font size of the delta value. Default is 18.(`px`)
- `value_text_color` (str, optional): The color of the main value text. Default is None.
- `arc_bg_color` (str, optional): The background color of the arc. Default is None.
- `background_stroke_width` (int, optional): The stroke width of the background circle. Default is 19.
- `arc_stroke_width` (int, optional): The stroke width of the arc. Default is None but falls back to background_stroke_width.
- `rounded` (bool, optional): Whether the arc should have rounded edges. Default is True.
- `label_visibility` (bool, optional): Whether the label should be visible. Default is True.
- `hide_background` (bool, optional): Whether the background circle should be hidden. Default is False.
