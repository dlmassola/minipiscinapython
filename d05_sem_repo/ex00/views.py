from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from psycopg2 import sql
from django.db import connection

def init(request):
    try:
        # Establish a connection to PostgreSQL
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_db_user",
            password="your_db_password",
            host="your_db_host",
            port="your_db_port"
        )
        cursor = conn.cursor()

        # Create the ex00_movies table if it doesn't exist
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex00_movies (
                    title varchar(64) UNIQUE NOT NULL,
                    episode_nb serial PRIMARY KEY,
                    opening_crawl text,
                    director varchar(32) NOT NULL,
                    producer varchar(128) NOT NULL,
                    release_date date NOT NULL
                )
            """)
        
        conn.commit()
        conn.close()
        
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
