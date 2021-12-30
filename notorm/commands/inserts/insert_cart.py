from sqlalchemy import insert

from notorm.utils.db_api.alchemy import cart, engine

conn = engine.connect()
ins = insert(cart)

row = conn.execute(ins, [
    {
        'user_id': '1',
        'goods_name': 'PC',
        'goods_price': '2000',
        'goods_id': '2'
    }
])