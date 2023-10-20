import pandas as pd
## adquisiscion de los datos #####
partido = pd.read_csv("https://raw.githubusercontent.com/cienciadedatos/datos-de-miercoles/master/datos/2019/2019-04-10/partidos.txt",delimiter='\t')
partido
partido_comparar=partido[(partido.
##### eleccióon  de los paises #########
alemania=partido_comparar[(partido_comparar.equipo_1=="Alemania")]
rusia =partido_comparar[(partido_comparar.equipo_1=="Rusia")]
#### media de goles de los paises #######
media1= alemania['equipo_1_final'].mean()
media1equipo_1=="Alemania")| (partido.equipo_1=="Rusia")]
partido_comparar
media2=rusia['equipo_1_final'].mean()
media2
tabla ={"paises":["Alemania","Rusia"],
        "media_goles": [1.91,3.33]}
tabla1= pd.DataFrame(tabla)
tabla1
######## grafico de barras de los gole por paises ##########
tabla1.plot(x = "paises", y = "media_goles", kind="bar")
plt.xlabel('Paises')
plt.ylabel('Media')
############ graficos de lineas de los goles por año de los paises ######
alemania.plot(x="anio", y="equipo_1_final")
plt.title("Alemania")
plt.show()
rusia.plot(x="anio", y="equipo_1_final")
plt.title("Rusia")
plt.show()
