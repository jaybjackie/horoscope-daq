import sys
from flask import abort
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import models

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)

def get_current_aqi():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
        SELECT c.value 
        FROM TermProjectCurrent c
        WHERE source="aqi"
        """)
        result = cs.fetchone()
    if result and result[0]:
        return result[0]
    abort(404)

def get_current_temp():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
        SELECT c.value 
        FROM TermProjectCurrent c
        WHERE source="temperature"
        """)
        result = cs.fetchone()
    if result and result[0]:
        return result[0]
    abort(404)

def get_current_precipitation_probability():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
        SELECT c.value 
        FROM TermProjectCurrent c
        WHERE source="precipitaion"
        """)
        result = cs.fetchall()
    if result and result[0]:
        return result[0]
    abort(404)

def get_current_uv_index():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
        SELECT c.value 
        FROM TermProjectCurrent c
        WHERE source="UV"
        """)
        result = cs.fetchone()
    if result and result[0]:
        return result[0]
    abort(404)

def get_history_aqi():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
        SELECT id, ts, pm25 FROM `TermProjectAqi`
        """)
        result = [models.AQI(*row) for row in cs.fetchall()]
        return result

def get_history_temperature_precipitation():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
        SELECT id, ts, temp, precipitaionProb FROM `TermProjectTemp`
        """)
        result = [models.TemperaturePrecipitation(*row) for row in cs.fetchall()]
        return result

def get_history_uv_index():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
        SELECT id, ts, uv FROM `TermProjectUV`
        """)
        result = [models.UV(*row) for row in cs.fetchall()]
        return result