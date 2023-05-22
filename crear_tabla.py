from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
import urllib.parse

server_name = 'servidorpostgresql.database.windows.net'
database_name = 'erney'
username = 'erneypuetate'
password = '@Adolfo2008'
encoded_password = urllib.parse.quote_plus(password)

# Crear el URI de conexión
#url = f"mssql+pymssql://{username}:{encoded_password}@{server_name}/{database_name}"
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Crea una instancia del motor de SQLAlchemy
server_name = 'servidorpostgresql.database.windows.net'
database_name = 'erney'
username = 'erneypuetate'
password = '@Adolfo2008'
encoded_password = urllib.parse.quote_plus(password)

# Crear el URI de conexión
uri = f"mssql+pymssql://{username}:{encoded_password}@{server_name}/{database_name}"
engine = create_engine(uri)
# Define la tabla
metadata = MetaData(bind=engine)

tabla = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(50)),
              Column('email', String(50)),
              Column('password', String(50))
              )

# Verifica si la tabla existe antes de crearla
tabla.create()
engine.dispose()
print("La tabla ha sido creada.")

