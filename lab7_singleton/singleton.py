"""Implementation of the Singleton pattern"""

from abc import ABC, abstractmethod


class SingletonMeta(ABC):
    _instance = None

    @abstractmethod
    def execute_query(self, query):
        """Execution of a request to the DB"""
        pass


class PostgreSQLDatabase(SingletonMeta):
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            # Initialize the connection to PostgreSQL
        return cls._instance

    def execute_query(self, query):
        """Execution of a request to the PostgreSQL"""
        pass


class MongoDBDatabase(SingletonMeta):
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            # Initialize the connection to MongoDB
        return cls._instance

    def execute_query(self, query):
        """Execution of a request to the MongoDB"""
        pass


if __name__ == '__main__':
    postgres_db = PostgreSQLDatabase()
    postgres_db.execute_query("SELECT * FROM users")

    postgres_db2 = PostgreSQLDatabase()

    mongodb_db = MongoDBDatabase()
    mongodb_db.execute_query("db.users.find()")

    if id(postgres_db) == id(postgres_db2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
