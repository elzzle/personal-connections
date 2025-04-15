import flet as ft
from utils.container_utils import on_hover

def main(page: ft.Page):
    page.title = "Emanuel's Connections"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.fonts = {
        "Cute Ghost": "assets/fonts/CuteGhostRegular.woff2"
    }

    header = ft.Text(
        "Emanuel's Connections",
        size=30,
        text_align=ft.TextAlign.CENTER
    )

    grid = ft.Column(
        controls = [
            ft.Row(
                controls = [
                    ft.Container(
                        width=100,
                        height=100,
                        border=ft.border.all(1, '#edebe6'),
                        bgcolor='#edebe6',
                        border_radius=10,
                        on_hover=on_hover,
                        data=r*4+c
                    ) for c in range(4)
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

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
