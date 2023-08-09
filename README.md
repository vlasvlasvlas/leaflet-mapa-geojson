
![image](https://github.com/vlasvlasvlas/leaflet-mapa-geojson/assets/4071796/5e34dc0e-1c98-4242-a770-9c9fd291ccbc)

# Qué es esto

Esto es un MVP Demo para lectura, edición y escritura de geometrías geojsons en MS SQL Server, usando la librería Leaflet con la extensión Geoman.

Utiliza Python 3 y Flask como framework.

# Para qué

Para poder levantar rapidamente un webgis embebido que sea sencillo para  la carga y edición de geometrías que almacene los datos en MS SQL Server.

# Instalación

## 1. virtualenv

Es necesario crear un virtual enviroment con venv.

```
python -m venv venv
source venv/scripts/activate
```

:white_check_mark: revisar que aparezca (venv) en la CLI.


## 2. Dependencias y librerías

Es necesario instalar las dependencias 

```
pip install -r requirements.txt

```

:white_check_mark: check installed dependencies (Flask, PyODBC, Dotenv)

- fill .env.dummy with DB conn and copy it to .env

## 3. SQL DDL

Es necesario tener una tabla para alojar las geometrías.

```
--create table
CREATE TABLE DB.dbo.test_geojson (
	id INT IDENTITY NOT NULL,
	geojson varchar(MAX) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);

--insert dummy
INSERT INTO DB.dbo.test_geojson
( geojson)
VALUES('{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-58.381691,-34.550478]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-58.326588,-34.545388]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-58.328304,-34.567866]}}]}');
```


## 4. Ejecución

Es necesario ejecutar la aplicación de Python utlizando la CLI.

```

python app.py

```

- Ingresar a través de un browser utilizando //localhost:5000

## To-Do's

:black_square_button: Sumar un ID de objeto al cual se le asocia la geometrías (id_objeto, id_geom, geojson).

:black_square_button: Sumar método "update" para las geometrías basadas en un id específico.

:black_square_button: dejar de forma dinámica el ID de la geometría.
