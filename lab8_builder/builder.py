"""Implementation of the Builder pattern"""

from abc import ABC, abstractmethod


class QueryBuilder(ABC):
    @abstractmethod
    def select(self, columns):
        """SELECT query construction logic"""
        pass

    @abstractmethod
    def where(self, condition):
        """The logic of building the WHERE condition"""
        pass

    @abstractmethod
    def limit(self, limit):
        """The logic of building the LIMIT constraint"""
        pass

    @abstractmethod
    def getSQL(self):
        """The logic of receiving a ready SQL query"""
        pass


class PostgreSQLQueryBuilder(QueryBuilder):
    def select(self, columns):
        """The logic of constructing a SELECT query for PostgreSQL"""
        pass

    def where(self, condition):
        """The logic of building a WHERE condition for PostgreSQL"""
        pass

    def limit(self, limit):
        """Logic for building the LIMIT constraint for PostgreSQL"""
        pass

    def getSQL(self):
        """The logic for obtaining a ready SQL query for PostgreSQL"""
        pass


class MySQLQueryBuilder(QueryBuilder):
    def select(self, columns):
        """The logic of constructing a SELECT query for MySQL"""
        pass

    def where(self, condition):
        """The logic of building a WHERE condition for MySQL"""
        pass

    def limit(self, limit):
        """Logic for building the LIMIT constraint for MySQL"""
        pass

    def getSQL(self):
        """The logic for obtaining a ready SQL query for MySQL"""
        pass
