import flet as ft

class LoginGUI:
    def __init__(self):
        self.username_field = ft.TextField(width=280, height=40, hint_text='Username', border='underline', color='#303030', prefix_icon=ft.icons.EMAIL)
        self.password_field = ft.TextField(width=280, height=40, hint_text='Password', border='underline', color='#303030', prefix_icon=ft.icons.LOCK)
        self.sign_in_button = ft.ElevatedButton(content=ft.Text("SIGN IN", color='white', weight=ft.FontWeight.W_500), width=280, bgcolor='black')
        self.body = self.build_body()

    def build_body(self):
        body = ft.Container(
            ft.Container(
                ft.Stack([
                    ft.Container(
                        border_radius=11,
                        rotate=ft.Rotate(0.98 * 3.14),  # degree
                        width=360,
                        height=560,
                        bgcolor='#22ffffff',
                    ),
                    ft.Container(
                        ft.Container(
                            ft.Column([
                                ft.Container(
                                    ft.Image(
                                        src='user.png',
                                        width=60,
                                    ),
                                    padding=ft.padding.only(150, 20),
                                ),
                                ft.Text(
                                    "Sign in",
                                    width=360,
                                    size=30,
                                    weight=ft.FontWeight.W_900,
                                    text_align='center',
                                ),
                                ft.Text(
                                    "Please login to use the platform",
                                    width=360,
                                    text_align='center',
                                ),
                                ft.Container(
                                    self.username_field,
                                    padding=ft.padding.only(40, 20),
                                ),
                                ft.Container(
                                    self.password_field,
                                    padding=ft.padding.only(40, 10),
                                ),
                                ft.Container(
                                    ft.TextButton(
                                        "I forgot my password",
                                    ),
                                    padding=ft.padding.only(40),
                                ),
                                ft.Container(
                                    self.sign_in_button,
                                    padding=ft.padding.only(40, 10)
                                ),
                                ft.Container(
                                    ft.Row([
                                        ft.Text(
                                            "Don't have an account?",
                                        ),
                                        ft.TextButton(
                                            "Create a free account."
                                        ),
                                    ], spacing=0),
                                    padding=ft.padding.only(40),
                                ),
                            ]),
                        ),
                        width=360,
                        height=560,
                        bgcolor='#22ffffff',
                        border_radius=11,
                    ),
                ]),
                padding=110,
                width=360,
                height=560,
            ),
            width=580,
            height=740,
            gradient=ft.LinearGradient(colors=['#5899E2', '#274060'])
        )
        return body

    def get_username(self):
        return self.username_field.value

    def get_password(self):
        return self.password_field.value