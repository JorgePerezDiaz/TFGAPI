from APIPruebas import ProductosDBConnection

db = ProductosDBConnection("127.0.0.1",3307,"root","productos","vialactea9")

def get_db():
    return db
