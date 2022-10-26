# **SQL**
## Database Management Systems
* MySQL
* PostgreSQL
* SQLite

### SQLite Types 
* TEXT
* NUMERIC
* INTEGER
* REAL
* BLOB

### SQL Types 
* CHAR (size)
* VARCHAR (size)
* SMALLINT
* INT
* BIGINT
* FLOAT
* DOUBLE
* MORE

### SQLite Commands: 

**1. CREATE TABLE**
```
CREATE TABLE flights(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEST NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);
```

**2. Insert Data: INSERT**
```
INSERT INTO flights
    (origin, destination, duration)
    VALUES("New York", "London", 415);
```

**3. Retrieve Data: SELECT**
```
SELECT * FROM flights; 

* - means everything
```

```
SELECT origin, destination FROM flights;

```
# Index SQLite table CREATE INDEX:

```
CREATE INDEX name_index ON passengers(last);
```

## Creating a SQLite database

```
touch flights.sql
sqlite3 flights.sql or sqlite3 <name>.db
```

# Checking SQLite tables

```
sqlite> .tables
```

# Formating SQLite tables

```
sqlite> .mode columns
```

