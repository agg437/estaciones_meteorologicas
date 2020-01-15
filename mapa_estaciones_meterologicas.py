import pandas as pd

estac_meteo = pd.read_csv('precip.stn', delimiter=',',index_col='station_id')  #localización de las estaciones meteorológicas
estac_meteo.head()

import pandas as pd

estac_meteo = pd.read_csv('precip.stn', delimiter=',',index_col='station_id')  #localización de las estaciones meteorológicas
estac_meteo.head()

fig, ax = plt.subplots()

#Distribución espacial de las estaciones
ax.scatter(estac_meteo.iloc[:, 1], estac_meteo.iloc[:, 2], c= 'purple',label='Stations emplacement')

#Valor promedio
lon_promedio = estac_meteo.iloc[:,1].mean()
lat_promedio = estac_meteo.iloc[:,2].mean()

ax.scatter(lon_promedio,lat_promedio, c = 'green', label = 'Average')
#Valor máximo
lon_max = estac_meteo.iloc[:,1].max()
lat_max = estac_meteo.iloc[:,2].max()

ax.scatter(lon_max, lat_max, c = 'red', label = 'Maximum')

#Ajustes del gráfico: ejes, leyenda, tamaño, disposición de las etiquetas

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(loc="upper left")
fig.set_size_inches(20,30)    
for label, x, y in zip(estac_meteo.iloc[:,0],estac_meteo.iloc[:, 1], estac_meteo.iloc[:, 2]):
    plt.annotate(
        label,
        xy = (x, y), xytext = (0, 10), #espacio entre la etiqueta y el punto
        textcoords = 'offset points', ha = 'center', va = 'bottom') #textcoords = 'offset points', puntos centrados y compensados
                                                                    #ha = 'center',etiqueta centrada
                                                                    #va = 'bottom', punto debajo de la etiqueta

fig.savefig("estaciones.png")