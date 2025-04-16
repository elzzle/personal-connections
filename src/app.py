import flet as ft
from utils.container_utils import build_container
from game.game_logic import shuffle

def main(page: ft.Page):
    page.title = "Emanuel's Connections"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.fonts = {
        "SpecialGothicCondensedOne": "fonts/SpecialGothicCondensedOne-Regular.ttf",
        "Cute Ghost": "fonts/Cute Ghost.ttf"
    }

    header = ft.Text(
        "Emanuel's Connections",
        size=80,
        text_align=ft.TextAlign.CENTER,
        font_family="Cute Ghost"
    )

    grid = ft.Column(
        controls = [
            ft.Row(
                controls = [
                    build_container(r*4+c) for c in range(4)
                ],
                spacing = 12,
                alignment=ft.MainAxisAlignment.CENTER
            ) for r in range(4)
        ],
        spacing = 12,
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(header)
    page.add(grid)
    page.add(ft.ElevatedButton("Shuffle", on_click=shuffle))

    shuffle(None)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
