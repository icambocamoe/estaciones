import petl as etl
import psycopg2
import sqlalchemy
import pyexcel as p
import datetime as d
import decimal as c
def func(val, row):
    s = str(row.FECHA)

    return s[0:11]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    try:
        xlx =  etl.io.xls.fromxls("C:/Users/jehu/Downloads/22RAMA/2022CO.xls")
        print(xlx)
        print("hola")
        aire = etl.io.xlsx.fromxlsx("C:/Users/jehu/Downloads/IMECAS/2015CO.xlsx", max_col=38, read_only=True)

        # fecha = etl.convert(aire,'ACO','AJM','ATI','BJU','CAM','CCA','CHO','CUA','FAC','HGM','INN','IZT','LLA','LPR','MER','MGH','MON','NEZ','PED','SAG','SFE','SJA','TAH','TLA','TLI','UAX','UIZ','VIF','XAL', float)

       # aire = etl.convert(aire,'FECHA', func, pass_row=True)
        aire = etl.convert(aire, 'FECHA', d.datetime.date)
        aire = etl.convert(aire, 'HORA', d.time)
        aire = etl.cut(aire, 'FECHA', 'HORA', 'ACO', 'AJM', 'ATI', 'CAM', 'CCA', 'CHO', 'CUA', 'FAC', 'HGM',
                        'INN', 'IZT', 'LLA', 'LPR', 'MER', 'MGH', 'MON', 'NEZ', 'PED', 'SAG', 'SFE', 'SJA', 'TAH',
                        'TLA', 'TLI', 'UAX', 'UIZ', 'VIF', 'XAL')
        #etl.tocsv(aire, "C:/Users/jehu/Downloads/O3/2015O3.csv")

        i=16
        while i != 22:
            fecha = etl.io.xlsx.fromxlsx("C:/Users/jehu/Downloads/IMECAS/20"+str(i)+"CO.xlsx", max_col=38,read_only=True)

            #fecha = etl.convert(aire,'ACO','AJM','ATI','BJU','CAM','CCA','CHO','CUA','FAC','HGM','INN','IZT','LLA','LPR','MER','MGH','MON','NEZ','PED','SAG','SFE','SJA','TAH','TLA','TLI','UAX','UIZ','VIF','XAL', float)

            #fecha = etl.convert(fecha,'FECHA', func, pass_row=True)
            fecha = etl.cut(fecha,'FECHA','HORA','ACO','AJM','ATI','CAM','CCA','CHO','CUA','FAC','HGM','INN','IZT','LLA','LPR','MER','MGH','MON','NEZ','PED','SAG','SFE','SJA','TAH','TLA','TLI','UAX','UIZ','VIF','XAL')
            fecha = etl.convert(fecha, 'FECHA', d.datetime.date)
            fecha = etl.convert(fecha, 'HORA', d.time)
            aire = etl.mergesort(aire,fecha, key='FECHA')


            #etl.tocsv(fecha, "C:/Users/jehu/Downloads/CO/20"+str(i)+"CO.csv")
            print(aire)
            i += 1

    except Exception as e:
        print('couldn open file ' + str(e))
    etl.tocsv(aire, "C:/Users/jehu/Downloads/CO/20" + str(i) + "TO.csv")
