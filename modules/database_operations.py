
import psycopg2 as pg
from psycopg2.extras import DictCursor
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from .app_settings import Settings_Json

from PyQt5.QtCore import QAbstractTableModel, QModelIndex
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery


class DataBase:
    def __init__(self):
        settings = Settings_Json().items
        self.__password = settings['PASSWORD']
        self.__dbname = settings["DBNAME"]
        self.__user = settings['USER']
        self.__hostname = settings['HOSTNAME']
        self.__port = settings['PORT']

        self.__connected_to_db = False
        self.__conn = None

    @property
    def database_status(self) -> bool:
        return self.__connected_to_db

    @database_status.setter
    def database_status(self, status: bool):
        self.__connected_to_db = status

    def connect_to_db_using_qt(self):
        self.db = QSqlDatabase("QPSQL")
        self.db.setDatabaseName(self.__dbname)
        self.db.setUserName(self.__user)
        self.db.setPassword(self.__password)

        if self.__hostname:
            self.db.setHostName(self.__hostname)
        if self.__port:
            self.db.setPort(self.__port)

        self.db.open()
        if not self.db.isOpen():
            print("Unable to connect to database using QT")
        else:
            self.__model = QSqlTableModel(db=self.db)
            self.__model.setTable("Sermons")
            self.__model.select()
            print("Successfully connected to database using Qt")

    @property
    def model(self):
        return self.__model

    def connect_to_db(self):
        try:
            self.__conn = pg.connect(database=self.__dbname, user=self.__user,
                                     password=self.__password, cursor_factory=DictCursor)
            self.database_status = True
            print("Connection to database successful")
        except pg.OperationalError as error:
            # TODO: Create new database
            # create the database if the application is installed in a new system
            conn = self.__create_database()
            self.__create_table(conn)

            # reconnect to the newly created database
            self.connect_to_db()
            pass
        except pg.Error as error:
            print("Unable to connect to database")
            print(error)

    def __create_database(self):
        query = """
CREATE DATABASE "GLH2"
    WITH
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    CONNECTION_LIMIT = -1;

COMMENT ON DATABASE "GLH2"
    Is 'God''s Lighthouse Database';
        """
        try:
            conn = pg.connect(user=self.__user, password=self.__password, cursor_factory=DictCursor)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            cursor = conn.cursor()
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            cursor.execute(query)
            return conn
        except pg.Error as error:
            print("Invalid Details")
            return

    def __create_table(self, conn):
        query = """
BEGIN;
CREATE TABLE IF NOT EXISTS "Sermons"
(
    "Messages" text NOT NULL,
    "Teachers" character varying,
    "Dates" date NOT NULL,
    "Id" character varying NOT NULL,
    "Summary" text,
    "Titles" character varying,
    "Themes" character varying,
    "Coordinators" character varying,
    PRIMARY KEY ("Id")
);
END;
        """
        try:
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            with conn:
                with conn.cursor(cursor_factory=DictCursor) as cursor:
                    sql = cursor.mogrify(query)
                    cursor.execute(query)
        except pg.Error as error:
            print(error)
            return

    def close_db(self):
        """close the database connection
        """        
        self.__conn.close()
        self.database_status = False
        print("Database closed successfully")

    def query_database(self, queries: str, *, mode, value=None):
        try:
            with self.__conn:
                with self.__conn.cursor(cursor_factory=DictCursor) as cursor:
                    if value is None:
                        raise ValueError("Value is None")
                    sql = cursor.mogrify(queries, value)
                    cursor.execute(queries, value)
                    if mode == 'select':
                        response = cursor.fetchall()
                        return response
                    return True
        except Exception as e:
            print(str(e))
            return False

    def insert_data_in_database(self, *, table_category, **kwargs):
        """Insert data in to the database

        Args:
            table_category (str): The table in the database where you want to insert
            the data

        Returns:
            None
        """
        query = f"""INSERT INTO "{table_category}" ({', '.join([f'"{key}"' for key in kwargs.keys()])}) """\
                f"""VALUES ({", ".join([f"%({val})s" for val in kwargs.keys()])});"""

        confirmation = self.query_database(query, mode="insert", value=kwargs)
        return confirmation

    def update_data_in_database(self, *, table_category, conditions: dict = None, **kwargs):
        if not isinstance(conditions, dict) or not conditions:
            raise TypeError("conditions must not be empty and of type dict")

        query = f"""UPDATE "{table_category}" SET {', '.join([f'"{key}" = %({key})s' for key in kwargs.keys()])} """ \
                f"""WHERE {" ".join([f'"{key}" = ' + f"%({key})s" for key in conditions.keys()])}"""

        kwargs.update(conditions)
        confirmation = self.query_database(query, mode='update', value=kwargs)
        return confirmation

    def retrieve_data_from_database(self, *cols, table_category=None, **conditions):
        if table_category is None:
            raise ValueError("Table category must not be None")

        query = f"""SELECT {', '.join([f'"{col}"' for col in cols])} FROM "{table_category}" """ \
                f"""WHERE {" ".join([f'"{key}" = ' + f"%({key})s" for key in conditions.keys()])}"""

        responses = self.query_database(query, mode="select", value=conditions)

        return responses

    def raw_query(self, query, value=None):
        responses = self.query_database(query, mode='select', value=value)
        return responses
