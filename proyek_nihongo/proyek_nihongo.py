import reflex as rx

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Perpustakaan Digital N2", size="9", color_scheme="cyan"),
            rx.text(
                "Selamat datang, Master Haris! Dashboard ini siap membantu persiapan N2 Master.",
                size="5",
                text_align="center",
            ),
            rx.divider(),
            rx.vstack(
                rx.text("Akses Cepat Materi:", weight="bold"),
                rx.link(
                    rx.button(
                        "📚 Buka PDF Soumatome N2",
                        color_scheme="blue",
                        size="4",
                        width="100%",
                        cursor="pointer",
                    ),
                    href="https://link-google-drive-master-disini", # Ganti dengan link PDF Master
                    is_external=True,
                ),
                rx.link(
                    rx.button(
                        "📝 Latihan Soal N2",
                        color_scheme="green",
                        size="4",
                        width="100%",
                        cursor="pointer",
                    ),
                    href="https://www.google.com", # Bisa diganti link lain nanti
                    is_external=True,
                ),
                spacing="4",
                width="100%",
            ),
            rx.spacer(),
            rx.text("Ganbatte kudasai!", font_style="italic", color_scheme="gray"),
            spacing="6",
            padding="2em",
            background="white",
            border_radius="15px",
            box_shadow="lg",
            align="center",
        ),
        background="whitesmoke",
        height="100vh",
        width="100%",
    )

# Membuat objek aplikasi
app = rx.App()
# Menambahkan halaman 'index' sebagai halaman utama (/)
app.add_page(index)


