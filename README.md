# Ejemplo de aplicación de grafos

## Ejercicio 1

Una empresa de cerveza artesanal cuenta con una red de distribución de sus productos en el país. La red está compuesta por 2 centros de distribución ubicados en las ciudades de Bogotá y Cali. 

Desde estos centros de distribución se abastecen a 15 ciudades del país: Medellín, Barranquilla, Cartagena, Cúcuta, Bucaramanga, Pereira, Santa Marta, Ibagué, Pasto, Manizales, Neiva, Villavicencio y Armenia, y por supuesto, Bogotá y Cali.

Se cuenta con una base de datos que contiene la información de las rutas entre las ciudades, la cual fue diseñada de en MySQL y puede ser consultada en mediante los archivos `beer_distribution_create_objects.sql` y `beer_distribution_load_data.sql`. A continuación se muestra el DER de la base de datos:

![beer_distribution_der](https://i.ibb.co/yQbGkkY/beer-distribution-der.png)

Adicionalmente, se emplearán las clases `City` y `Route` para representar las ciudades y las rutas entre las ciudades, respectivamente.

Emplando la base de datos y las clases mencionadas, se desea implementar un sistema que permita a la empresa determinar desde qué centros de distribución puede abastecer a cada una de las ciudades.

## Solución

Para resolver este problema, se modela la red de distribución como un grafo, donde los nodos representan las ciudades y las aristas representan las rutas entre las ciudades.

En este caso se representa el grafo mediante listas de adyacencia. Para construir el grafo, se emplea una estructura de datos vista previamente.

Para resolver el problema, se emplea el algoritmo de Dijkstra para encontrar el camino más corto entre cada ciudad y cada centro de distribución.

Para poder analizar la solución planteda, se ha definido el paquete `exercise_1` el cual contiene dos módulos: `analysis` y `solution`.

Al ejecutar el módulo `analysis`, se generan un archivo CSV por cada centro de distribución, el cual contiene la información de las distancias y recorridos hacia cada ciudad. Para esto se debe ejecutar el siguiente comando:

```bash
python -m exercise_1.analysis
```

Al ejecutar el módulo `solution`, se genera un archivo CSV tomando en cuenta la información de los dos centros de distribución. Para esto se debe ejecutar el siguiente comando:

```bash
python -m exercise_1.solution
```

Los archivos generados se encuentran en la carpeta `paths/exercise_1/`.

## Ejercicio 2

La empresa desea construir una nueva planta de producción.

Se desea determinar cuál de las ciudades es la más adecuada para construir la nueva planta de producción, de tal forma que se minimice la distancia total de los recorridos desde la nueva planta de producción hasta cada una de las ciudades.

## Solución

Para resolver este problema, se emplea nuevamente el algoritmo de Dijkstra para encontrar el camino más corto entre cada ciudad y la nueva planta de producción. Para lograr esto, se realiza un proceso similar al del ejercicio anterior, pero en este caso se analiza la información de los dos centros de distribución y la nueva planta de producción.

Este proceso puede ser considerado como una solución de fuerza bruta, ya que no se emplea ningún algoritmo de optimización tomando en cuenta la información obtenida en el ejercicio anterior. No obstante, el objetivo de este ejercicio es mostrar la posibilidad de emplear el algoritmo de Dijkstra para resolver problemas de optimización. Posteriormente, se puede modificar el script para emplear la información obtenida anteriormente y así mejorar la solución.

Para poder analizar la solución planteda, se ha definido el paquete `exercise_2` un módulo: `solution`.

Al ejecutar el módulo `solution`, se genera un archivo CSV por cada ciudad que no sea un centro de distribución. Además, se genera un archivo CSV que contiene la mejor solución. Para esto se debe ejecutar el siguiente comando:

```bash
python -m exercise_2.solution
```