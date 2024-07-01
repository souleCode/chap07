import flet as ft
import speedtest
from time import sleep
from TypeWriterSpeedTes import TypeWriterControlSpeedTest


def main(page: ft.Page):
    page.title = "Internet Speed Test"
    page.theme_mode = 'dark'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_bgcolor = 'blue'
    page.padding = 20
    page.bgcolor = "black"

    # Enable scroll in the page
    page.auto_scroll = True

    # Configure the fonts
    page.fonts = {
        "RoosterPersonalUse": "fonts/RoosterPersonalUse-3z8d8.ttf",
        "SourceCodePro-BlackItalic": "fonts/SourceCodePro-BlackItalic.ttf",
        "SourceCodePro-Bold": "fonts/SourceCodePro-Bold.ttf"
    }

    # Heading of the app
    appTitle = ft.Row(
        controls=[
            ft.Text("Internet", font_family="RoosterPersonalUse",
                    style="displayLarge", color="#ff3300"),
            ft.Text("Speed", font_family="RoosterPersonalUse",
                    style="displayLarge", color="#ffff00"),
        ],
        alignment='center',
    )

    # Terminal lines
    line_01 = TypeWriterControlSpeedTest(value="> Press start...",
                                         font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_02 = TypeWriterControlSpeedTest(value="",
                                         font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_03 = TypeWriterControlSpeedTest(value="",
                                         font_family="SourceCodePro-BlackItalic", color="#1aff1a")

    # Progress bar
    progress_bar_01 = ft.ProgressBar(
        width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text_01 = TypeWriterControlSpeedTest(
        value=" ", font_family="SourceCodePro-Bold", transparency=False)
    progress_row_01 = ft.Row([progress_text_01, progress_bar_01])

    line_04 = TypeWriterControlSpeedTest(value="",
                                         font_family="SourceCodePro-Bold", color="#ffff00")
    line_05 = TypeWriterControlSpeedTest(value="",
                                         font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    progress_bar_02 = ft.ProgressBar(
        width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text_02 = TypeWriterControlSpeedTest(
        value=" ", font_family="SourceCodePro-Bold", transparency=False)
    progress_row_02 = ft.Row([progress_text_02, progress_bar_02])

    line_06 = TypeWriterControlSpeedTest(value="",
                                         font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_07 = TypeWriterControlSpeedTest(value="",
                                         font_family="SourceCodePro-Bold", color="#1aff1a")
    line_08 = TypeWriterControlSpeedTest(value="",
                                         font_family="SourceCodePro-BlackItalic", color="#ffffff")
    termilText = ft.Column(
        [line_01, line_02,
         line_03, progress_row_01, line_04,
         line_05, line_06, progress_row_02,
         line_07, line_08]
    )

    # Container to display internet infos
    getSpeedContainer = ft.Container(
        content=termilText,
        width=200,
        height=100,
        bgcolor="#4d4d4d",
        border_radius=35,
        animate=ft.animation.Animation(1000, "bounceOut")
    )

    # Terminal animation function
    def animate_getSpeedContainer(e):
        progress_row_01.opacity = 0
        progress_bar_01.opacity = 0
        progress_bar_02.opacity = 0
        progress_row_02.opacity = 0
        progress_bar_02.value = None
        progress_bar_01.value = None

        line_01.text_to_print = ""
        line_01.update()

        line_02.text_to_print = ""
        line_02.update()

        line_03.text_to_print = ""
        line_03.update()

        line_04.text_to_print = ""
        line_04.update()

        line_05.text_to_print = ""
        line_05.update()

        line_06.text_to_print = ""
        line_06.update()

        line_07.text_to_print = ""
        line_07.update()

        line_08.text_to_print = ""
        line_08.update()

        getSpeedContainer.update()
        getSpeedContainer.width = 700
        getSpeedContainer.height = 400
        line_01.text_to_print = "> Calculating download speed, please wait..."
        getSpeedContainer.update()
        sleep(2)
        line_01.update()

        try:
            st = speedtest.Speedtest()
            ideal_server = st.get_best_server()  # Find the best server and connect
            city = ideal_server['name']
            country = ideal_server['country']
            cc = ideal_server['cc']
            line_02.text_to_print = f">Finding the best possible server in {city},{country} ({
                cc})"
            line_02.update()
            getSpeedContainer.update()
            sleep(4)

            line_03.text_to_print = "> Connection established, status OK"
            line_03.update()
            progress_row_01.opacity = 1
            progress_bar_01.opacity = 1
            getSpeedContainer.update()

            download_speed = st.download()/1024/1024
            progress_bar_01.value = 1
            line_04.text_to_print = f"> The download speed is {
                str(round(download_speed, 2))} Mbps"
            line_04.update()
            getSpeedContainer.update()

            line_05.text_to_print = "> Calculating upload speed, please wait..."
            line_05.update()
            getSpeedContainer.update()
            sleep(2)
            line_06.text_to_print = "> Executing upload script, hold on..."
            line_06.update()
            progress_row_02.opacity = 1
            progress_bar_02.opacity = 1
            getSpeedContainer.update()
            upload_speed = st.upload()/1024/1024
            progress_bar_02.value = 1
            line_07.text_to_print = f"The upload speed is {
                str(round(upload_speed, 2))} Mbps"
            line_07.update()
            getSpeedContainer.update()
            sleep(2)
            line_08.text_to_print = "> Completed successfully\n\n >>App Developed by SouleCode"
            line_08.update()
            getSpeedContainer.update()

        except speedtest.ConfigRetrievalError as e:
            line_01.text_to_print = "> Error: Unable to retrieve configuration. Please try again later."
            line_01.update()
            getSpeedContainer.update()
        except Exception as e:
            line_01.text_to_print = f"> Error: {str(e)}"
            line_01.update()
            getSpeedContainer.update()

    # Page components
    page.add(
        appTitle,
        getSpeedContainer,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
                      on_click=animate_getSpeedContainer,
                      icon_color="#1aff1a", icon_size=50,
                      ),
    )


ft.app(target=main, assets_dir="assets")
