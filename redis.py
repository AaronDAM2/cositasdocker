import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Create database
r.set('nombre', 'Redis')
r.set('tipo', 'Base de datos en memoria')
r.set('lenguaje', 'Lenguaje de programación de alto nivel')
r.set('fundacion', '2009')

# Update database
r.set('nombre', 'RedisDB')

# Delete database
r.delete('lenguaje')

# Destruct database
r.flushall()
