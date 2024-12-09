import time
import sqlite3 as sql

def createDb():
    conn = sql.connect("autoconocimientoJesusAldayrRamirezErazo.db")
    print("Base de datos de autoconocimiento creada")
    conn.commit()
    conn.close();

def createTeable():
    conn=sql.connect("autoconocimientoJesusAldayrRamirezErazo.db")
    cursor= conn.cursor()

    cursor.execute("""
    CREATE TABLE strategic_impact (
    impact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER,
    impact_area TEXT,
    expected_outcome TEXT,
    actual_outcome TEXT,
    impact_score INTEGER CHECK (impact_score BETWEEN 1 AND 10)py
    );
    """)
    conn.commit()
    print("Tabla creada")
    conn.close()

def insertarNuevoImpacto(impact_id,plan_id, impact_area, expected_outcome, actual_outcome, impact_score):
    try:
        conn = sql.connect("autoconocimientoJesusAldayrRamirezErazo.db")
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO strategic_impact (impact_id,plan_id, impact_area, expected_outcome, actual_outcome, impact_score)
        VALUES (?, ?, ?, ?, ?, ?);
        """, (impact_id, plan_id, impact_area, expected_outcome, actual_outcome, impact_score))
        conn.commit()
        print("Registro insertado correctamente")
    except sql.Error as e:
        print(f"Error al insertar en la tabla: {e}")
    finally:
        conn.close()

def searchStrategicImpact(impact_id=None):
    
    try:
        conn = sql.connect("autoconocimientoJesusAldayrRamirezErazo.db")
        cursor = conn.cursor()

        # Construir la consulta base
        query = "SELECT * FROM strategic_impact WHERE 1=1"
        params = []

        # Agregar filtros opcionales
        if impact_id is not None:
            query += " AND impact_id = ?"
            params.append(impact_id)
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Mostrar resultados
        if results:
            print("Resultados encontrados:")
            for row in results:
                print(f"ID: {row[0]}, Plan ID: {row[1]}, Área: {row[2]}, Esperado: {row[3]}, Real: {row[4]}, Puntuación: {row[5]}")
        else:
            print("No se encontraron registros.")

    except sql.Error as e:
        print(f"Error al buscar en la tabla: {e}")
    finally:
        conn.close()

if __name__=="__main__":
    #createDb()
    #createTeable()
    #insertarNuevoImpacto(1,1,"asd","asd","asd",1)
    insertarNuevoImpacto(2,1,"nuevo","impacto","estrategico",1)
    