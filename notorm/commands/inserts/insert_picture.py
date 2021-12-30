from sqlalchemy import insert

from notorm.utils.db_api.alchemy import picture, engine

conn = engine.connect()
ins = insert(picture)

row = conn.execute(ins, [
    {
        'id': '1',
        'url': 'https://i.imgur.com/WZ2zWbU.jpg'
    },
    {
        'id': '2',
        'url': 'https://i.imgur.com/tZKO08g.jpg'
    },
    {
        'id': '3',
        'url': 'https://i.imgur.com/wmTayLF.jpg'
    }
])
