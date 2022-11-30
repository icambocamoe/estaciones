#Gonzalez Rocha Jacobo Jehu
#Moreno Garcia Fernando Israel
#Sotelo Palacios Miguel Angel 

from fastapi import FastAPI
import psycopg2
import datetime as d

app = FastAPI()


result = []

@app.get("/getDataByDate/{date}")
async def read_item(date: str, col: str):
    try:
        conn = psycopg2.connect(dbname="imecas", user="postgres", password="")
        cur = conn.cursor()
        result.clear()
        s=date[2:4]
        col = col.upper()
        query = "SELECT "+'"FECHA",'+'"HORA",'+ '"'+col +'"'+ "FROM public."+'"CO-'+s+'"'+" WHERE "+'"FECHA"'+" = '"+date+"'"
        cur.execute(query)

        twple = cur.fetchall()
        i=0
        for i in range(len(twple)):
            dicty = {"date: ": twple[i][0], "hour: ": twple[i][1], col: twple[i][2]}
            result.append(dicty)
            i=i+1

        cur.close()
        conn.close()
        return {"message": result}
    except(Exception, psycopg2.Error) as e:
            return {'message': 'error de conexion '+str(e)+query}

@app.get("/getDataByState/{state}")
async def read_item(state: str, tipo_v: str):
    try:
        conn = psycopg2.connect(dbname="vehiculos", user="postgres", password="")
        cur = conn.cursor()
        result.clear()
        state = state.title()
        t = tipo_v[0:1]
        t = t.upper()
        query = "SELECT "+'"ESTADO","'+t+'_SUMA","'+t+'_OFICIAL","'+t+ '_PUBLICO","'+t+'_PARTICULAR"'+" FROM public.vehiculos where "+'"ESTADO" = ' "'"+state+"'"
        cur.execute(query)

        twple = cur.fetchall()
        i=0
        for i in range(len(twple)):
            dicty = {"ESTADO: ": twple[i][0], t+"_SUMA": twple[i][1], t+"_OFICIAL": twple[i][2], t+"_PUBLICO": twple[i][3], t+"_PARTICULAR": twple[i][4]}
            result.append(dicty)
            i=i+1

        cur.close()
        conn.close()
        return {"message": result}
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion ' + str(e) + query}

@app.get("/getDataByYear/{year}")
async def read_item(year: int, zona: str):
    try:
        conn = psycopg2.connect(dbname="accidentes", user="postgres", password="")
        cur = conn.cursor()
        result.clear()

        query = "select "+'"Tipo","'+str(year)+'" from "'+zona+'"'

        cur.execute(query)

        twple = cur.fetchall()

        i = 0
        for i in range(len(twple)):
            dicty = {"Tipo: ": twple[i][0], "Cantidad": twple[i][1]}
            result.append(dicty)
            i = i + 1

        cur.close()
        conn.close()
        return {"message": result}
    except(Exception, psycopg2.Error) as e:
        return {'message': 'error de conexion ' + str(e) + query}