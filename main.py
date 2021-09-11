from re import TEMPLATE
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import sys
import webbrowser
import tablas
import datetime
from datetime import date
import folium



#GRAPHIC INTERFACE
class Examen:
    def __init__(self, ventana):
        self.window_root = ventana
        self.window_root.state(newstate = "normal")
        self.window_root.title("ANIME APP | BY: ROSMEIRY MARGARITA GARABITO MARIA | PROF: AMADIS SUAREZ")
        self.window_root.geometry("900x600+0+0")
        self.window_root.resizable(False,False)
        
        self.img_root = PhotoImage(file="items/ANIME.png")
        self.img_space = Label(self.window_root, image=self.img_root, bg="LightCyan4",width=900, height=593).place(x=0, y=0)

#WINDONW ROOT: BUTTONS
        self.button_character_window_gestion = ttk.Button(self.window_root, text= "Gestion De Personajes",width=30, command= self.open_gestion_character).place(x=245, y=375)
        self.button_report = ttk.Button(self.window_root, text= "Reportes",width=30, command= self.open_reports).place(x=200, y=420)
        self.button_config = ttk.Button(self.window_root, text= "Configuracion",width=30, command= self.open_configs).place(x=485, y=420)
        self.button_out = ttk.Button(self.window_root, text= "Salir",width=10, command= self.out).place(x=400, y=420)
        self.button_info = ttk.Button(self.window_root, text= "Acerca De",width=30, command=self.about).place(x=455, y=375)

#WINDOW_2: CHARACTERS GESTION
        self.window_2_characters = Toplevel()
        self.window_2_characters.state(newstate = "withdraw")
        self.window_2_characters.geometry("900x550+0+0")
        self.window_2_characters.title("GESTIONES")
        self.window_2_characters.configure(bg= "#31B189")
        self.window_2_characters.resizable(False,False)

#WINDOW_2: ALL THE LABELS AND BUTTONS
        self.img_space = Label(self.window_2_characters, bg="#FFCB72",width=900, height=593).place(x=0, y=0)
        self.insert_space = Label(self.window_2_characters, text= "DATOS PERSONALES DEL PERSONAJE (SOLO PERSONAJES DE ANIME)",bg="#31B189", fg='black', font=("Century", 16), width=60).place(x=50, y=20)

        self.name_space = Label(self.window_2_characters, text="Nombre",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=60)
        self.name_insert = Entry(self.window_2_characters, width=50)
        self.name_insert.place(x=140, y=65)
        self.name_insert.focus()
        
        self.last_name_space = Label(self.window_2_characters, text="Apellido",bg="#FFCB72",fg='black', font=("Century", 12)).place(x=50, y=85)
        self.last_name_insert = Entry(self.window_2_characters, width=50)
        self.last_name_insert.place(x=140, y=90)
        
        self.Photo_space = Label(self.window_2_characters, text="Url foto",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=110)
        self.Photo_insert = Entry(self.window_2_characters, width=50)
        self.Photo_insert.place(x=140, y=115)
        
        self.Pronunciation_space = Label(self.window_2_characters, text="Pronunciacion",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=135)
        self.Pronunciation_insert = Entry(self.window_2_characters, width=43)
        self.Pronunciation_insert.place(x=180, y=140)
        
        self.Date_space = Label(self.window_2_characters, text="Fecha Nacimiento",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=160)
        self.Date_insert = Entry(self.window_2_characters, width=40)
        self.Date_insert.place(x=200, y=165)

        self.Power_space = Label(self.window_2_characters, text="Poder",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=185)
        self.Power_insert = Entry(self.window_2_characters, width=53)
        self.Power_insert.place(x=120, y=190)
        
        self.Quote_space = Label(self.window_2_characters, text="Frase fav",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=210)
        self.Quote_insert = Entry(self.window_2_characters, width=43)
        self.Quote_insert.place(x=180, y=215)
        
        self.Genre_space = Label(self.window_2_characters, text="Genero",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=235)
        self.Genre_insert = Entry(self.window_2_characters, width=51)
        self.Genre_insert.place(x=130, y=240)
        
        self.high_space = Label(self.window_2_characters, text="Altura",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=260)
        self.high_insert = Entry(self.window_2_characters, width=51)
        self.high_insert.place(x=130, y=265)
        
        self.sex_space = Label(self.window_2_characters, text="Sexo",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=285)
        self.sex_insert = Entry(self.window_2_characters, width=54)
        self.sex_insert.place(x=110, y=290)
        
        self.state_space = Label(self.window_2_characters, text="Estado",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=310)
        self.state_insert = Entry(self.window_2_characters, width=51)
        self.state_insert.place(x=130, y=315)
        
        self.direction_space = Label(self.window_2_characters, text="Direccion",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=335)
        self.direction_insert = Entry(self.window_2_characters, width=40)
        self.direction_insert.place(x=130, y=340)
        
        self.latitude_space = Label(self.window_2_characters, text="latitud",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=360)
        self.latitude_insert = Entry(self.window_2_characters, width=40)
        self.latitude_insert.place(x=130, y=365)
        
        self.longitude_space = Label(self.window_2_characters, text="longitud",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=385)
        self.longitude_insert = Entry(self.window_2_characters, width=40)
        self.longitude_insert.place(x=130, y=390)
               
        self.description_space = Label(self.window_2_characters, text="Ropa descripcion", width=33,bg="#FFCB72", fg='black', font=("Century", 12)).place(x=10, y=430)
        self.description_insert = Entry(self.window_2_characters, width=55)
        self.description_insert.place(x=20, y=470)
        
        self.animeId_space = Label(self.window_2_characters, text="ID",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=570, y=65)
        self.animeId_insert = Entry(self.window_2_characters, width=37)
        self.animeId_insert.place(x=615, y=70)

        self.gestion_container = LabelFrame(self.window_2_characters, text="INGRESA UN ID DE ANIME PARA ESCOGER")
        self.gestion_container.place(x=500, y=100,width=340, height=380)
        self.scroll_p = Scrollbar(self.gestion_container) 
        self.scroll_p.pack(side = RIGHT, fill = Y)
        self.list_p = Listbox(self.gestion_container, yscrollcommand = self.scroll_p.set, width=70, height="100")
        self.list_p.pack()
        
        self.button_insert = Button(self.window_2_characters,width=30, command=self.insert_characters_c, text="Insert").place(x=440, y=485)
        self.button_menu = Button(self.window_2_characters,command=self.open_menu_root, width=30, text="Back").place(x=670, y=485)
        self.button_modify = Button(self.window_2_characters,command=self.open_gestion_modify, width=30, text="Modify").place(x=440, y=520)
        self.button_delete = Button(self.window_2_characters, command=self.open_gestion_delete, width=30, text="Delete").place(x=670, y=520)
        
#WINDOW_3: MODIFY CHARACTERS 
        self.window_modify_character = Toplevel()
        self.window_modify_character.state(newstate = "withdraw")
        self.window_modify_character.geometry("1200x650+0+0")
        self.window_modify_character.title("MODIFY CHARACTERS")
        self.window_modify_character.configure(bg= "#FFCB72")
        self.window_modify_character.resizable(False,False)
        
        self.modify_character_space = Label(self.window_modify_character, text= "MODIFICA LOS DATOS DE CUALQUIER PERSONAJE",bg="#31B189", fg='white', font=("Century", 16), width=60).place(x=250, y=10)

#DRAWING LABELS AND BUTTONS       
        self.modify_name_space = Label(self.window_modify_character , text="Nombre",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=260, y=200)
        self.modify_name_insert = Entry(self.window_modify_character , width=50)
        self.modify_name_insert.place(x=340, y=205)
        self.modify_name_insert.focus()
        
        self.last_name_space  = Label(self.window_modify_character , text="Apellido",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=260, y=230)
        self.last_name_insert_modify  = Entry(self.window_modify_character , width=50)
        self.last_name_insert_modify.place(x=340, y=230)
        
        self.Photo_space  = Label(self.window_modify_character, text="url Foto",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=260, y=260)
        self.Photo_modify_insert  = Entry(self.window_modify_character, width=50)
        self.Photo_modify_insert.place(x=340, y=260)
        
        self.pronunciation_modify_space = Label(self.window_modify_character, text="Pronunciacion",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=220, y=290)
        self.pronunciation_modify_insert = Entry(self.window_modify_character, width=43)
        self.pronunciation_modify_insert.place(x=340, y=290)
        
        self.date_modify_space = Label(self.window_modify_character, text="Fecha Nacimiento",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=190, y=320)
        self.date_modify_insert = Entry(self.window_modify_character, width=40)
        self.date_modify_insert.place(x=340, y=320)
        
        self.power_modify = Label(self.window_modify_character, text="Poder",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=270, y=350)
        self.power_modify_insert = Entry(self.window_modify_character, width=53)
        self.power_modify_insert.place(x=340, y=350)
        
        self.quote_modify_space = Label(self.window_modify_character, text="Frase Favorita",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=210, y=380)
        self.quote_modify_insert = Entry(self.window_modify_character, width=43)
        self.quote_modify_insert.place(x=340, y=380)
        
        self.genre_modify_space = Label(self.window_modify_character, text="Genero",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=270, y=410)
        self.genre_modify_insert = Entry(self.window_modify_character, width=51)
        self.genre_modify_insert.place(x=340, y=410)
        
        self.high_modify_space = Label(self.window_modify_character, text="Altura",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=270, y=440)
        self.high_modify_insert = Entry(self.window_modify_character, width=51)
        self.high_modify_insert.place(x=340, y=440)
        
        self.sex_direction_space = Label(self.window_modify_character, text="Sexo",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=280, y=470)
        self.sex_modify_insert = Entry(self.window_modify_character, width=54)
        self.sex_modify_insert.place(x=340, y=470)
        
        self.state_modify_space = Label(self.window_modify_character, text="Estado",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=265, y=500)
        self.state_modify_insert = Entry(self.window_modify_character, width=51)
        self.state_modify_insert.place(x=340, y=500)
        
        self.direction_modify_space = Label(self.window_modify_character, text="Direccion",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=260, y=530)
        self.direction_modify_insert = Entry(self.window_modify_character, width=40)
        self.direction_modify_insert.place(x=340, y=530)
        
        self.latitude_modify_space = Label(self.window_modify_character, text="Latitud",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=265, y=560)
        self.latitud_modify_insert = Entry(self.window_modify_character, width=40)
        self.latitud_modify_insert.place(x=340, y=560)
        
        self.longitude_modify_space = Label(self.window_modify_character, text="Longitud",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=265, y=590)
        self.longitude_modify_insert = Entry(self.window_modify_character, width=40)
        self.longitude_modify_insert.place(x=340, y=590)
               
        self.description_modify_space = Label(self.window_modify_character, text="Descripcion de la ropa", width=33,bg="#FFCB72", fg='black', font=("Century", 12)).place(x=720, y=460)
        self.description_modify_insert = Entry(self.window_modify_character, width=55)
        self.description_modify_insert.place(x=720, y=500, height=100)

        self.gestion_container_modify = LabelFrame(self.window_modify_character, text="Listas de anime: Elija el ID del anime de su personaje")
        self.gestion_container_modify.place(x=300, y=70,width=340, height=110)
        self.scroll_p_modificar = Scrollbar(self.gestion_container) 
        self.scroll_p_modificar.pack(side = RIGHT, fill = Y)
        self.list_p_modificar = Listbox(self.gestion_container_modify, yscrollcommand = self.scroll_p.set, width=70)
        self.list_p_modificar.pack()
        
        self.animeId_modify_space = Label(self.window_modify_character, text="Id Anime",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=150, y=80)
        self.animeId_modify_insert = Entry(self.window_modify_character, width=6)
        self.animeId_modify_insert.place(x=230, y=80)
        
        self.animeId_modify_character_space = Label(self.window_modify_character, text="Id Personaje",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=150, y=120)
        self.animeId_modify_character_space = Entry(self.window_modify_character, width=6)
        self.animeId_modify_character_space.place(x=250, y=120)
        
        self.gestion_container2_modify = LabelFrame(self.window_modify_character, text="Listado de personajes")
        self.gestion_container2_modify.place(x=680, y=50,width=405, height=390)
        self.scroll_gm = Scrollbar(self.gestion_container2_modify) 
        self.scroll_gm.pack(side = RIGHT, fill = Y)
        self.scroll_gm_h = Scrollbar(self.gestion_container2_modify, orient= HORIZONTAL) 
        self.scroll_gm_h.pack(side = BOTTOM, fill = X)
        self.mylist_gm = Listbox(self.gestion_container2_modify, xscrollcommand=self.scroll_gm_h.set, yscrollcommand=self.scroll_gm, width=70, height=20)
        self.mylist_gm.pack()
        
        self.scroll_gm_h.config(command=self.mylist_gm.xview)
        self.scroll_gm.config(command=self.mylist_gm.yview)
    
        self.button_insert_modify = Button(self.window_modify_character,width=30, command=self.gestion_character_modify_c, text="Modificar", font=("Times New Roman", 12)).place(x=600, y=610)
        self.button_menu_modify = Button(self.window_modify_character,width=30, command=self.open_gestion_character,text="Regresar", font=("Times New Roman", 12)).place(x=900, y=610)
        
#WINDOW_4: DELETE CHARACTERS
        self.delete_character_window = Toplevel()
        self.delete_character_window .state(newstate = "withdraw")
        self.delete_character_window .geometry("520x600+0+0")
        self.delete_character_window .title("ELIMINAR PERSONAJES")
        self.delete_character_window .configure(bg= "#FFCB72")
        self.delete_character_window .resizable(False,False)
        
        self.img_delete_space  = Label(self.delete_character_window,bg="#31B189",width=900, height=593).place(x=0, y=0)
        self.insert_delete_space  = Label(self.delete_character_window , text= "ELIMINE UN PERSONAJE",bg="#FFCB72", fg='black', font=("Century", 16), width=32).place(x=50, y=50)  
        
        self.gestion_container_delete2 = LabelFrame(self.delete_character_window, text="LISTA DE PERSONAJES", fg="black", bg="#FFCB72")
        self.gestion_container_delete2.place(x=50, y=90,width=418, height=385)
        self.scroll_ge = Scrollbar(self.gestion_container_delete2) 
        self.scroll_ge.pack(side = RIGHT, fill = Y)
        self.scroll_ge_h = Scrollbar(self.gestion_container_delete2, orient= HORIZONTAL) 
        self.scroll_ge_h.pack(side = BOTTOM, fill = X)
        self.list_ge = Listbox(self.gestion_container_delete2, xscrollcommand=self.scroll_ge_h.set, yscrollcommand=self.scroll_ge, width=70, height=20)
        self.list_ge.pack()
        
        self.scroll_ge_h.config(command=self.list_ge.xview)
        self.scroll_ge.config(command=self.list_ge.yview)
        
        self.animeId_delete_space = Label(self.delete_character_window, text="ID PERSONAJE",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=490)
        self.animeId_delete_space = Entry(self.delete_character_window, width=45)
        self.animeId_delete_space.place(x=190, y=490)
        
        self.button_insert_delete = Button(self.delete_character_window,width=20, text="Eliminar" , command=self.delete_characters_e).place(x=100, y=525)
        self.button_menu_delete = Button(self.delete_character_window,width=20, text="Regresar" , command=self.open_gestion_character).place(x=280, y=525)
        
#WINDOW_5: REPORTS
        self.window_reports = Toplevel()
        self.window_reports.state(newstate = "withdraw")
        self.window_reports.geometry("900x600+0+0")
        self.window_reports.title("REPORTES")
        self.window_reports.configure(bg= "#31B189")
        self.window_reports.resizable(width=False, height=False)
        
        self.img_space = Label(self.window_reports, bg="#FFCB72",width=900, height=593).place(x=0, y=0)
        self.report_space = Label(self.window_reports, text= "LISTADO DE PERSONAJES",bg="#31B189", fg='black', font=("Times New Roman", 16), width=31).place(x=250, y=50)
        
        self.button_list = Button(self.window_reports,width=40, command=self.list_of_characters, text="LISTAR").place(x=25, y=150)
        self.button_zodiac = Button(self.window_reports, width=40, command=self.list_of_characters_zodiac, text="SIGNOS").place(x=40, y=200)
        self.button_map = Button(self.window_reports,width=40, command=self.map, text="MAPA").place(x=55, y=250)
        self.button_html = Button(self.window_reports,width=40, command=self.report_html_i, text="HTML").place(x=65, y=300)
        self.button_anime = Button(self.window_reports,width=40, command=self.list_of_characters_anime, text="ANIME").place(x=75, y=350)
        self.buttom_state = Button(self.window_reports,width=40, command=self.list_of_characters_state, text="ESTADO").place(x=85, y=400)
        
        self.animeId_space_report = Label(self.window_reports, text="Id Personaje || HTML",bg="#31B189", fg='white', font=("Century", 12)).place(x=120, y=550)
        self.animeId_insert_report = Entry(self.window_reports, width=15)
        self.animeId_insert_report.place(x=335, y=550)
        self.animeId_insert_report.focus()
        
        self.report_container = LabelFrame(self.window_reports, text="REPORTE DE PERSONAJES", bg="#31B189")
        self.report_container.place(x=450, y=100,width=405, height=390)
        self.scroll_r = Scrollbar(self.report_container) 
        self.scroll_r.pack(side = RIGHT, fill = Y)
        self.list_r = Listbox(self.report_container, yscrollcommand = self.scroll_r.set, width=70, height=20)
        self.list_r.pack()
        self.button_menu_report = ttk.Button(self.window_reports,width=40, command=self.open_menu_root, text="MENU PRINCIPAL").place(x=450, y=495)

#WINDOW_6: CONFIG
        self.window_config = Toplevel()
        self.window_config.state(newstate = "withdraw")
        self.window_config.geometry("460x580+0+0")
        self.window_config.title("Configuraciones")
        self.window_config.configure(bg= "#31B189")
        self.window_config.resizable(width=False, height=False)

        self.config_img = PhotoImage(file="items/config.png")
        self.space_config_img = Label(self.window_config, image=self.config_img ,bg="#31B189", fg="black" ,width=460, height=600).place(x=0, y=0)

        self.button_insert_config = Button(self.window_config,width=30, text="Agregar" ,command=self.open_configs_insert).place(x=120, y=240)
        self.button_html_config = Button(self.window_config,width=30,text="Modificar" ,command=self.open_configs_modify).place(x=120, y=300)
        self.button_delete_config = Button(self.window_config,width=30, text="Eliminar" , command=self.open_configs_delete).place(x=120, y=360)
        self.button_state_config = Button(self.window_config,width=30, text="Regresar", command=self.open_menu_root).place(x=120, y=420)
        
#WINDOW_7: CONFIG_INSERT
        self.Window_config_insert_i = Toplevel()
        self.Window_config_insert_i.state(newstate = "withdraw")
        self.Window_config_insert_i.geometry("460x600+0+0")
        self.Window_config_insert_i.title("AGREGAR")
        self.Window_config_insert_i.configure(bg= "#31B189")
        self.Window_config_insert_i.resizable(False,False)
        
        self.background_img = PhotoImage(file = "items/Agregar.png")
        
        self.space_config_img = Label(self.Window_config_insert_i, image=self.background_img, bg="Gray",width=460, height=540).place(x=0, y=0)

        self.name_space_config = Label(self.Window_config_insert_i, text="Nombre/Anime",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=80, y=160)
        self.name_insert_config = Entry(self.Window_config_insert_i, width=30)
        self.name_insert_config.place(x=210, y=160)
        self.name_insert_config.focus() 
        
        self.state_space_config = Label(self.Window_config_insert_i, text="Estado/Anime",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=80, y=230)
        self.state_insert_config = Entry(self.Window_config_insert_i, width=30)
        self.state_insert_config.place(x=210, y=230)

        self.genre_space_config = Label(self.Window_config_insert_i, text="Genero/Anime",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=80, y=300)
        self.genre_insert_config = Entry(self.Window_config_insert_i, width=30)
        self.genre_insert_config.place(x=210, y=300)
        
        self.button_agregarnew = Button(self.Window_config_insert_i,width=30, command=self.insert_anime, text="Agregar").place(x=120, y=400)
        self.button_agregarneww = Button(self.Window_config_insert_i,width=30, command=self.open_configs, text="Volver").place(x=120, y=440)
        
#WINDOW_8: CONFIG_MODIFY
        self.window_config_modify = Toplevel()
        self.window_config_modify.state(newstate = "withdraw")
        self.window_config_modify.geometry("460x600+0+0")
        self.window_config_modify.title("Configuraciones Agregar")
        self.window_config_modify.configure(bg= "#31B189")
        self.window_config_modify.resizable(False,False)
        
        self.background_img_config_modify = PhotoImage(file = "items/Modificar.png")
        
        self.space_config_img = Label(self.window_config_modify, image=self.background_img_config_modify, bg="LightCyan4",width=460, height=540).place(x=0, y=0)
        
        self.container_modify = LabelFrame(self.window_config_modify , text="ELIGE UN ID PARA PODER MODIFICAR LOS DATOS")
        self.container_modify.place(x=55, y=100,width=350, height=150)
        self.scroll_m = Scrollbar(self.container_modify) 
        self.scroll_m.pack(side = RIGHT, fill = Y)
        self.list_m = Listbox(self.container_modify, yscrollcommand = self.scroll_m.set, width=70, height=20)
        self.list_m.pack()
        
        self.space_modify_name_s = Label(self.window_config_modify, text="ID Del Anime",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=260)
        self.insert_modify_name_i = Entry(self.window_config_modify, width=30)
        self.insert_modify_name_i.place(x=200, y=265)
        self.insert_modify_name_i.focus() 
        
        self.modify_name_space = Label(self.window_config_modify, text="Nombre Del Anime",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=300)
        self.insert_name_modify = Entry(self.window_config_modify, width=30)
        self.insert_name_modify.place(x=200, y=305)
        
        self.state_modify_space = Label(self.window_config_modify, text="Estado Del Anime",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=340)
        self.state_insert_modify = Entry(self.window_config_modify, width=30)
        self.state_insert_modify.place(x=200, y=345)

        self.genre_space_modify = Label(self.window_config_modify, text="Genero Del Anime",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=50, y=380)
        self.genre_insert_modify = Entry(self.window_config_modify, width=30)
        self.genre_insert_modify.place(x=200, y=385)

        self.button_modificarnew = Button(self.window_config_modify ,width=30, command= self.modify_anime, text="Modificar").place(x=120, y=450)
        self.button_modificarneww = Button(self.window_config_modify,width=30, command=self.open_configs, text="Volver").place(x=120, y=500)

#WINDOW_9: CONFIG_DELETE
        self.window_config_delete = Toplevel()
        self.window_config_delete.state(newstate = "withdraw")
        self.window_config_delete.geometry("500x540+0+0")
        self.window_config_delete.title("Agregar")
        self.window_config_delete.configure(bg="#31B189")
        self.window_config_delete.resizable(width=False, height=False)
        
        self.img_window_config_delete_background = PhotoImage(file = "items/Eliminar.png")
        self.space_config_img = Label(self.window_config_delete, image=self.img_window_config_delete_background, bg="#31B189",width=500, height=575).place(x=0, y=0)

        self.delete_container = LabelFrame(self.window_config_delete, text="Ingresa ID para eliminar anime")
        self.delete_container.place(x=55, y=150,width=400, height=250)
        self.scroll_e = Scrollbar(self.delete_container) 
        self.scroll_e.pack(side = RIGHT, fill = Y)
        self.list_e = Listbox(self.delete_container, yscrollcommand = self.scroll_e.set, width=70, height=20)
        self.list_e.pack()
        
        
        self.lavel_name_delete_id = Label(self.window_config_delete, text="ID/Anime",bg="#FFCB72", fg='black', font=("Century", 12)).place(x=80, y=410)
        self.insert_name_delete_id = Entry(self.window_config_delete, width=30)
        self.insert_name_delete_id.place(x=180, y=415)
        self.insert_name_delete_id.focus() 
        
        self.button_eliminarnew = Button(self.window_config_delete,width=40, command=self.delete_anime, text="Eliminar").place(x=120, y=445)
        self.button_eliminarneww = Button(self.window_config_delete,width=40, command=self.open_configs, text="Volver").place(x=120, y=480)
        
       
       
        
#FUNCTIONS FOR ALL THE WINDOWS
    def open_gestion_delete(self):
        self.delete_character_window.state(newstate="normal") 
        self.window_2_characters.state(newstate= "withdraw") 
         
        self.list_ge.delete(0, END)
        for i in tablas.Personajes.select():
            self.list_ge.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre + " Apellido: " + i.apellido + " Fecha de nacimiento" + i.fecha_nacimiento + " Latitud" + str(i.latitud) + " Longitud" + str(i.longitud))                                                       
          
    def open_gestion_modify(self):
        self.window_modify_character.state(newstate="normal") 
        self.window_2_characters.state(newstate= "withdraw") 
        
        self.mylist_gm.delete(0, END)
        for i in tablas.Personajes.select():
            self.mylist_gm.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre + " Apellido: " + i.apellido + " Fecha de nacimiento" + i.fecha_nacimiento + " Latitud" + str(i.latitud) + " Longitud" + str(i.longitud))                                                       
        
        
        self.list_p_modificar.delete(0, END)
        for i in tablas.Anime.select():
            self.list_p_modificar.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre)    
        
    def open_menu_root(self):
        self.window_root.state(newstate="normal") 
        self.window_2_characters.state(newstate= "withdraw")
        self.window_reports.state(newstate= "withdraw")
        self.window_config.state(newstate= "withdraw")
    
    def open_gestion_character(self):
        self.window_2_characters.state(newstate="normal") 
        self.window_modify_character.state(newstate= "withdraw")
        self.delete_character_window.state(newstate= "withdraw")
        self.window_root.state(newstate= "withdraw")

        self.list_p.delete(0, END)
        for i in tablas.Anime.select():
            self.list_p.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre) 
    
    def open_reports(self):
        self.window_reports.state(newstate="normal") 
        self.window_root.state(newstate= "withdraw")
        
    def open_configs(self):
        self.window_config.state(newstate="normal") 
        self.window_root.state(newstate= "withdraw")
        self.Window_config_insert_i.state(newstate= "withdraw")
        self.window_config_modify.state(newstate= "withdraw")
        self.window_config_delete.state(newstate= "withdraw")
        
    def open_configs_insert(self):
        self.Window_config_insert_i.state(newstate="normal") 
        self.window_config.state(newstate= "withdraw")
        
    def open_configs_modify(self):
        self.window_config_modify.state(newstate="normal") 
        self.window_config.state(newstate= "withdraw")
        
        self.list_m.delete(0, END)
        for i in tablas.Anime.select():
            self.list_m.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre) 
        
    def open_configs_delete(self):
        self.window_config_delete.state(newstate="normal") 
        self.window_config.state(newstate= "withdraw")
        
        self.list_e.delete(0, END)
        for i in tablas.Anime.select():
            self.list_e.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre) 

    def out(self):
        sys.exit()
        
    def about(self):
        url = "https://youtu.be/8bfBSy5fUPI"
        webbrowser.open(url)
            
#ALL THE DATA
    def validate_anime(self):
        if len(self.name_insert_config.get()) > 0 and len(self.state_insert_config.get()) > 0 and len(self.genre_insert_config.get()) > 0:
            return True
        else:
            return False
        
    def validate_anime_modify(self):
        if len(self.insert_name_modify.get()) > 0 and len(self.state_insert_modify.get()) > 0 and len(self.genre_insert_modify.get()) > 0:
            return True
        else:
            return False

    def validate_character(self):
        if len(self.name_insert.get()) > 0 and len(self.last_name_insert.get()) > 0 and len(self.Photo_insert.get()) > 0 and len(self.Pronunciation_insert.get()) > 0 and len(self.Date_insert.get()) > 0 and len(self.Power_insert.get()) > 0 and len(self.Quote_insert.get()) > 0 and len(self.Genre_insert.get()) > 0 and len(self.high_insert.get()) > 0 and len(self.sex_insert.get()) > 0 and len(self.state_insert.get()) > 0 and len(self.direction_insert.get()) > 0 and len(self.latitude_insert.get()) > 0 and len(self.longitude_insert.get()) > 0 and len(self.animeId_insert.get()) > 0 and len(self.description_insert.get()) > 0:
            return True
        else:
            return False
        
    def validate_character_modify(self):
        if len(self.animeId_modify_insert.get()) > 0 and len(self.latitud_modify_insert.get()) > 0 and len(self.longitude_modify_insert.get()) > 0 and len(self.animeId_modify_character_space.get()) > 0 and len(self.date_modify_insert.get()) > 0 and len(self.modify_name_insert.get()) > 0 and len(self.last_name_insert_modify.get()) > 0 and len(self.Photo_modify_insert.get()) > 0 and len(self.pronunciation_modify_insert.get()) > 0 and len(self.power_modify_insert.get()) > 0 and len(self.quote_modify_insert.get()) > 0 and len(self.genre_modify_insert.get()) > 0 and len(self.high_modify_insert.get()) > 0 and len(self.sex_modify_insert.get()) > 0 and len(self.state_modify_insert.get()) > 0 and len(self.direction_modify_insert.get()) > 0 and len(self.description_modify_insert.get()) > 0:
            return True
        else: 
            return False
     
#GESTION ANIME 
    def insert_anime(self):
        if self.validate_anime():
            self.serie = tablas.Anime()
            self.serie.nombre = self.name_insert_config.get()
            self.serie.estado = self.state_insert_config.get()
            self.serie.genero = self.genre_insert_config.get()
            self.serie.save()
            
            self.name_insert_config.delete(0, END)
            self.state_insert_config.delete(0, END)
            self.genre_insert_config.delete(0, END)
            self.name_insert_config.focus()
        else:
            messagebox.showwarning(message ="Todos los datos son requeridos", title="ERROR")
    
    def modify_anime(self):
        if self.validate_anime_modificar():
            try:
                self.comparador = int(self.insert_modify_name_i.get())
                try:
                    self.serie = tablas.Anime.select().where(tablas.Anime.id == self.comparador).get()
                    self.serie.nombre = self.insert_name_modify.get()
                    self.serie.estado = self.state_insert_modify.get()
                    self.serie.genero = self.genre_insert_modify.get()
                    self.serie.save()
                    
                    self.insert_name_modify.delete(0, END)
                    self.state_insert_modify.delete(0, END)
                    self.genre_insert_modify.delete(0, END)
                    self.insert_modify_name_i.delete(0, END)
                    self.insert_modify_name_i.focus()
                    self.list_m.delete(0, END)
                    for i in tablas.Anime.select():
                        self.list_m.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre) 
                    
                except:
                     messagebox.showwarning(message ="El ID digitado no existe en la base de datos", title="ERROR")
            except:
                messagebox.showwarning(message ="Digite un Numero entero en el campo ID del anime", title="ERROR")
        else:
            messagebox.showwarning(message ="Todos los datos son requeridos", title="ERROR")
        
    def delete_anime(self):
        try:
            self.comparar = int(self.insert_name_delete_id.get())
            try:
                self.serie = tablas.Anime.select().where(tablas.Anime.id == self.comparar).get()
                messagebox.showinfo(message="Serie Eliminada", title="INFORMATION")
                self.serie.delete_instance()
                
                self.list_e.delete(0, END)
                for i in tablas.Anime.select():
                    self.list_e.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre) 
                self.insert_name_delete_id.delete(0, END)
                self.insert_name_delete_id.focus()
            except:
                messagebox.showwarning(message="El Id del anime que digito no existe", title="ERROR")
                
        except:
            messagebox.showwarning(message="Digite un numero entero porfavor ", title="ERROR") 
          
#GESTION CHARACTERS
    def insert_characters_c(self): 
        if self.validate_character():
            try:
                self.animeid = int(self.animeId_insert.get())
                self.latitud = float(self.latitude_insert.get())
                self.longitud = float(self.longitude_insert.get())
                
                try:
                    self.anime = tablas.Anime.select().where(tablas.Anime.id == self.animeid).get()
                    self.serie = tablas.Personajes()
                    try:
                        self.fecha_naci = datetime.datetime.strptime(self.Date_insert.get(), '%d/%m/%Y')
                        self.serie.nombre = self.name_insert.get()
                        self.serie.apellido = self.last_name_insert.get()
                        self.serie.foto_url = self.Photo_insert.get()
                        self.serie.pornunciacion = self.Pronunciation_insert.get()
                        self.serie.fecha_nacimiento = self.fecha_naci
                        self.serie.poder = self.Power_insert.get()
                        self.serie.frase_favorita = self.Quote_insert.get()
                        self.serie.genero = self.Genre_insert.get()
                        self.serie.altura = self.high_insert.get()
                        self.serie.sexo = self.sex_insert.get()
                        self.serie.estado = self.state_insert.get()
                        self.serie.direccion = self.direction_insert.get()
                        self.serie.latitud = self.latitud
                        self.serie.longitud = self.longitud
                        
                        self.serie.serie_F_K = self.anime
                        self.serie.vestimenta = self.description_insert.get()
                        
                        #Calculando la edad
                        self.fechaActual = datetime.datetime.now()

                        self.fecha_nacimiento_str = self.serie.fecha_nacimiento

                        self.fecha_naci

                        fechaActual_mes = self.fechaActual.month - self.fecha_naci.month
                        fechaActual_dias = self.fechaActual.day - self.fecha_naci.day

                        if fechaActual_mes >= 0 and fechaActual_dias >= 0:
                            self.edad = self.fechaActual.year - self.fecha_naci.year

                        else:
                            self.edad = self.fechaActual.year - self.fecha_naci.year  
                            self.edad = self.edad - 1
                                       
                        self.serie.edad = self.edad
                        #Calculando la Edad
                        
                        #Calculando el signo
                        if int(self.fecha_naci.month) == 3 and int(self.fecha_naci.day) >= 21 or int(self.fecha_naci.month) == 4 and int(self.fecha_naci.day) <= 20:
                            self.signo_zodiacal_1 = "Aries"
                        elif int(self.fecha_naci.month) == 4 and int(self.fecha_naci.day) >= 21 or int(self.fecha_naci.month) == 5 and int(self.fecha_naci.day) <= 21:
                            self.signo_zodiacal_1 = "Tauro"
                        elif int(self.fecha_naci.month) == 5 and int(self.fecha_naci.day) >= 22 or int(self.fecha_naci.month) == 6 and int(self.fecha_naci.day) <= 22:
                            self.signo_zodiacal_1 = "Geminis"
                        elif int(self.fecha_naci.month) == 6 and int(self.fecha_naci.day) >= 23 or int(self.fecha_naci.month) == 7 and int(self.fecha_naci.day) <= 23:
                            self.signo_zodiacal_1 = "Cancer"
                        elif int(self.fecha_naci.month) == 7 and int(self.fecha_naci.day) >= 24 or int(self.fecha_naci.month) == 8 and int(self.fecha_naci.day) <= 23:
                            self.signo_zodiacal_1 = "Leo"
                        elif int(self.fecha_naci.month) == 8 and int(self.fecha_naci.day) >= 24 or int(self.fecha_naci.month) == 9 and int(self.fecha_naci.day) <= 23:
                            self.signo_zodiacal_1 = "Virgo"
                        elif int(self.fecha_naci.month) == 9 and int(self.fecha_naci.day) >= 24 or int(self.fecha_naci.month) == 10 and int(self.fecha_naci.day) <= 23:
                            self.signo_zodiacal_1 = "Libra"
                        elif int(self.fecha_naci.month) == 10 and int(self.fecha_naci.day) >= 24 or int(self.fecha_naci.month) == 11 and int(self.fecha_naci.day) <= 22:
                            self.signo_zodiacal_1 = "Escorpio"
                        elif int(self.fecha_naci.month) == 11 and int(self.fecha_naci.day) >= 23 or int(self.fecha_naci.month) == 12 and int(self.fecha_naci.day) <= 21:
                            self.signo_zodiacal_1 = "Sagitario"
                        elif int(self.fecha_naci.month) == 12 and int(self.fecha_naci.day) >= 22 or int(self.fecha_naci.month) == 1 and int(self.fecha_naci.day) <= 20:
                            self.signo_zodiacal_1 = "Capricornio"
                        elif int(self.fecha_naci.month) == 1 and int(self.fecha_naci.day) >= 21 or int(self.fecha_naci.month) == 2 and int(self.fecha_naci.day) <= 19:
                            self.signo_zodiacal_1 = "Acuario"
                        elif int(self.fecha_naci.month) == 2 and int(self.fecha_naci.day) >= 20 or int(self.fecha_naci.month) == 3 and int(self.fecha_naci.day) <= 20:
                            self.signo_zodiacal_1 = "Acuario"
                        
                        self.serie.signo_zodiacal = self.signo_zodiacal_1

                        #Calculando el signo
                        
                        self.serie.save()
                        
                        self.name_insert_config.delete(0, END)
                        self.name_insert_config.focus()
                        self.name_insert.delete(0, END)
                        self.last_name_insert.delete(0, END)
                        self.Photo_insert.delete(0, END)
                        self.Pronunciation_insert.delete(0, END)
                        self.Date_insert.delete(0, END)
                        self.Power_insert.delete(0, END)
                        self.Quote_insert.delete(0, END)
                        self.Genre_insert.delete(0, END)
                        self.high_insert.delete(0, END)
                        self.sex_insert.delete(0, END)
                        self.state_insert.delete(0, END)
                        self.direction_insert.delete(0, END)
                        self.latitude_insert.delete(0, END)
                        self.longitude_insert.delete(0, END)
                        self.animeId_insert.delete(0, END)
                        self.description_insert.delete(0, END)
                    except:
                        messagebox.showwarning(message ="Solo puede ingresar fechas de nacimientos\ncon el siguiente formato DD/MM/AA", title="ERROR")
                        self.Date_insert.delete(0, END)
                except:
                    messagebox.showwarning(message ="El anime cuyo ID fue dijitado no existe\nSi El Anime de supersonaje no existe ne la base de datos agreguelo primero", title="ERROR")
                    self.animeId_insert.delete(0, END)
            except:
                messagebox.showwarning(message ="Digite un Numero entero en el campo 'ID del Anime'\nDigite numeros validos en los campos Latitud y Longitud", title="ERROR")
                self.animeId_insert.delete(0, END)
                self.longitude_insert.delete(0, END)
                self.latitude_insert.delete(0, END)
        else:
            messagebox.showwarning(message ="Todos los datos son requeridos", title="ERROR")
            
    def gestion_character_modify_c(self):
        if self.validate_character_modify():
            try:
                self.animeid_m = int(self.animeId_modify_insert.get())
                self.latitud_m = float(self.latitud_modify_insert.get())
                self.longitud_m = float(self.longitude_modify_insert.get())
                self.personajeid_m = int(self.animeId_modify_character_space.get())
                
                try:
                    self.anime = tablas.Anime.select().where(tablas.Anime.id == self.animeid_m).get()
                    self.personas = tablas.Personajes.select().where(tablas.Personajes.id == self.personajeid_m).get()
                    try:
                        self.fecha_nacii = datetime.datetime.strptime(self.date_modify_insert.get(),'%d/%m/%Y')
                        self.personas.nombre = self.modify_name_insert.get()
                        self.personas.apellido = self.last_name_insert_modify.get()
                        self.personas.foto_url = self.Photo_modify_insert.get()
                        self.personas.pornunciacion = self.pronunciation_modify_insert.get()
                        self.personas.fecha_nacimiento = self.fecha_nacii
                        self.personas.poder = self.power_modify_insert.get()
                        self.personas.frase_favorita = self.quote_modify_insert.get()
                        self.personas.genero = self.genre_modify_insert.get() 
                        self.personas.altura = self.high_modify_insert.get()
                        self.personas.sexo = self.sex_modify_insert.get()
                        self.personas.estado = self.state_modify_insert.get()
                        self.personas.direccion = self.direction_modify_insert.get()
                        self.personas.latitud = self.latitud_m
                        self.personas.longitud = self.longitud_m 
                        self.personas.serie_F_K = self.anime
                        self.personas.vestimenta = self.description_modify_insert.get()
                        
                        #Calculando la edad
                        self.fechaActual = datetime.datetime.now()

                        self.fecha_nacimiento_str = self.personas.fecha_nacimiento

                        self.fecha_nacii

                        self.fechaActual_mes = self.fechaActual.month - self.fecha_nacii.month
                        self.fechaActual_dias = self.fechaActual.day - self.fecha_nacii.day

                        if self.fechaActual_mes >= 0 and self.fechaActual_dias >= 0:
                            self.edad = self.fechaActual.year - self.fecha_nacii.year

                        else:
                            self.edad = self.fechaActual.year - self.fecha_nacii.year  
                            self.edad = self.edad - 1
                                        
                        self.personas.edad = self.edad
                        #Calculando la Edad
                        
                        #Calculando el signo
                        if int(self.fecha_nacii.month) == 3 and int(self.fecha_nacii.day) >= 21 or int(self.fecha_nacii.month) == 4 and int(self.fecha_nacii.day) <= 20:
                            self.signo_zodiacal_2 = "Aries"
                        elif int(self.fecha_nacii.month) == 4 and int(self.fecha_nacii.day) >= 21 or int(self.fecha_nacii.month) == 5 and int(self.fecha_nacii.day) <= 21:
                            self.signo_zodiacal_2 = "Tauro"
                        elif int(self.fecha_nacii.month) == 5 and int(self.fecha_nacii.day) >= 22 or int(self.fecha_nacii.month) == 6 and int(self.fecha_nacii.day) <= 22:
                            self.signo_zodiacal_2 = "Geminis"
                        elif int(self.fecha_nacii.month) == 6 and int(self.fecha_nacii.day) >= 23 or int(self.fecha_nacii.month) == 7 and int(self.fecha_nacii.day) <= 23:
                            self.signo_zodiacal_2 = "Cancer"
                        elif int(self.fecha_nacii.month) == 7 and int(self.fecha_nacii.day) >= 24 or int(self.fecha_nacii.month) == 8 and int(self.fecha_nacii.day) <= 23:
                            self.signo_zodiacal_2 = "Leo"
                        elif int(self.fecha_nacii.month) == 8 and int(self.fecha_nacii.day) >= 24 or int(self.fecha_nacii.month) == 9 and int(self.fecha_nacii.day) <= 23:
                            self.signo_zodiacal_2 = "Virgo"
                        elif int(self.fecha_nacii.month) == 9 and int(self.fecha_nacii.day) >= 24 or int(self.fecha_nacii.month) == 10 and int(self.fecha_nacii.day) <= 23:
                            self.signo_zodiacal_2 = "Libra"
                        elif int(self.fecha_nacii.month) == 10 and int(self.fecha_nacii.day) >= 24 or int(self.fecha_nacii.month) == 11 and int(self.fecha_nacii.day) <= 22:
                            self.signo_zodiacal_2 = "Escorpio"
                        elif int(self.fecha_nacii.month) == 11 and int(self.fecha_nacii.day) >= 23 or int(self.fecha_nacii.month) == 12 and int(self.fecha_nacii.day) <= 21:
                            self.signo_zodiacal_2 = "Sagitario"
                        elif int(self.fecha_nacii.month) == 12 and int(self.fecha_nacii.day) >= 22 or int(self.fecha_nacii.month) == 1 and int(self.fecha_nacii.day) <= 20:
                            self.signo_zodiacal_2 = "Capricornio"
                        elif int(self.fecha_nacii.month) == 1 and int(self.fecha_nacii.day) >= 21 or int(self.fecha_nacii.month) == 2 and int(self.fecha_nacii.day) <= 19:
                            self.signo_zodiacal_2 = "Acuario"
                        elif int(self.fecha_nacii.month) == 2 and int(self.fecha_nacii.day) >= 20 or int(self.fecha_nacii.month) == 3 and int(self.fecha_nacii.day) <= 20:
                            self.signo_zodiacal_2 = "Acuario"
                        self.personas.signo_zodiacal = self.signo_zodiacal_2
                        #Calculando el signo
                        
                        self.personas.save()

                        self.animeId_modify_insert.delete(0, END)
                        self.latitud_modify_insert.delete(0, END)
                        self.longitude_modify_insert.delete(0, END)
                        self.animeId_modify_character_space.delete(0, END)
                        self.date_modify_insert.delete(0, END)
                        self.modify_name_insert.delete(0, END)
                        self.last_name_insert_modify.delete(0, END)
                        self.Photo_modify_insert.delete(0, END)
                        self.pronunciation_modify_insert.delete(0, END)
                        self.power_modify_insert.delete(0, END)
                        self.quote_modify_insert.delete(0, END)
                        self.genre_modify_insert.delete(0, END)
                        self.high_modify_insert.delete(0, END)
                        self.sex_modify_insert.delete(0, END)
                        self.state_modify_insert.delete(0, END)
                        self.direction_modify_insert.delete(0, END)
                        self.description_modify_insert.delete(0, END)
                        
                        self.mylist_gm.delete(0, END)
                        for i in tablas.Personajes.select():
                            self.mylist_gm.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre + " Apellido: " + i.apellido + " Fecha de nacimiento" + i.fecha_nacimiento + " Latitud" + str(i.latitud) + " Longitud" + str(i.longitud))                                                       
                    
            
                    except:
                        messagebox.showwarning(message ="Solo puede ingresar fechas de nacimientos\ncon el siguiente formato DD/MM/AA", title="ERROR")
                        
                except:
                    messagebox.showwarning(message ="El anime o el personaje cuyo ID fue dijitado no existe", title="ERROR")
                
            except:
                messagebox.showwarning(message ="Digite numeros enteros en los campos ID anime, ID personajes'\nDigite numeros validos en los campos Latitud y Longitud", title="ERROR")
        else:
            messagebox.showwarning(message ="Todos los campos son requeridos", title="ERROR")
            
    def delete_characters_e(self):
        try:
            self.comparador = int(self.animeId_delete_space.get())
            try:
                self.personajes_e = tablas.Personajes.select().where(tablas.Personajes.id == self.comparador).get()
                messagebox.showinfo(message="Pesonaje Eliminado", title="INFORMATION")
                self.personajes_e.delete_instance()
                
                self.animeId_delete_space.focus()
                self.animeId_delete_space.delete(0, END)
                
                self.list_ge.delete(0, END)
                for i in tablas.Personajes.select():
                    self.list_ge.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre + " Apellido: " + i.apellido + " Fecha de nacimiento" + i.fecha_nacimiento + " Latitud" + str(i.latitud) + " Longitud" + str(i.longitud))                                                       
              
            except:
                messagebox.showwarning(message="El Id del anime que digito no existe", title="ERROR")
                
        except:
            messagebox.showwarning(message="Digite un numero entero porfavor ", title="ERROR") 
                     
#REPORTS  
    def list_of_characters(self):    
        self.list_r.delete(0, END)
        for i in tablas.Personajes.select():
            self.list_r.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre) 
             
    def list_of_characters_zodiac(self):    
        self.list_r.delete(0, END)
        for i in tablas.Personajes.select().order_by(tablas.Personajes.signo_zodiacal):
            self.list_r.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre + " Signo Zodiacal: " + i.signo_zodiacal) 
    
    def list_of_characters_anime(self):    
        self.list_r.delete(0, END)
        for i in tablas.Personajes.select().order_by(tablas.Personajes.serie_F_K):
            self.series = tablas.Anime.select().where(tablas.Anime.id == i.serie_F_K).get()
            self.list_r.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre + " Anime: " + self.series.nombre)

    def list_of_characters_state(self):    
        self.list_r.delete(0, END)
        for i in tablas.Personajes.select().order_by(tablas.Personajes.estado):
            self.list_r.insert(END, "Numero ID: "+ str(i.id) + " nombre: " +  i.nombre + " Estado del Personaje: " + i.estado)  
             
    def report_html_i(self): 
        try:
            self.comparador_html = int(self.animeId_insert_report.get())
            try:
                self.exportar_html = tablas.Personajes.select().where(tablas.Personajes.id == self.comparador_html).get()
                self.exportar_html_a = tablas.Anime.select().where(tablas.Anime.id == self.exportar_html.serie_F_K).get()
                
                self.html= f"""
                <!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <title></title>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1">
                            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                        </head>
                        <body>
                            <div>
                                <img src="{self.exportar_html.foto_url}" class="img-thumbnail">
                            </div>
                            <div>
                                <ul class="list-group">

                                    <li class="list-group-item" >Nombre: {self.exportar_html.nombre} </li>
                                    <li class="list-group-item">Apellido: {self.exportar_html.apellido} </li>
                                    <li class="list-group-item">Serie: {self.exportar_html_a.nombre} </li>
                                    <li class="list-group-item">Poder: {self.exportar_html.poder} </li>
                                    <li class="list-group-item">Frase: {self.exportar_html.frase_favorita} </li>
                                    <li class="list-group-item">Edad: {self.exportar_html.edad} </li>
                                    <li class="list-group-item">sexo: {self.exportar_html.sexo} </li>
                                    <li class="list-group-item">estado: {self.exportar_html.estado} </li>
                                    <li class="list-group-item">Signo Zodiacal: {self.exportar_html.signo_zodiacal} </li>
                                    <li class="list-group-item">Altura: {self.exportar_html.altura} </li>
                                </ul>
                            </div>
                        
                        </body>
                    </html>
                 
                 """
                archivo = open("personajes.html", "w")
                archivo.write(self.html)
                archivo.close()
                webbrowser.open("personajes.html")   
            except:
                 messagebox.showwarning(message="El ID que digito no existe en la base de datos", title="ERROR")
        except:
            messagebox.showwarning(message="Digite un numero entero porfavor", title="ERROR")
              
    #FUNSION PARA ENVIAR LOS PERSONAJES AL MAPA
    def map(self):
       
        map = folium.Map(location=[18.6127095,-68.755382], zoom_start = 10)
        
        for mot in tablas.Personajes.select():
            self.series_w = tablas.Anime.select().where(tablas.Anime.id == mot.serie_F_K).get()
            folium.Marker([mot.latitud, mot.longitud], popup = f"{mot.nombre} {mot.apellido} {mot.signo_zodiacal} {self.series_w.nombre}", tooltip = "Clip Para Ver Mas").add_to(map)

        map.save("map.html")
        webbrowser.open("map.html") 
    
if __name__ == "__main__":
    ventana = Tk()
    aplicacion = Examen(ventana)
    ventana.mainloop()
    
    