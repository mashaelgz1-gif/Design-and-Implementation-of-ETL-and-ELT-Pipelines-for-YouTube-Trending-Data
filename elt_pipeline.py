import pandas as pd
import sqlite3
from sqlalchemy import create_engine

sqlite_path = "/youtube_elt_source.db"
csv_path = "USvideos.csv"
conn_sqlite = sqlite3.connect(sqlite_path)
df_categories = pd.read_sql_query("SELECT * FROM legacy_categories", conn_sqlite)
conn_sqlite.close()

df_videos = pd.read_csv(csv_path)

DATABASE_URL = "YOUR_DATABASE_URL"

engine = create_engine(DATABASE_URL)

df_categories.to_sql("stage_categories", engine, if_exists="replace", index=False)
df_videos.to_sql("stage_usvideos", engine, if_exists="replace", index=False)

print("Data loaded into Neon successfully")
