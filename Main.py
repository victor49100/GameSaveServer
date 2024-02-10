import shutil
import zipfile
from tkinter import filedialog

import mysql.connector
from mysql.connector import Error
import pandas as pd
import Gui
import os

def create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="82.66.184.236",  # ici l'ip de la BDD
            user="victor2",
            passwd="freebox",
            database="SaveGame"
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Error as err:
        print(f"Error: '{err}'")


def pushZip(zip_file_path, GameName):
    GameID = getGameID(GameName)
    try:
        # Ouvrir et lire le fichier .zip en tant que flux binaire
        with open(zip_file_path, 'rb') as zip_file:
            zip_data = zip_file.read()
            # Exécuter la requête SQL pour insérer les données binaires dans la table
            cursor = connection.cursor()
            print(GameID)
            query = "INSERT INTO `SaveZip` (GameId, DateAjout, Save) VALUES (%s, CURRENT_TIMESTAMP(), %s)"
            cursor.execute(query, (GameID, zip_data))

            connection.commit()
            print("Fichier .zip inséré avec succès.")
            os.remove(zip_file_path)
    except Error as e:
        print(f"Erreur lors de l'insertion du fichier .zip : {e}")


def getGameID(GameName):
    if connection is not None:
        query = f"SELECT GameId.GameId FROM GameId WHERE GameId.NomDuJeu LIKE '%{GameName}%'; "
        results = execute_query(connection, query)
        if results:
            return results[0]['GameId']


def querySelectAllGames():
    if connection is not None:
        query = f"SELECT  GameId.* FROM GameId"
        results = execute_query(connection, query)
        if results:
            return results


def queryAdd(GameName):
    if connection is not None:
        if (GameName != "\n"):
            query = f"INSERT INTO `GameId` VALUES (NULL, '{GameName}');"
            # Exécutez la requête et obtenez les résultats
            results = execute_query(connection, query)
            connection.commit()
            if results:
                df = pd.DataFrame(results)
                print(df)
        else:
            print("pas de nom de jeu entrée")
            return 0


connection = create_server_connection()
