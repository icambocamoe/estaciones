#gonzalez rocha jacobo jehu
#moreno garcia fernando israel
#sotelo palacios miguel angel

from fastapi import FastAPI
import psycopg2

app = FastAPI()


result = []

@app.get("/")
async def root():
    return {"message": "Hello World"}
#B
@app.get('/getTotalCopies/')  #####LISTO######
async def method_name():
    # listo
    try:
        conn = psycopg2.connect(dbname="dvdrental", user="postgres", password="")
        result.clear()
        cur = conn.cursor()
        cur.execute('SELECT a.address, f.title, count(i.film_id) AS count FROM address a JOIN store s ON a.address_id = s.address_id JOIN inventory i ON s.store_id = i.store_id JOIN film f ON i.film_id = f.film_id WHERE a.address_id = 1 OR a.address_id = 2 GROUP BY a.address, f.title ORDER BY f.title;')
        twple = cur.fetchall()

        i=0
        for i in range(len(twple)):
            dicty = {"address": twple[i][0], "title": twple[i][1], "copies": twple[i][2]}
            result.append(dicty)
            i=i+1

        cur.close()
        conn.close()
        return {'TotalCopies': result}
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion'}

#E
@app.get("/addActor/")
async def read_item(first_name: str, last_name: str):
    try:
        conn = psycopg2.connect(dbname="dvdrental", user="postgres", password="")
        cur = conn.cursor()
        query = "INSERT INTO public.actor (first_name, last_name) VALUES ('" + str(first_name) + "', '" + str(last_name) +"');"

        cur.execute(query)
        conn.commit()

        cur.close()
        conn.close()
        return {"message": query}
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion'}




#F
@app.get("/deleteOneTransactionBySubscriptor/{payment_id}")
async def read_item(payment_id: int):

    try:
        conn = psycopg2.connect(dbname="dvdrental", user="postgres", password="")
        cur = conn.cursor()
        query = 'DELETE FROM public.payment WHERE rental_id=(SELECT rental_id FROM public.payment WHERE payment.payment_id='+str(payment_id)+');'
        cur.execute(query)
        conn.commit()
        query = 'DELETE FROM public.payment WHERE payment_id='+str(payment_id)+';'
        cur.execute(query)
        conn.commit()
        return {"message": "eliminado" }
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion'}

