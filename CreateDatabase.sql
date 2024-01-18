-- Création de la base de données SaveGame
CREATE DATABASE IF NOT EXISTS SaveGame;

-- Utilisation de la base de données SaveGame
USE SaveGame;

-- Table GameId
CREATE TABLE IF NOT EXISTS GameId (
    GameId INT AUTO_INCREMENT,
    NomDuJeu VARCHAR(255),
    PRIMARY KEY (GameId)
);

-- Table GamePath
CREATE TABLE IF NOT EXISTS GamePath (
    GameId INT,
    Linux TINYTEXT,
    Windows TINYTEXT,
    PRIMARY KEY (GameId),
    FOREIGN KEY (GameId) REFERENCES GameId(GameId)
);

-- Table SaveZip avec LONGBLOB limité à 64 Mo
CREATE TABLE IF NOT EXISTS SaveZip (
    GameId INT,
    SaveId INT AUTO_INCREMENT,
    DateAjout TIMESTAMP,
    Save LONGBLOB,
    PRIMARY KEY (SaveId),
    FOREIGN KEY (GameId) REFERENCES GameId(GameId),
    CHECK (LENGTH(Save) <= 67108864) -- 64 Mo en octets
);

