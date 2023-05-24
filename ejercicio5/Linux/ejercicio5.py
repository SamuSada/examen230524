import tkinter as tk
import requests
from bs4 import BeautifulSoup

municipio = "A Coruña"


def id_ames():
    temp_min("ames-bertamirans-id15002")
    temp_max("ames-bertamirans-id15002")
    label2.config(text="Temperaturas - Ames")


def id_arteixo():
    temp_min("arteixo-baiuca-a-id15005")
    temp_max("arteixo-baiuca-a-id15005")
    label2.config(text="Temperaturas - Arteixo")


def id_betanzos():
    temp_min("betanzos-id15009")
    temp_max("betanzos-id15009")
    label2.config(text="Temperaturas - Betanzos")


def id_boiro():
    temp_min("boiro-boiro-de-arriba-id15011")
    temp_max("boiro-boiro-de-arriba-id15011")
    label2.config(text="Temperaturas - Boiro")


def id_cambre():
    temp_min("cambre-id15017")
    temp_max("cambre-id15017")
    label2.config(text="Temperaturas - Cambre")


def id_carballo():
    temp_min("carballo-id15019")
    temp_max("carballo-id15019")
    label2.config(text="Temperaturas - Carballo")


def id_acoruna():
    temp_min("coruna-a-id15030")
    temp_max("coruna-a-id15030")
    label2.config(text="Temperaturas - A Coruña")


def id_culleredo():
    temp_min("culleredo-tarrio-id15031")
    temp_max("culleredo-tarrio-id15031")
    label2.config(text="Temperaturas - Culleredo")


def id_fene():
    temp_min("fene-id15035")
    temp_max("fene-id15035")
    label2.config(text="Temperaturas - Fene")


def id_ferrol():
    temp_min("ferrol-id15036")
    temp_max("ferrol-id15036")
    label2.config(text="Temperaturas - Ferrol")


def id_laracha():
    temp_min("laracha-a-id15041")
    temp_max("laracha-a-id15041")
    label2.config(text="Temperaturas - Laracha")


def id_naron():
    temp_min("naron-id15054")
    temp_max("naron-id15054")
    label2.config(text="Temperaturas - Narón")


def id_noia():
    temp_min("noia-id15057")
    temp_max("noia-id15057")
    label2.config(text="Temperaturas - Noia")


def id_oleiros():
    temp_min("oleiros-real-o-id15058")
    temp_max("oleiros-real-o-id15058")
    label2.config(text="Temperaturas - Oleiros")


def id_ordes():
    temp_min("ordes-id15059")
    temp_max("ordes-id15059")
    label2.config(text="Temperaturas - Ordes")


def id_rianxo():
    temp_min("rianxo-id15072")
    temp_max("rianxo-id15072")
    label2.config(text="Temperaturas - Rianxo")


def id_ribeira():
    temp_min("ribeira-santa-uxia-de-ribeira-id15073")
    temp_max("ribeira-santa-uxia-de-ribeira-id15073")
    label2.config(text="Temperaturas - Ribeira")


def id_sada():
    temp_min("sada-id15075")
    temp_max("sada-id15075")
    label2.config(text="Temperaturas - Sada")


def id_santiago():
    temp_min("santiago-de-compostela-id15078")
    temp_max("santiago-de-compostela-id15078")
    label2.config(text="Temperaturas - Santiago")


def id_teo():
    temp_min("teo-ramallosa-a-id15082")
    temp_max("teo-ramallosa-a-id15082")
    label2.config(text="Temperaturas - Teo")


def temp_min(id_municipio):
    entry1.delete(0, tk.END)
    url = f"https://www.aemet.es/es/eltiempo/prediccion/municipios/{id_municipio}.html"
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    temp_min_str = str(sopa.find('span', class_='texto_azul'))
    lista = []
    for u in temp_min_str:
        if u.isdigit():
            lista.append(int(u))
    temp_minima = int(f"{lista[0]}{lista[1]}")
    entry1.insert(0, temp_minima)


def temp_max(id_municipio):
    entry0.delete(0, tk.END)
    url = f"https://www.aemet.es/es/eltiempo/prediccion/municipios/{id_municipio}.html"
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    temp_min_str = str(sopa.find('span', class_='texto_rojo'))
    lista = []
    for u in temp_min_str:
        if u.isdigit():
            lista.append(int(u))
    temp_maxima = int(f"{lista[0]}{lista[1]}")
    entry0.insert(0, temp_maxima)


fuente = ("Courier 10 Pitch", 20, "normal")

root = tk.Tk()
root.title("Temperaturas - A Coruña")
root.geometry("1100x700+200+200")

# Canva titulo
label2 = tk.Label(root, text=f"Temperaturas - A Coruña", font=fuente)
label2.pack(pady=20)

# Canva0
canva0 = tk.Canvas(root, highlightthickness=0)
canva0.pack(pady=20)

# Canva0 -- ENTRY 0
label0 = tk.Label(canva0, text="Máximas", font=fuente)
label0.grid(row=0, column=0, padx=20)
entry0 = tk.Entry(canva0, width=2)
entry0.config(font=fuente)
entry0.grid(row=0, column=1, padx=20, pady=10)

# Canva0 -- ENTRY 1
label0 = tk.Label(canva0, text="Mínimas", font=fuente)
label0.grid(row=1, column=0, padx=20)
entry1 = tk.Entry(canva0, width=2)
entry1.config(font=fuente)
entry1.grid(row=1, column=1, padx=20, pady=10)

# Canva1
canva1 = tk.Canvas(root, highlightthickness=0)
canva1.pack(pady=20)

# Botones
boton1 = tk.Button(canva1, text="Ames", width=20, height=2, command=id_ames)
boton1.grid(row=0, column=0, padx=20, pady=10)

boton2 = tk.Button(canva1, text="Arteixo", width=20, height=2, command=id_arteixo)
boton2.grid(row=0, column=1, padx=20, pady=10)

boton3 = tk.Button(canva1, text="Betanzos", width=20, height=2, command=id_betanzos)
boton3.grid(row=0, column=2, padx=20, pady=10)

boton4 = tk.Button(canva1, text="Boiro", width=20, height=2, command=id_boiro)
boton4.grid(row=0, column=3, padx=20, pady=10)

boton5 = tk.Button(canva1, text="Cambre", width=20, height=2, command=id_cambre)
boton5.grid(row=1, column=0, padx=20, pady=10)

boton6 = tk.Button(canva1, text="Carballo", width=20, height=2, command=id_carballo)
boton6.grid(row=1, column=1, padx=20, pady=10)

boton7 = tk.Button(canva1, text="A Coruña", width=20, height=2, command=id_acoruna)
boton7.grid(row=1, column=2, padx=20, pady=10)

boton8 = tk.Button(canva1, text="Culleredo", width=20, height=2, command=id_culleredo)
boton8.grid(row=1, column=3, padx=20, pady=10)

boton9 = tk.Button(canva1, text="Fene", width=20, height=2, command=id_fene)
boton9.grid(row=2, column=0, padx=20, pady=10)

boton10 = tk.Button(canva1, text="Ferrol", width=20, height=2, command=id_ferrol)
boton10.grid(row=2, column=1, padx=20, pady=10)

boton11 = tk.Button(canva1, text="Laracha", width=20, height=2, command=id_laracha)
boton11.grid(row=2, column=2, padx=20, pady=10)

boton12 = tk.Button(canva1, text="Narón", width=20, height=2, command=id_naron)
boton12.grid(row=2, column=3, padx=20, pady=10)

boton13 = tk.Button(canva1, text="Noia", width=20, height=2, command=id_noia)
boton13.grid(row=3, column=0, padx=20, pady=10)

boton14 = tk.Button(canva1, text="Oleiros", width=20, height=2, command=id_oleiros)
boton14.grid(row=3, column=1, padx=20, pady=10)

boton15 = tk.Button(canva1, text="Ordes", width=20, height=2, command=id_ordes)
boton15.grid(row=3, column=2, padx=20, pady=10)

boton16 = tk.Button(canva1, text="Rianxo", width=20, height=2, command=id_rianxo)
boton16.grid(row=3, column=3, padx=20, pady=10)

boton17 = tk.Button(canva1, text="Ribeira", width=20, height=2, command=id_ribeira)
boton17.grid(row=4, column=0, padx=20, pady=10)

boton18 = tk.Button(canva1, text="Sada", width=20, height=2, command=id_sada)
boton18.grid(row=4, column=1, padx=20, pady=10)

boton19 = tk.Button(canva1, text="Santiago de Compostela", width=20, height=2, command=id_santiago)
boton19.grid(row=4, column=2, padx=20, pady=10)

boton20 = tk.Button(canva1, text="Teo", width=20, height=2, command=id_teo)
boton20.grid(row=4, column=3, padx=20, pady=10)

root.mainloop()
