from mysql.connector import connect

mydb = connect(
    host='localhost',
    user='SamuSada',
    password='2505',
    database='cinemania'
)

consulta = mydb.cursor()

consulta.execute('SELECT nombre, COUNT(pa.id_pelicula)  FROM actores_actrices aa  JOIN peliculas_actores pa ON aa.id_actor = pa.id_actor GROUP BY aa.id_actor ORDER BY COUNT(pa.id_pelicula) DESC ')

for i in consulta:
    print(f"{i[0]} - {i[1]} películas")
