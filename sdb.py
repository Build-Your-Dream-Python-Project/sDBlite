import sqlite3

class PrimaryKey:
    pass

class Connection:
    def __init__(self, file_path, log=False):
        self.connection = sqlite3.connect(file_path)
        self.cursor = self.connection.cursor()
        if log:
            print(f"Connected to database: {file_path}")

    def close(self, log=False):
        self.cursor.close()
        self.connection.close()
        if log:
            print("Connection closed.")

    class Table:
        def __init__(self, connection, table_name):
            self.connection = connection
            self.cursor = self.connection.cursor()
            self.table_name = table_name

        def create(self, columns, log=False):
            try:
                query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
                for column_name, data_type in columns.items():
                    if data_type == str:
                        query += f"{column_name} TEXT, "
                    elif data_type == int:
                        query += f"{column_name} INTEGER, "
                    elif data_type == PrimaryKey:
                        query += f"{column_name} INTEGER PRIMARY KEY AUTOINCREMENT, "
                    else:
                        print(f"Invalid data type for column '{column_name}'.")
                        return
                query = query.rstrip(", ") + ")"
                self.cursor.execute(query)
                if log:
                    print(f"Table '{self.table_name}' created successfully.")
            except Exception as e:
                print(f"Error creating table: {e}")

            return self  # Return the Table object itself

        def drop(self, log=False):
            try:
                query = f"DROP TABLE IF EXISTS {self.table_name}"
                self.cursor.execute(query)
                if log:
                    print(f"Table '{self.table_name}' dropped successfully.")
            except Exception as e:
                print(f"Error dropping table: {e}")

        def insert(self, values, log=False):
            try:
                query = f"INSERT INTO {self.table_name} VALUES ("
                for value in values:
                    if isinstance(value, str):
                        query += f"'{value}', "
                    else:
                        query += f"{value}, "
                query = query.rstrip(", ") + ")"
                self.cursor.execute(query)
                self.connection.commit()
                if log:
                    print(f"Row inserted into table '{self.table_name}' successfully.")
            except Exception as e:
                print(f"Error inserting row: {e}")

        def select(self, columns=None):
            try:
                if columns:
                    query = f"SELECT {', '.join(columns)} FROM {self.table_name}"
                else:
                    query = f"SELECT * FROM {self.table_name}"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                return rows
            except Exception as e:
                print(f"Error selecting rows: {e}")

        def close(self, log=False):
            self.cursor.close()
            self.connection.close()
            if log:
                print("Connection closed.")

def connect(file_path, log=False):
    return Connection(file_path, log=log)

def table(self, table_name):
    return self.Table(self.connection, table_name)

setattr(Connection, "table", table)
