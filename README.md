## Qué es esto

Es una MVP Demo para lectura y escritura de geojsons en MS SQL Server usando la librería Leaflet con la extensión Geoman.

Utiliza Python 3 y Flask como framework.

## Para qué

Para poder levantar rapidamente un webgis simple de carga y edición de geometrías que hable con MS SQL Server.


## virtualenv

```
python -m venv venv
source venv/scripts/activate
```
:white_check_mark: check (venv) on cli 


## pip install requirements.txt

```
pip install -r requirements.txt

```

:white_check_mark: check installed dependencies (Flask, PyODBC, Dotenv)

- fill .env.dummy with DB conn and copy it to .env

## SQL DDL

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


## ejecución

```
python app.py
```

- enjoy!

## To-Do's

:black_square_button: update geom based on ID

:black_square_button: remove hardcoded ID from test
