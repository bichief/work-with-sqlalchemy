from sqlalchemy import select
from utils.db_api.alchemy import engine, users, goods

conn = engine.connect()

s = select([goods]).where(
    (goods.c.price > 300) &
    (goods.c.name == 'PC')
)
r = conn.execute(s)
print(r.fetchall())