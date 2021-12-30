from sqlalchemy.dialects.postgresql import insert

from utils.db_api.alchemy import users, engine

user_info = insert(users).values(
    name='Дмитрий',
    username='dima228'
)

print(user_info)

conn = engine.connect()
row = conn.execute(user_info)