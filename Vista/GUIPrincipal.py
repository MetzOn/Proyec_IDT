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
        self.Imagen_Captura=ft.Image(src=False,width="100%")

        #TextField para el Registro de empleados
        self.tfNombreEmpleado=ft.TextField(hint_text="Ingrese su nombre",label="Nombres", height=40)
        self.tfApellidosEmpleado=ft.TextField(hint_text="Ingrese su apellido",label="Apellidos", height=40)
        self.tfIdEmpleado=ft.TextField(hint_text="ID: Se genera Automaticamente",disabled=True, height=40 )
        self.tfDniEmpleado=ft.TextField(hint_text="Ingrese su DNI",max_length=8,keyboard_type=ft.KeyboardType.NUMBER,label="DNI", height=50 )
        self.tfTelefonoEmpleado=ft.TextField(hint_text="Ingrese su teléfono",max_length=9,keyboard_type=ft.KeyboardType.PHONE,label="Telefono",height=50)
        self.cbTipoEmpleado=ft.Dropdown(label="Tipo de Empleado",hint_text="Seleccione el tipo de empleado",height=40,
        options=[
            ft.dropdown.Option(key="A", text="Administrador"),
            ft.dropdown.Option(key="B", text="Empleado")
            ]
        )
        self.cbPermisoDIngreso=ft.Dropdown(label="Permiso de ingreso", height=40 ,hint_text="Seleccione el tipo de permiso",
            options=[
            ft.dropdown.Option(key="1", text="Permitido"),
            ft.dropdown.Option(key="0", text="No permitido")
            ]
        )

        #BOTONES
        #BarNavegacion
        self.btnIconSalir=ft.IconButton(icon=ft.icons.OUTPUT)
        #Home- Reconocimeinto
        self.btnIniciarReconocimiento=ft.ElevatedButton(text="INICIAR") 
        self.btnFinalizarVideo=ft.ElevatedButton(text="FINALIZAR")    
        #Registro-Agregar nuevo empleado
        self.btnAgregarEmpleadoPanel=ft.ElevatedButton(expand=True,icon=ft.icons.GROUP_ADD,text="Agregar nuevo empleado",col={'md': 6, 'lg': 3},)                                
        self.btnCrearEmpleado=ft.ElevatedButton(icon=ft.icons.SUPERVISED_USER_CIRCLE_ROUNDED,text="Crear Perfil")
        self.btnTomarImagenes=ft.ElevatedButton(icon=ft.icons.PHOTO_CAMERA,text="Tomar imagenes",col={'md': 6, 'lg': 3})
        #Registro-AdministrarEmpleados
        self.btnAdministrarEmpleadosPanel=ft.ElevatedButton(icon=ft.icons.TABLE_VIEW,text="Administrar empleados",col={'md': 6, 'lg': 3})
        self.btnModificarEmpleado=ft.ElevatedButton(icon=ft.icons.UPDATE,text="Actualizar",col={'md': 6, 'lg': 3},)
        self.btnEliminarEmpleado=ft.ElevatedButton(icon=ft.icons.DELETE,text="Eliminar",col={'md': 6, 'lg': 3},)

        #TABLA
        #Registro-AdministrarEmpleados
        self.tbRegistroEmpleados=ft.DataTable(
            expand=True,
            border= ft.border.all(2,self.ColorFondoA),
            data_row_color={ft.MaterialState.SELECTED:"purple",
                            ft.MaterialState.PRESSED:"black"},
            border_radius=10,
            show_checkbox_column=True,
            columns=[
                ft.DataColumn(ft.Text("ID",color=self.ColorFondoA,weight="bold")),
                ft.DataColumn(ft.Text("Nombre",color=self.ColorFondoA,weight="bold")),
                ft.DataColumn(ft.Text("Apellido",color=self.ColorFondoA,weight="bold")),
                ft.DataColumn(ft.Text("DNI",color=self.ColorFondoA,weight="bold")),
                ft.DataColumn(ft.Text("Fecha Registro",color=self.ColorFondoA,weight="bold")),
                ft.DataColumn(ft.Text("Telefono",color=self.ColorFondoA,weight="bold")),
                ft.DataColumn(ft.Text("Tipo",color=self.ColorFondoA,weight="bold")),
                ft.DataColumn(ft.Text("Permiso",color=self.ColorFondoA,weight="bold")),
            ]
        )
        #SUBCONTENEDORES (REGISTRO):
        self.CtTomarImagenes=ft.Container(expand=True,alignment=ft.alignment.center, 
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=self.btnTomarImagenes
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        expand=True,
                        content=self.Imagen_Captura
                    ),
                    ft.Container(
                        alignment=ft.alignment.bottom_right,
                        content=self.btnCrearEmpleado

                    )
                                                    
                ]
            )
        )
        self.CtAdministarDatos=ft.Container(
            expand=True,alignment=ft.alignment.center, 
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Text(value="TABLA",style=ft.TextStyle(
                                color=ft.colors.WHITE,
                                size=18,
                                weight=ft.FontWeight.W_500,
                                font_family="Arial"))
                    ),
                    ft.Column(
                        expand=True,
                        scroll="auto",
                        controls=[
                            ft.ResponsiveRow(
                                controls=[
                                    self.tbRegistroEmpleados
                                    ]
                            )
                            
                        ]
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.ResponsiveRow(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                self.btnModificarEmpleado,
                                self.btnEliminarEmpleado
                            ]
                        )
                    ),
                ]
            )

        )

        #LISTAS- PARA CONTENEDORES
        #Lista- Registro(Agregar-Administrar)
        self.ContenedoresResgistro=[self.CtTomarImagenes,self.CtAdministarDatos]
        self.ContenedorRegistro= ft.Container(
            expand=True,
            col=11,
            content=self.ContenedoresResgistro[1],
        )
    #ME QUEDE AQUIIIIIIIIIIIIII, QUERIA VER EL TEMA DE CAMBIAR DE PANELES

        #PANELES PRINCIPALES (implementacion de componentes)
        #Navegacion
        self.Navegacion= ft.Container(col=1,bgcolor=self.ColorFondoN,on_change=self.change_page,border_radius= 10,
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
                                self.btnIconSalir,
                            ],  
                        )
                    ),
                ]
            )

        )
        
        #Home
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
                                        self.btnIniciarReconocimiento,
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
                                        self.btnFinalizarVideo,
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
                                self.btnAgregarEmpleadoPanel,
                                self.btnAdministrarEmpleadosPanel,
                            ]
                        )
                    ),
                    ft.Container(
                        height=200,
                        content=ft.ResponsiveRow(
                            alignment=ft.MainAxisAlignment.CENTER,
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
                                                ft.ResponsiveRow(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    expand=True,
                                                    controls=[
                                                        ft.Column(
                                                            col={'md': 3, 'lg':6 },
                                                            controls=[
                                                                self.cbTipoEmpleado
                                                            ]
                                                        ),
                                                        ft.Column(
                                                            col={'md': 3, 'lg':6 },
                                                            controls=[
                                                                self.cbPermisoDIngreso

                                                            ]
                                                            
                                                        ),
                                                    ]
                                                ),
                                                
                                            ]
                                        )
                                
                            ]

                        )
                    ),
                    self.ContenedorRegistro,
                ]
            )

        )

        #Se crean las Listas para navegar entre contenedores
        self.ContenedoresPrincipales=[self.Contenedor_Inicial_Home,self.Contenedor_Inicial_Registro]
        

        self.Paneles= ft.Container(
            expand=True,
            col=11,
            content=self.ContenedoresPrincipales[1],
        )

        self.Contenido= ft.ResponsiveRow(
            controls=[
                self.Navegacion,
                self.Paneles
            ]
        )


    def build(self):
        return self.Contenido
    
    def getNombreRegistro(self):
        return self.tfNombreEmpleado.value
    def getApellidoRegistro(self):
        return self.tfApellidosEmpleado.value
    def getDniRegistro(self):
        return self.tfDniEmpleado.value
    def getTipoEmpleadoRegistro(self):
        return self.cbTipoEmpleado.value
    def getPermisoIngresoRegistro(self):
        return self.cbPermisoDIngreso.value
    
    def change_page(self,e):
        index= e.control.selected_index

def main(page: ft.Page):
    page.window_min_height=820
    page.window_min_width=1100
    page.theme_mode=ft.ThemeMode.SYSTEM
    page.add(PrincipalGUI(page))

ft.app(main)