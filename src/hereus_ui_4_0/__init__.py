from bevyframe.Widgets.Style import *
from hereus_ui_4_0.palette import palette

imports = [
    "https://fonts.googleapis.com/css2?family=Noto+Emoji:wght@700&display=swap",
    "https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200",
    "https://fonts.googleapis.com/css2?family=Croissant+One&family=Parisienne&display=swap",
    "https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap",
    "https://www.nerdfonts.com/assets/css/webfont.css"
]
webkit = {
    "scrollbar": {
        "width": "0px"
    }
}

css = """
.material-symbols-rounded {
  font-variation-settings:
  'FILL' 0,
  'wght' 200,
  'GRAD' -25,
  'opsz' 30
}
body {
    padding: 0 !important;
    margin: 0 !important;
}
#root {
    position: relative;
    width: 100%; /* not vw */
    max-width: 1600px;
    height: 100vh;
    margin: 0 auto !important;
    overflow: hidden;
    padding: 0 !important;
}
.link {
    text-decoration: underline;
    margin: 0;
    border: 0;
    background: none;
    overflow: visible;
    color: blue;
    cursor: pointer;
}

"""


class Label:
    class Hover:
        border = NoStyle


class Badge:
    class Caution:
        font_weight = 500
        font_size = Size.pixel(15)
        background_color = Color.red
        z_index = 9999
        position = Position.relative()
        padding = Padding(
            left=Size.pixel(4),
            right=Size.pixel(4)
        )
        margin = Margin(
            left=Size.pixel(-30),
            top=Size.pixel(-50)
        )
        border_radius = Size.pixel(10)


class Textbox:
    border_radius = Size.pixel(5)
    border = NoStyle
    font_family = ["DM Sans", "sans-serif"]
    width = Size.pixel(380)
    max_width = Size.pixel(380)
    height = Size.pixel(50)
    font_size = Size.pixel(20)
    padding = Padding(
        left=Size.pixel(10),
        right=Size.pixel(10)
    )
    css = {'backdrop-filter': 'blur(10px)'}

    class LightTheme:
        background_color = palette["Light"]["SubWidgetColor"]
        color = Color.black

    class DarkTheme:
        background_color = palette["Dark"]["SubWidgetColor"]
        color = Color.white

    class Focus:
        outline = NoStyle


class Button:
    border_radius = Size.pixel(10)
    border = NoStyle
    color = Color.white
    width = Size.pixel(400)
    height = Size.pixel(50)
    font_size = Size.pixel(20)
    cursor = Cursor.pointer
    font_family = ["DM Sans", "sans-serif"]
    css = {
        'box-shadow': '0px 0px 30px #8080801A',
        'backdrop-filter': 'blur(10px)'
    }

    class Hover:
        outline = NoStyle
        css = {"box-shadow": "inset 0 0 100px 100px #FFFFFF60"}

    class LightTheme:
        class Blank:
            background_color = palette["Blank"]["AccentColor"]

        class Red:
            background_color = palette["Red"]["AccentColor"]

        class Orange:
            background_color = palette["Orange"]["AccentColor"]

        class Yellow:
            background_color = palette["Yellow"]["AccentColor"]

        class Green:
            background_color = palette["Green"]["AccentColor"]

        class Blue:
            background_color = palette["Blue"]["AccentColor"]

        class Pink:
            background_color = palette["Pink"]["AccentColor"]

    class DarkTheme:
        class Blank:
            color = Color.black
            background_color = palette["Blank"]["AccentColor"]

        class Red:
            color = Color.black
            background_color = palette["Red"]["AccentColor"]

        class Orange:
            color = Color.black
            background_color = palette["Orange"]["AccentColor"]

        class Yellow:
            color = Color.black
            background_color = palette["Yellow"]["AccentColor"]

        class Green:
            color = Color.black
            background_color = palette["Green"]["AccentColor"]

        class Blue:
            color = Color.black
            background_color = palette["Blue"]["AccentColor"]

        class Pink:
            color = Color.black
            background_color = palette["Pink"]["AccentColor"]


class SmallButton:
    border_radius = Size.pixel(10)
    width = Size.pixel(150)
    height = Size.pixel(50)


class MiniButton:
    # modifying over 'Button'
    border_radius = Size.pixel(15)
    width = Size.pixel(100)
    height = Size.pixel(30)
    font_size = Size.pixel(15)

    class LightTheme:
        class Blank:
            background_color = palette["Light"]["WidgetColor"]
            color = palette["Blank"]["AccentColor"]

        class Red:
            background_color = palette["Light"]["WidgetColor"]
            color = palette["Red"]["AccentColor"]

        class Orange:
            background_color = palette["Light"]["WidgetColor"]
            color = palette["Orange"]["AccentColor"]

        class Yellow:
            background_color = palette["Light"]["WidgetColor"]
            color = palette["Yellow"]["AccentColor"]

        class Green:
            background_color = palette["Light"]["WidgetColor"]
            color = palette["Green"]["AccentColor"]

        class Blue:
            background_color = palette["Light"]["WidgetColor"]
            color = palette["Blue"]["AccentColor"]

        class Pink:
            background_color = palette["Light"]["WidgetColor"]
            color = palette["Pink"]["AccentColor"]

    class DarkTheme:
        class Blank:
            background_color = palette["Dark"]["WidgetColor"]
            color = palette["Blank"]["AccentColor"]

        class Red:
            background_color = palette["Dark"]["WidgetColor"]
            color = palette["Red"]["AccentColor"]

        class Orange:
            background_color = palette["Dark"]["WidgetColor"]
            color = palette["Orange"]["AccentColor"]

        class Yellow:
            background_color = palette["Dark"]["WidgetColor"]
            color = palette["Yellow"]["AccentColor"]

        class Green:
            background_color = palette["Dark"]["WidgetColor"]
            color = palette["Green"]["AccentColor"]

        class Blue:
            background_color = palette["Dark"]["WidgetColor"]
            color = palette["Blue"]["AccentColor"]

        class Pink:
            background_color = palette["Dark"]["WidgetColor"]
            color = palette["Pink"]["AccentColor"]


class Link:
    color = inherit
    text_decoration = inherit


class TextArea:
    margin = Size.pixel(3)
    font_family = ["DM Sans", "sans-serif"]

    class Focus:
        outline = NoStyle


class Page:
    font_family = ["DM Sans", "sans-serif"]
    overflow = Overflow(x=Visibility.hidden)
    scroll_behavior = Scroll.smooth
    padding = Padding(
        top=Size.pixel(0)
    )

    class LightTheme:
        color = Color.black

        class Blank:
            background_image = palette["Blank"]["LightBackground"]
            background_color = palette["Blank"]["LightBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Blank"]["AccentColor"]

        class Red:
            background_image = palette["Red"]["LightBackground"]
            background_color = palette["Red"]["LightBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Red"]["AccentColor"]

        class Orange:
            background_image = palette["Orange"]["LightBackground"]
            background_color = palette["Orange"]["LightBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Orange"]["AccentColor"]

        class Yellow:
            background_image = palette["Yellow"]["LightBackground"]
            background_color = palette["Yellow"]["LightBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Yellow"]["AccentColor"]

        class Green:
            background_image = palette["Green"]["LightBackground"]
            background_color = palette["Green"]["LightBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Green"]["AccentColor"]

        class Blue:
            background_image = palette["Blue"]["LightBackground"]
            background_color = palette["Blue"]["LightBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Blue"]["AccentColor"]

        class Pink:
            background_image = palette["Pink"]["LightBackground"]
            background_color = palette["Pink"]["LightBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Pink"]["AccentColor"]

    class DarkTheme:
        color = Color.white

        class Blank:
            background_image = palette["Blank"]["DarkBackground"]
            background_color = palette["Blank"]["DarkBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Blank"]["AccentColor"]

        class Red:
            background_image = palette["Red"]["DarkBackground"]
            background_color = palette["Red"]["DarkBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Red"]["AccentColor"]

        class Orange:
            background_image = palette["Orange"]["DarkBackground"]
            background_color = palette["Orange"]["DarkBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Orange"]["AccentColor"]

        class Yellow:
            background_image = palette["Yellow"]["DarkBackground"]
            background_color = palette["Yellow"]["DarkBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Yellow"]["AccentColor"]

        class Green:
            background_image = palette["Green"]["DarkBackground"]
            background_color = palette["Green"]["DarkBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Green"]["AccentColor"]

        class Blue:
            background_image = palette["Blue"]["DarkBackground"]
            background_color = palette["Blue"]["DarkBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Blue"]["AccentColor"]

        class Pink:
            background_image = palette["Pink"]["DarkBackground"]
            background_color = palette["Pink"]["DarkBackground"].split(", ")[2].split(" ")[0]
            accent_color = palette["Pink"]["AccentColor"]


class Box:
    border = Border(Size.pixel(2), BorderLine.solid, "#ffffffa0")
    border_radius = Size.pixel(20)
    padding = Padding(
        top=Size.pixel(0),
        bottom=Size.pixel(0),
        left=Size.pixel(15),
        right=Size.pixel(15)
    )
    css = {'backdrop-filter': 'blur(10px)'}

    class LightTheme:
        background_color = palette["Light"]["WidgetColor"]

    class DarkTheme:
        background_color = palette["Dark"]["WidgetColor"]


class Navbar:
    width = Size.pixel(80)
    overflow = Visibility.hidden
    border_radius = Size.pixel(10)
    z_index = 9999
    padding = Padding(
        right=Size.pixel(5)
    )
    position = Position.fixed(
        top=Size.pixel(20),
        bottom=Size.pixel(20),
        left=Size.pixel(10)
    )

    class RawItem:
        float = Float.right
        border_radius = Size.pixel(15)
        text_align = Align.center
        text_decoration = NoStyle
        font_size = Size.pixel(17)
        color = [Color.black, Color.white]
        align_items = Align.left
        cursor = Cursor.pointer
        border = NoStyle
        padding = Padding(
            top=Size.pixel(14),
            bottom=Size.pixel(14),
            left=Size.pixel(16),
            right=Size.pixel(16)
        )

    class ActiveItem:
        background_color = palette["Light"]["WidgetColor"]

    class InactiveItem:
        background_color = Color.transparent

    class Icon:
        float = Float.left
        text_align = Align.center
        text_decoration = NoStyle
        padding = Padding(
            left=Size.pixel(10),
        )


class Topbar:
    height = Size.pixel(75)
    overflow = Visibility.hidden
    border_radius = Size.pixel(10)
    z_index = 9999
    padding = Padding(
        right=Size.pixel(5),
        top=Size.pixel(20)
    )
    position = Position.fixed(
        top=Size.pixel(0),
        left=Size.pixel(0),
        right=Size.pixel(0)
    )
    margin = Margin(
        top=Size.pixel(-10)
    )

    class Item:
        background_color = Color.transparent
        border_radius = Size.pixel(15)
        align_items = Align.left
        cursor = Cursor.pointer
        float = Float.right
        color = Color.black
        border = NoStyle
        padding = Padding(
            top=Size.pixel(14),
            bottom=Size.pixel(14),
            left=Size.pixel(16),
            right=Size.pixel(16)
        )
        css = {"filter": "drop-shadow(1px 1px 1px #808080A0)"}
