import os
import pyodbc
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

load_dotenv()

app = Flask(__name__)

# Configuración de la conexión a SQL Server
db_config = {
    "server": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PWRD"),
    "port": os.getenv("DB_PORT"),
}


def get_connection():
    connection_string = f"DRIVER={{SQL Server}};SERVER={db_config['server']};PORT={db_config['port']};DATABASE={db_config['database']};UID={db_config['username']};PWD={db_config['password']}"
    return pyodbc.connect(connection_string)


print(">> test conn start")
connection = get_connection()
cursor = connection.cursor()
sql_query = "SELECT * FROM dbo.test_geojson"
cursor.execute(sql_query)

# debug start
columns = [column[0] for column in cursor.description]
results = []
for row in cursor.fetchall():
    results.append(dict(zip(columns, row)))
print(results)
# debug end

connection.commit()
connection.close()
print(">> test conn end")


# index
@app.route("/")
def index():
    return render_template("index.html")


# guardar el geojson
@app.route("/guardar_geojson", methods=["POST"])
def guardar_geojson():
    try:
        feature_collection = request.json["featureCollection"]

        connection = get_connection()
        cursor = connection.cursor()

        # se podria modificar el insert por update donde el id sea el geojsonid que se usa en /cargar_objetos
        sql_query = "INSERT INTO dbo.test_geojson (geojson) VALUES (?)"
        cursor.execute(sql_query, feature_collection)
        connection.commit()
        connection.close()

        return jsonify({"message": "GeoJSON guardado correctamente"})
    except Exception as err:
        return jsonify({"error": str(err)})


# cargar el geojson
@app.route("/cargar_geojson", methods=["POST"])
def cargar_geojson():
    try:
        print("--select start --")
        feature_collectionid = request.json["idgeom"]
        connection = get_connection()
        cursor = connection.cursor()

        sql_query = """
        
        SELECT '{"type": "FeatureCollection", "features": [' +
        STRING_AGG(JSON_QUERY(geojson, '$.features'), ',') +
        ']}'
        FROM dbo.test_geojson;
        
        """
        #"SELECT geojson,id FROM dbo.test_geojson WHERE id < (?)"
        # completar el where con los filtros que se necesiten desde el front
        
        cursor.execute(sql_query, feature_collectionid)
        print("sql_query:",sql_query)
        print("feature_collectionid:",feature_collectionid)

        # debug start
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            print("row in cursor ------- start")
            print(dict(zip(columns, row)))
            results.append(dict(zip(columns, row)))
            print("row in cursor ------- end")
        #print(results[0]["geojson"])
        #print(results)
        # debug end

        connection.commit()
        connection.close()
        print("--select end --")

        return jsonify(
            {
                "message": "GeoJSON guardado correctamente",
                "geojson": results[0]["geojson"],
            }
        )

    except Exception as err:
        return jsonify({"error": str(err)})


if __name__ == "__main__":
    app.run(debug=True)
