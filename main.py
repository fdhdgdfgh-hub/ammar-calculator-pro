import flet as ft

def main(page: ft.Page):
    page.title = "حاسبة عمار PRO"
    page.bgcolor = "#171717"
    page.window_width = 400
    page.window_height = 700
    
    # شاشة العرض
    result_text = ft.Text(value="0", color="white", size=40)
    history_text = ft.Text(value="", color="grey", size=20)

    def on_click(e):
        button_text = e.control.text
        current = result_text.value

        if button_text == "=":
            try:
                history_text.value = current + " ="
                # تحويل العلامات لتفهمها بايثون
                math_expr = current.replace('×', '*').replace('÷', '/').replace('%', '/100')
                result_text.value = str(eval(math_expr))
            except:
                result_text.value = "خطأ"
        elif button_text == "C":
            result_text.value = "0"
            history_text.value = ""
        elif button_text == "DEL":
            result_text.value = current[:-1] if len(current) > 1 else "0"
        else:
            result_text.value = button_text if current == "0" else current + button_text
        
        page.update()

    # إنشاء الأزرار
    def btn(text, color="grey800"):
        return ft.ElevatedButton(
            text=text, on_click=on_click, 
            bgcolor=color, color="white", expand=1, height=70
        )

    page.add(
        ft.Column([
            ft.Container(content=ft.Column([history_text, result_text]), padding=20),
            ft.Row([btn("C", "orange"), btn("DEL", "orange"), btn("%", "orange"), btn("÷", "orange")]),
            ft.Row([btn("7"), btn("8"), btn("9"), btn("×", "orange")]),
            ft.Row([btn("4"), btn("5"), btn("6"), btn("-", "orange")]),
            ft.Row([btn("1"), btn("2"), btn("3"), btn("+", "orange")]),
            ft.Row([btn("0",), btn("."), btn("=" , "blue")]),
        ])
    )

ft.app(target=main)
