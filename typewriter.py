import flet as ft
from TypeWriterControl import TypeWriterControl


def main(page: ft.Page):
    page.title = "Type Writer animation effet App"
    page.window.width = 400
    page.window.height = 500
    page.bgcolor = '#333333'
    page.theme_mode = "dark"
    page.window.center()
    page.scroll = 'always'
    page.update()
    sometexe = '''
       What is Lorem Ipsum?
        Lorem Ipsum is simply dummy text of the printing and typesetting 
        industry. Lorem Ipsum has been the industry's standard dummy text
        ever since the 1500s, when an unknown printer took a galley of type 
        and scrambled it to make a type specimen book. It has survived not 
        only five centuries, but also the leap into electronic typesetting,
        remaining essentially unchanged. It was popularised in the 1960s with
        the release of Letraset sheets containing Lorem Ipsum passages, 
        and more recently with desktop publishing software like Aldus PageMaker
        including versions of Lorem Ipsum.
    '''
    page.add(
        TypeWriterControl(sometexe)
    )


ft.app(target=main, assets_dir="assets")
