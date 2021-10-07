if __name__ == '__main__':
    import sqlalchemy
    from testcontainers.postgres import PostgresContainer

    with PostgresContainer('postgres:14.0-alpine') as postgresql:
        print(f"connection url: {postgresql.get_connection_url()}")
        engine = sqlalchemy.create_engine(postgresql.get_connection_url())
        version, = engine.execute("select version()").fetchone()
        print(f'Postgresql version: {version}')  # 14.0, as specified above
