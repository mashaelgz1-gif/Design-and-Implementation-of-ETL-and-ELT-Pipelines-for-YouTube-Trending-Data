import pandas as pd
import sqlite3
from sqlalchemy import create_engine

sqlite_path = "/Users/mashaelalqzlan/Desktop/sqlite-tools-osx-arm64-3510200/youtube_elt_source.db"
csv_path = "USvideos.csv"
conn_sqlite = sqlite3.connect(sqlite_path)
df_categories = pd.read_sql_query("SELECT * FROM legacy_categories", conn_sqlite)
conn_sqlite.close()

df_videos = pd.read_csv(csv_path)

engine = create_engine(
    "postgresql+psycopg2://neondb_owner:npg_TeCRUh4PYp1L@ep-flat-butterfly-an76x6b1-pooler.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

df_categories.to_sql("stage_categories", engine, if_exists="replace", index=False)
df_videos.to_sql("stage_usvideos", engine, if_exists="replace", index=False)

print("Data loaded into Neon successfully")
