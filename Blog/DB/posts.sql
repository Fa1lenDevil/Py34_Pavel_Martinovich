DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    dateOfRegistration TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);