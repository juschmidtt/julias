import psycopg

conn = psycopg.connect("dbname=julias user=postgres password=3f@db host=164.90.152.205 port=80")

cur = conn.cursor() 
# teste 