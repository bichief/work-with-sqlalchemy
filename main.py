from notorm.utils.db_api.alchemy import engine, metadata

metadata.create_all(engine)  # создает таблицы