-- Connexion à la base de données
\c projet_api_rest_bd;

-- Création du type ENUM pour le rôle
CREATE TYPE user_role AS ENUM ('admin', 'user');

-- Création des tables
CREATE TABLE "Group" (
    groupID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE "User" (
    userID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    login VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role user_role NOT NULL,
    groupID INT,
    FOREIGN KEY(groupID) REFERENCES "Group"(groupID)
);

CREATE TABLE "Prompt" (
    promptID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    content TEXT NOT NULL,
    status VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL DEFAULT 1000.00,
    creationDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    editDate TIMESTAMP,
    userID INT,
    FOREIGN KEY(userID) REFERENCES "User"(userID)
);

CREATE TABLE "Vote" (
    voteID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    voteValue INT NOT NULL,
    userID INT NOT NULL,
    promptID INT NOT NULL,
    FOREIGN KEY(userID) REFERENCES "User"(userID),
    FOREIGN KEY(promptID) REFERENCES "Prompt"(promptID)
);

CREATE TABLE "Note" (
    noteID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    noteValue INT NOT NULL,
    userID INT NOT NULL,
    promptID INT NOT NULL,
    FOREIGN KEY(userID) REFERENCES "User"(userID),
    FOREIGN KEY(promptID) REFERENCES "Prompt"(promptID)
);
