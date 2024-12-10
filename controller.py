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

def editarImpacto(impact_id, plan_id=None, impact_area=None, expected_outcome=None, actual_outcome=None, impact_score=None):
    try:
        conn = sql.connect("autoconocimientoJesusAldayrRamirezErazo.db")
        cursor = conn.cursor()

        # Crear una lista de campos y valores a actualizar
        campos_a_actualizar = []
        valores = []

        if plan_id is not None:
            campos_a_actualizar.append("plan_id = ?")
            valores.append(plan_id)
        if impact_area is not None:
            campos_a_actualizar.append("impact_area = ?")
            valores.append(impact_area)
        if expected_outcome is not None:
            campos_a_actualizar.append("expected_outcome = ?")
            valores.append(expected_outcome)
        if actual_outcome is not None:
            campos_a_actualizar.append("actual_outcome = ?")
            valores.append(actual_outcome)
        if impact_score is not None:
            campos_a_actualizar.append("impact_score = ?")
            valores.append(impact_score)

        # Si no hay cambios, salimos
        if not campos_a_actualizar:
            print("No se proporcionaron campos para actualizar.")
            return

        # Agregar el identificador al final de los valores
        valores.append(impact_id)

        # Crear el comando SQL dinámicamente
        comando_sql = f"""
        UPDATE strategic_impact
        SET {', '.join(campos_a_actualizar)}
        WHERE impact_id = ?
        """

        # Ejecutar la consulta
        cursor.execute(comando_sql, valores)
        conn.commit()

        if cursor.rowcount > 0:
            print("Registro actualizado correctamente")
        else:
            print("No se encontró un registro con el impact_id proporcionado.")

    except sql.Error as e:
        print(f"Error al actualizar la tabla: {e}")
    finally:
        conn.close()

def eliminarImpacto(impact_id):
    try:
        conn = sql.connect("autoconocimientoJesusAldayrRamirezErazo.db")
        cursor = conn.cursor()

        # Crear y ejecutar el comando SQL para eliminar
        comando_sql = "DELETE FROM strategic_impact WHERE impact_id = ?"
        cursor.execute(comando_sql, (impact_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print("Registro eliminado correctamente")
        else:
            print("No se encontró un registro con el impact_id proporcionado.")

    except sql.Error as e:
        print(f"Error al eliminar en la tabla: {e}")
    finally:
        conn.close()

def consultarTablaCompleta():
    try:
        conn = sql.connect("autoconocimientoJesusAldayrRamirezErazo.db")
        cursor = conn.cursor()

        # Consultar todos los registros de la tabla
        cursor.execute("SELECT * FROM strategic_impact")
        registros = cursor.fetchall()

        if registros:
            for registro in registros:
                print(registro)
        else:
            print("No hay registros en la tabla.")

    except sql.Error as e:
        print(f"Error al consultar la tabla: {e}")
    finally:
        conn.close()



if __name__=="__main__":
    #createDb()
    #createTeable()
    #insertarNuevoImpacto(1,1,"asd","asd","asd",1)
    #insertarNuevoImpacto(2,1,"nuevo","impacto","estrategico",1)
    #editarImpacto(2,1,"nuevo","impacto","estrategico",5)
    #eliminarImpacto(2)
    consultarTablaCompleta()