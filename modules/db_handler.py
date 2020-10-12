import sqlite3

CREATE_TABLE = '''
                CREATE TABLE IF NOT EXISTS dry_storage(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    food TEXT,
                    quantity INTEGER,
                    metric TEXT
                )
                '''

INSERT_DATA = '''
                INSERT INTO dry_storage(
                    food,
                    quantity,
                    metric
                )
                VALUES (?, ?, ?)
              '''

TEST_DATA = (
    ('Noodles', 4, 'st'),
    ('Flour', 1.5, 'kg')
)


def open_connection(db_file):
    return sqlite3.connect(db_file)


def create_table(connection):
    try:
        connection.execute(CREATE_TABLE)
    except Exception as e:
        print(e)
        raise


def insert_data(connection):
    try:
        with connection:
            connection.executemany(INSERT_DATA, TEST_DATA)
    except sqlite3.IntegrityError:
        print('Couldn\'t add X twice')
    except Exception:
        print('Failed')
        raise


def main():
    connection = open_connection('example.db')
    with connection:
        create_table(connection)
        insert_data(connection)


main()
