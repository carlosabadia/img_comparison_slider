# img-comparison-slider

A Reflex custom component img-comparison-slider.

## Installation

```bash
pip install reflex-img-comparison-slider
```

## Usage

```python
import reflex as rx
from reflex_img_comparison_slider import img_comparison_slider


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Image Comparison Slider", size="7"),
            img_comparison_slider(
                rx.image(src="/green-leaves.webp", slot="first"),
                rx.image(src="/green-leaves-blurred.webp", slot="second"),
            ),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )
```

### Slider Props

| Name       | Key          | Values                               | Description                                                              |
|------------|--------------|--------------------------------------|--------------------------------------------------------------------------|
| Position   | `value`      | `int`                        | Position of the divider in percents. Must be between 0 and 100. (default: 50) |
| Hover      | `hover`      | `bool`                       | Automatically slide on mouse over. (default: False)                      |
| Direction  | `direction`  | `"vertical", "horizontal"`           | Direction of the slider. (default: "horizontal")                         |
| Keyboard   | `keyboard`   | `"enabled", "disabled`            | Enable/disable slider position control with the keyboard. (default: enabled) |
| Handle     | `handle`     | `bool`                       | Enable/disable dragging by handle only. (default: False)                 |
