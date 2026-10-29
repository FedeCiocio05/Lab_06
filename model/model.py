import mysql
from mysql.connector import errorcode

from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        #stabilisco la connessione
        cnx = get_connection()
        if cnx is None:
            raise ConnectionError("Impossibile connettersi al database.")

        cursor = cnx.cursor()
        try:
            query = """
                        SELECT *
                        FROM strumento
                    """
            cursor.execute(query)

            lista_strumenti = []
            for row in cursor:
                lista_strumenti.append(Strumento(row[0],
                                                 row[1],
                                                 row[2],
                                                 row[3],
                                                 row[4],
                                                 row[5])
                                       )
            return lista_strumenti
        finally:    #a prescindere dal try chiudo la connessione
            cursor.close()
            cnx.close()

        # TODO

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        #stabilisco la connessione
        cnx = get_connection()
        if cnx is None:
            raise ConnectionError("Impossibile connettersi al database.")

        cursor = cnx.cursor()
        try:
            query = """
                        SELECT *
                        FROM strumento
                        WHERE tipo = %s
                    """
            cursor.execute(query, (tipo,)) #parametro {tipo <--> %s}

            strumenti_per_tipo = []
            for row in cursor:
                strumenti_per_tipo.append(Strumento(row[0],
                                                     row[1],
                                                     row[2],
                                                     row[3],
                                                     row[4],
                                                     row[5])
                                       )
            return strumenti_per_tipo
        finally:  # a prescindere dal try chiudo la connessione
            cursor.close()
            cnx.close()
        # TODO
