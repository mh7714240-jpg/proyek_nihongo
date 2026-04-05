
import reflex as rx

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Perpustakaan Digital N2 Master Haris", size="9"),
            rx.text(
                "Selamat datang di dashboard belajar pribadi.",
                color_scheme="gray",
            ),
            rx.divider(),
            # Tombol untuk membuka PDF Soumatome N2
            rx.link(
                rx.button(
                    "Buka PDF Soumatome N2",
                    color_scheme="blue",
                    cursor="pointer",
                    size="4",
                ),
                href="https://link-google-drive-master-disini", # Ganti dengan link share PDF Master
                is_external=True,
            ),
            rx.text("Ganbatte kudasai, Master!", font_style="italic"),
            align="center",
            spacing="5",
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index)
