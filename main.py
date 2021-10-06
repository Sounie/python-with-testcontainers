if __name__ == '__main__':
    import sqlalchemy
    from testcontainers.mysql import MySqlContainer

    with MySqlContainer('mysql:5.7.17') as mysql:
        print(f"connection url: {mysql.get_connection_url()}")
        engine = sqlalchemy.create_engine(mysql.get_connection_url())
        version, = engine.execute("select version()").fetchone()
        print(f'MySQL version: {version}')  # 5.7.17, as specified above
