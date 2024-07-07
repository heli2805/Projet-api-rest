# models.py

from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2.extras

def create_tables():
    conn = current_app.config['db']
    cur = conn.cursor()

    cur.execute('''
    CREATE TYPE user_role AS ENUM ('admin', 'user');
    CREATE TABLE IF NOT EXISTS "Group" (
        groupID SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS "User" (
        userID SERIAL PRIMARY KEY,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        login VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        role user_role NOT NULL,
        groupID INT,
        FOREIGN KEY(groupID) REFERENCES "Group"(groupID)
    );

    CREATE TABLE IF NOT EXISTS "Prompt" (
        promptID SERIAL PRIMARY KEY,
        content TEXT NOT NULL,
        status VARCHAR(50) NOT NULL,
        price DECIMAL(10, 2) NOT NULL DEFAULT 1000.00,
        creationDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        editDate TIMESTAMP,
        userID INT,
        FOREIGN KEY(userID) REFERENCES "User"(userID)
    );

    CREATE TABLE IF NOT EXISTS "Vote" (
        voteID SERIAL PRIMARY KEY,
        voteValue INT NOT NULL,
        userID INT NOT NULL,
        promptID INT NOT NULL,
        FOREIGN KEY(userID) REFERENCES "User"(userID),
        FOREIGN KEY(promptID) REFERENCES "Prompt"(promptID)
    );

    CREATE TABLE IF NOT EXISTS "Note" (
        noteID SERIAL PRIMARY KEY,
        noteValue INT NOT NULL,
        userID INT NOT NULL,
        promptID INT NOT NULL,
        FOREIGN KEY(userID) REFERENCES "User"(userID),
        FOREIGN KEY(promptID) REFERENCES "Prompt"(promptID)
    );
    ''')

    conn.commit()
    cur.close()

def hash_password(password):
    return generate_password_hash(password)

def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)
