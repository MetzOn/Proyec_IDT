import flet as ft

class PrincipalGUI(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)
        #Colores:
        self.ColorFondoN='#274060'
        self.ColorFondoA='#5899E2'
        #Texto:
        self.defecto=ft.Text(value="SRFacial > ",
                             style=ft.TextStyle(
                                color=ft.colors.WHITE,
                                size=18,
                                weight=ft.FontWeight.W_500,
                                font_family="Arial")
                                )
        self.direccion1=ft.Text(value="Reconocimiento",
                             style=ft.TextStyle(
                                color=ft.colors.WHITE,
                                size=18,
                                weight=ft.FontWeight.W_500,
                                font_family="Arial"))
        self.direccion2=ft.Text(value="Registro y administracion de Empleados",
                             style=ft.TextStyle(
                                color=ft.colors.WHITE,
                                size=18,
                                weight=ft.FontWeight.W_500,
                                font_family="Arial"))
        self.direccion3=ft.Text(value="Registro de Historial",
                             style=ft.TextStyle(
                                color=ft.colors.WHITE,
                                size=18,
                                weight=ft.FontWeight.W_500,
                                font_family="Arial"))
        self.direccion_principal=[self.direccion1,self.direccion2,self.direccion3]
        #Componentes: 
            #Para el video
        self.Imagen_video=ft.Image( src=False, width="100%", height="100%")
            #TextField para el Registro de empleados
        self.tfNombreEmpleado=ft.TextField(hint_text="Ingrese su nombre",label="Nombres"
        )
        self.tfApellidosEmpleado=ft.TextField(hint_text="Ingrese su apellido",label="Apellidos")

        self.tfIdEmpleado=ft.TextField(hint_text="ID: Se genera Automaticamente",disabled=True)

        self.tfDniEmpleado=ft.TextField(hint_text="Ingrese su DNI",max_length=8,keyboard_type=ft.KeyboardType.NUMBER,label="DNI")

        self.tfTelefonoEmpleado=ft.TextField(hint_text="Ingrese su teléfono",
        max_length=9,  # Asumiendo que el teléfono tiene 10 dígitos
        keyboard_type=ft.KeyboardType.PHONE,label="Telefono")

        self.tfTipoEmpleado=ft.Dropdown(
        label="Tipo de Empleado",
        hint_text="Seleccione el tipo de empleado",
        options=[
            ft.dropdown.Option(key="A", text="Administrador"),
            ft.dropdown.Option(key="B", text="Empleado")
            ]
        )
        self.tfPermiso=

        #Paneles (implementacion de componentes)
        self.Navegacion= ft.Container(#Se crea el container par apoder ponerle cosas dentro 

            col=1,
            bgcolor=self.ColorFondoN,
            border_radius= 10,
            #El content se usa para recien delimitar el contenido que tendra el container, el resto es para estetica del contenedor
            content=ft.Column( 
                #Controls es como en content pero de las columnas y filas, es una lista, lo que se coloque ahi va a estar ordenado en la columna, o la fila 
                controls=[
                    ft.Container(
                        #NavigationBar es un contenedor especifico para la navecacion, te da atributos para manejar eso de manera mas sencilla
                        padding=ft.padding.only(top=20),
                        expand=True,
                        content=ft.NavigationRail(
                            bgcolor=self.ColorFondoN,
                            expand=True,
                            selected_index=0,
                            destinations=[
                                ft.NavigationDestination(label="CASA",icon=ft.icons.HOME),
                                ft.NavigationDestination(label="REGISTRO",icon=ft.icons.APP_REGISTRATION),
                                ft.NavigationDestination(label="HISTORIAL",icon=ft.icons.FACT_CHECK),
                            ]


                        )
                    ),
                    ft.Container(
                        padding=ft.padding.only(bottom=20),
                        expand=True,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            expand=True,
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.IconButton(
                                icon=ft.icons.OUTPUT,
                            ),
                            
                            ],
                            
                            
                        )

                    ),
                ]
            )

        )
        
#AQUI ESTOY
        self.Contenedor_Inicial_Home=ft.Container(
            expand= True,
            border_radius= 10,
            content=ft.Column(
                expand= True,
                controls=[
                    ft.Column(
                        expand= True,
                    controls=[
                        ft.Container(
                            bgcolor=self.ColorFondoN,
                            padding=20,
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                    controls=[
                                        self.defecto,
                                        self.direccion_principal[0]
                                    ]
                                ),
                                ]
                            )
                            
                        ),
                        ft.Container(
                            padding=20,
                            alignment=ft.alignment.center,
                            
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            value="Iniciar camara",
                                            font_family="Arial",
                                            size=14,
                                            weight=500
                                        ),
                                        ft.ElevatedButton(
                                            text="INICIAR",
                                        )     
                                    ]
                                )
                        ),
                        ft.Container(
                            expand=True,
                            alignment=ft.alignment.center,
                            content=(
                                ft.Column(
                                    controls=[
                                        self.Imagen_video
                                    ]
                                )
                            )
                            

                        ),
                        ft.Container(
                            padding=20,
                            
                            alignment=ft.alignment.center,
                            content=(
                                ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            value="Finalizar Video",
                                            font_family="Arial",
                                            size=14,
                                            weight=500
                                        ),
                                        ft.ElevatedButton(
                                            text="FINALIZAR",
                                        )     
                                    ]
                                )
                            )
                            

                        ),

                    ]
                )
                ]
            )


            
        )
        
        self.Contenedor_Inicial_Registro=ft.Container(
            expand=True,
            content= ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        bgcolor=self.ColorFondoN,
                            padding=20,
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                    controls=[
                                        self.defecto,
                                        self.direccion_principal[1]
                                    ]
                                ),
                                ]
                            )

                    ),
                    ft.Container(
                        content=ft.ResponsiveRow(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                 
                                ft.ElevatedButton(
                                    expand=True,
                                    icon=ft.icons.GROUP_ADD,
                                    text="Agregar nuevo empleado",
                                    col={'md': 6, 'lg': 3},
                                    

                                ),
                                ft.ElevatedButton(
                                    icon=ft.icons.TABLE_VIEW,
                                    text="Administrar empleados",
                                    col={'md': 6, 'lg': 3}
                                ),
                            ]
                        )
                    ),
                    ft.Container(
                        expand=True,
                        content=ft.ResponsiveRow(
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                ft.Column(
                                            col={'md': 11, 'lg': 5},
                                            controls=[
                                                self.tfIdEmpleado,
                                                self.tfNombreEmpleado,
                                                self.tfApellidosEmpleado
                                            ]
                                        ),
                                ft.Column(
                                    col={'md': 11, 'lg': 5},
                                            controls=[
                                                self.tfDniEmpleado,
                                                self.tfTelefonoEmpleado,
                                                self.tfTipoEmpleado
                                            ]
                                        )
                                
                            ]

                        )
                    ),
                    ft.Container(),
                ]
            )

        )
       
       
       
       
       
       
       
        self.Paneles= ft.Container(
            expand=True,
            col=11,
            content=ft.Column(
                controls=[
                    self.Contenedor_Inicial_Registro
                ]
                
            )
        )

        self.Contenido= ft.ResponsiveRow(
            controls=[
                self.Navegacion,
                self.Paneles
            ]
        )


    def build(self):
        return self.Contenido

def main(page: ft.Page):
    page.window_min_height=820
    page.window_min_width=530
    page.theme_mode=ft.ThemeMode.SYSTEM
    page.add(PrincipalGUI(page))

ft.app(main)