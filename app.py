from flask import Flask, request
import uuid
import psycopg

app = Flask(__name__)
connection_db = psycopg.connect("dbname=julias user=postgres password=3f@db host=164.90.152.205 port=80")