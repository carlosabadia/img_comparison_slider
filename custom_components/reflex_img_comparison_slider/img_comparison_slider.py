"""Reflex custom component ImgComparisonSlider."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

# Component wrapped: https://github.com/sneas/img-comparison-slider

import reflex as rx
from typing import Literal

LiteralDirection = Literal["vertical", "horizontal"]
LiteralKeyboard = Literal["enabled", "disabled"]


class ImgComparisonSlider(rx.Component):
    """ImgComparisonSlider component."""

    # The React library to wrap.
    library = "@img-comparison-slider/react"

    # The React component tag.
    tag = "ImgComparisonSlider"

    # Position of the divider in percents. Must be between 0 and 100. (default: 50)
    value: rx.Var[int] = 50

    # Automatically slide on mouse over. (default: False)
    hover: rx.Var[bool] = False

    # Direction of the slider. (default: "horizontal")
    direction: rx.Var[LiteralDirection] = "horizontal"

    # Enable/disable slider position control with the keyboard. (default: enabled)
    keyboard: rx.Var[LiteralKeyboard] = "enabled"

    # Enable/disable dragging by handle only. (default: False)
    handle: rx.Var[bool] = False



img_comparison_slider = ImgComparisonSlider.create