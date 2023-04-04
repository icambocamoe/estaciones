#Gonzalez Rocha Jacobo Jehu - aporto E y F
#Moreno Garcia Fernando Israel - C y D
#Sotelo Palacios Miguel Angel - A y B

from fastapi import FastAPI
import psycopg2
import datetime as d
from starlette.middleware.cors import CORSMiddleware
import requests
import json
from bs4 import BeautifulSoup

app = FastAPI()
#

origins = "http://localhost:3000"


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

result = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

#A

@app.get('/getFilmByActor/{actor}')
async def read_item(actor_name: str, actor_last: str, token: str):
    try:
        """read token"""
        conn = psycopg2.connect(dbname="imecas", user="postgres", password="")
        cur = conn.cursor()

        actor_name = actor_name.title()
        actor_last = actor_last.title()

        cur.execute("select title, film.length, release_year, rating, category.name from film inner join (select film_id from film_actor where film_actor.actor_id = (select actor.actor_id from actor where first_name='" + actor_name + "' and last_name = '" + actor_last + "')) C on C.film_id = film.film_id	inner join film_category on film_category.film_id = film.film_id	inner join category on category.category_id = film_category.category_id")
        twple = cur.fetchall()
        i=0
        for i in range(len(twple)):
            dicty = {"fecha: ": twple[i][0], "hora: ": twple[i][1], "release year:": twple[i][2], "rating:" :twple[i][3], "categoria:" :twple[i][4]}
            result.append(dicty)
            i=i+1
        cur.close()
        conn.close()
        return {'actor': result}
    except(Exception, psycopg2.Error) as e:
            return {'message': 'error de conexion '+str(e)}
#B
@app.get('/getTotalCopies/')
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
            dicty = {"id":i,"address": twple[i][0], "title": twple[i][1], "copies": twple[i][2]}
            result.append(dicty)
            i=i+1

        cur.close()
        conn.close()
        return {'TotalCopies': result}
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion '+str(e)}
#C

@app.get('/getHistoryByClient/')
async def read_item(customer_id: int):
    try:
        conn = psycopg2.connect(dbname="dvdrental", user="postgres", password="")
        result.clear()
        cur = conn.cursor()
        query = "select title, T.address, T.rental_date, T.return_date, T.tiempo, T.amount, T.payment_date from film inner join (select film_id, inventory.store_id, address, C.rental_date,C.return_date,C.tiempo, C.amount, C.payment_date from inventory inner join (select inventory_id,rental_date,return_date, return_date -  rental_date as tiempo, amount, payment_date  from rental inner join payment on payment.rental_id = rental.rental_id where rental.customer_id = (select customer_id from customer where customer_id ="+str(customer_id)+") )C on C.inventory_id = inventory.inventory_id inner join address on inventory.store_id = address.address_id) T on T.film_id = film.film_id"


        cur.execute(query)

        twple = cur.fetchall()

        i = 1
        for i in range(len(twple)):
            dicty = {"title:": twple[i][0], "address:": twple[i][1], "rental_date:": twple[i][2], "return_date:": twple[i][3], "rental_days:": twple[i][4], "amount:": twple[i][5], "payment_date:": twple[i][6]}
            result.append(dicty)
            i = i + 1

        cur.close()
        conn.close()
        return {"message": result}

    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion '+str(e)}

#D

@app.get('/getTotalSubscriptors/')
async def method_name():
    try:
        conn = psycopg2.connect(dbname="dvdrental", user="postgres", password="")
        cur = conn.cursor()
        query = "select country, city, count(store.store_id) as suscriptores from public.country inner join city on city.country_id = country.country_id inner join address ON address.city_id = city.city_id inner join store ON store.address_id = address.address_id inner join (select customer.store_id from customer) C on C.store_id = store.store_id group by country, city"

        cur.execute(query)

        twple = cur.fetchall()

        i = 1
        for i in range(len(twple)):
            dicty = {"country:": twple[i][0], "city:": twple[i][1], "suscriptors:": twple[i][2]}
            result.append(dicty)
            i = i + 1

        cur.close()
        conn.close()
        return {"message": result}
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion '+str(e)}
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
        return {'message': 'error de conexion '+str(e)}




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
        return {'message': 'error de conexion'+str(e)}

@app.get('/getImecaMaxValues/{estacion}&{year}')
async def read_item(estacion: str, year: str):
    # listo
    try:
        conn = psycopg2.connect(dbname="imecas", user="postgres", password="")
        result.clear()
        cur = conn.cursor()
        cur.execute('SELECT "fecha",'+str(estacion)+' FROM fullprops  where extract(year from "fecha") = '+"'"+year+"'")
        twple = cur.fetchall()

        i=0
        for i in range(len(twple)):
            dicty = {"fecha": twple[i][0], "estacion": twple[i][1]}
            result.append(dicty)
            i=i+1

        cur.close()
        conn.close()
        return {'MaxValues': result}
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion '+str(e)}

@app.get('/getRegressionValues/{estacion}&{month}&{day}')
async def read_item(estacion: str, month: int, day: int,):
    # listo
    try:
        conn = psycopg2.connect(dbname="imecas", user="postgres", password="")
        result.clear()
        cur = conn.cursor()
        cur.execute('select ROW_NUMBER () OVER (ORDER BY "fecha"),'+str(estacion)+',"fecha" from "fullprops" where extract(month from "fecha") = '+str(month)+' and extract(day from "fecha") = '+str(day))
        twple = cur.fetchall()

        i=0
        for i in range(len(twple)):
            dicty = {"row": twple[i][0],"estacion": twple[i][1],"fecha": twple[i][2]}
            result.append(dicty)
            i=i+1

        cur.close()
        conn.close()
        return {'RegressionValues': result}
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion '+str(e)}

@app.get('/getEscritura/{escritura}')
async def read_item(escritura: str):
    # listo
    try:

        url = "http://NOT238.dyndns.org:2080/cgi-bin/exp_grales_www.exe?EXPE="+escritura+"&TIPO_USO=Consulta"
        r = requests.get(url)

        byteData = r.content
        str1 = byteData.decode('ansi')
        soup = BeautifulSoup(str1, "html.parser")
        dict = []
        # Find all table elements
        tables = soup.find_all('table')

        # Loop through the tables and print their contents
        for table in tables:

            # Get the table rows
            rows = []
            for tr in table.find_all('tr'):

                row = []
                for td in tr.find_all('td'):
                    row.append(td.text.strip())
                if row:
                    rows.append(row)

            # Print the table headers and rows
            transposed_list = list(map(list, zip(*rows)))
            flag = 0

            for row in transposed_list:
                result = [s for s in row if ":" in s]
                result2 = [s for s in row if ":" not in s]
                if flag:
                    dict.append(result2)
                for data in result:
                    splitted = data.split(":")
                    dict.append(splitted)
                flag = 1

        del dict[0]
        del dict[0]
        my_dict = {key: value for key, value in dict}
        return {'EscrituraValues': my_dict}
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion '+str(str1)}


@app.post("/login")
async def read_item(user: str, passwd: str):
    # listo
    try:
        urlogin = "http://notdf77.dyndns.org:2080/cgi-bin/CONRTG_WWW.EXE"
        User = {
            "usuario": user,
            "claveac": passwd
        }
        login = requests.post(urlogin, data=User)
        byteLoginData = login.content
        lstr = byteLoginData.decode('ansi')
        return {lstr}
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion '+str(lstr)}