from sqlalchemy import insert

from utils.db_api.alchemy import goods, engine

conn = engine.connect()
ins = insert(goods)

row = conn.execute(ins, [
    {
        'id': '1',
        'name': 'Laptop',
        'description': 'Good laptop!',
        'price': '1000'
    },
    {
        'id': '2',
        'name': 'PC',
        'description': 'Good PC!',
        'price': '2000'
    },
    {
        'id': '3',
        'name': 'Dildo',
        'description': 'Good Dildo!',
        'price': '300'
    },

])

