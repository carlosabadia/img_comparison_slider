"""Welcome to Reflex! This file showcases the custom component in a basic app."""

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


# Add state and page to the app.
app = rx.App()
app.add_page(index)
