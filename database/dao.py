from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_nodes(n_alb):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select a.id
                   from artist a, album a2
                   where a.id = a2.artist_id
                   group by a.id
                   having count(*) >= %s"""
        cursor.execute(query, (n_alb,))
        for row in cursor:
            result.append(row)
        conn.close()
        return result

    @staticmethod
    def get_connessioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select a1.id as artista1, a2.id as artista2,  count(*) as peso
from (select a.id as album, a.artist_id as artista1, t.genre_id as genere
from album a, track t
where a.id = t.album_id) t1,
(select a.id as album, a.artist_id as artista2, t.genre_id as genere
from album a, track t
where a.id = t.album_id) t2, artist a1, artist a2
where t1.album < t2.album and t1.genere = t2.genere and a1.id = t1.artista1 and a2.id = t2.artista2 and a1.id != a2.id
group by a1.id, a2.id"""
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

