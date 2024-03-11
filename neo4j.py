from neo4j import GraphDatabase

# Connect to Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "adminpass"))

# Create database
with driver.session() as session:
    session.run("""
        CREATE (:BaseDatos {nombre: 'Neo4j', tipo: 'Base de datos grafica', lenguaje: 'Lenguaje de programación de alto nivel', fundacion: 2007})
        """)

# Update database
with driver.session() as session:
    session.run("""
        MATCH (n:BaseDatos)
        SET n.nombre = 'Neo4jDB'
        """)

# Delete database
with driver.session() as session
