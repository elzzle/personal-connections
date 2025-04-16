import flet as ft
from game.puzzle_data import source_arr, word_containers

NORMAL_COLOR = '#edebe6'
HOVER_COLOR = '#faf9f7'
HIGHLIGHT_COLOR = '#858076'

TEXT_COLOR_NORMAL = "#000000"
TEXT_COLOR_HIGHLIGHTED = "#ffffff"

num_highlighted = 0

# TODO: Fix the changing of colors between hovering over and highlighting

def on_hover(e):
    e.control.bgcolor = HOVER_COLOR if e.data == 'true' else NORMAL_COLOR
    e.control.update()

def on_click(e):
    if e.control.bgcolor != HIGHLIGHT_COLOR:
        e.control.bgcolor = HIGHLIGHT_COLOR
        e.control.content = build_text(e.control.content.value, TEXT_COLOR_HIGHLIGHTED)

    else:
        e.control.bgcolor = NORMAL_COLOR
        e.control.content = build_text(e.control.content.value, TEXT_COLOR_NORMAL)

    e.control.update()

def build_container(id):
    text = source_arr[id]
    container = ft.Container(
                        content=build_text(text, TEXT_COLOR_NORMAL),
                        alignment=ft.alignment.center,
                        width=100,
                        height=100,
                        border=ft.border.all(1, '#edebe6'),
                        bgcolor=NORMAL_COLOR,
                        border_radius=10,
                        on_hover=on_hover,
                        on_click=on_click,
                        data=id
                    )
    word_containers.append((container, text))
    return container

def build_text(text, color):
    return ft.Text(text, color=color, font_family="SpecialGothicCondensedOne", size=20)