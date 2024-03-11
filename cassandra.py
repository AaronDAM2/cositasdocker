from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect()

# Create database
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS tutorial
    WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 }
    """)
session.set_keyspace('tutorial')
session.execute("""
    CREATE TABLE IF NOT EXISTS datos (
        nombre text PRIMARY KEY,
        tipo text,
        lenguaje text,
        fundacion int
    )
    """)

# Insert data
session.execute("""
    INSERT INTO datos (nombre, tipo, lenguaje, fundacion)
    VALUES ('Cassandra', 'Base de datos distribuida', 'Lenguaje de programación de alto nivel', 2008)
    """)

# Update data
session.execute("""
    UPDATE datos SET nombre = 'CassandraDB' WHERE nombre = 'Cassandra'
    """)

# Delete data
session.execute("""
    DELETE FROM datos WHERE lenguaje = 'Lenguaje de programación de alto nivel'
    """)

# Destruct database
session.execute("""
    DROP KEYSPACE tutorial
    """)
