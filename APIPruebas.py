import sys
from mariadb import connect, Error

class DatabaseConnection:

    def __init__(self, host, port, user, database, password):
        self.host = host
        self.port = port
        self.user = user
        self.database = database
        self.password = password
        self.connect()

    def connect(self):

        try:
            self.conn=connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
        except Error as e:
            print(f"Error conectando a la base de datos {e}")
            sys.exit(1)
        else:
            print("Conexión realizada a la base de datos.")

    def close(self):
        self.conn.close()

    def execute_query(self,query):
        self.conn.cursor().execute(query)

    def get_cursor(self):
        return self.conn.cursor()

class Producto:
    def __init__(self, id, nombre, marca, precio, stock ):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id} Nombre: {self.nombre} Marca: {self.marca} Precio: {self.precio} Stock: {self.stock}"
    
class ProductosDBConnection(DatabaseConnection):
    
    def __init__(self, host, port, user, database, password):
        super().__init__(host, port, user, database, password)

    def list_productos(self):
        productos_lista = []
        cur=self.get_cursor()
        cur.execute("select * from productos")
        for (id, nombre, marca, precio, stock) in cur:
            productos_lista.append(Producto(id, nombre, marca, precio, stock))
        return productos_lista
    
    def get_productos_by_marca(self, marca):
        productos_lista_marca = []
        cur = self.get_cursor()
        cur.execute("Select * from productos where marca = ?",(marca,))
        for (id, nombre, marca, precio, stock) in cur:
            productos_lista_marca.append(Producto(id, nombre, marca, precio, stock))
        return productos_lista_marca
    
    def get_productos_by_id(self, id):
        cur = self.get_cursor()
        cur.execute("Select * from productos where id = ?",(id,))
        for (id, nombre, marca, precio, stock) in cur:
            return Producto(id, nombre, marca, precio, stock)
        
    def delete_productos(self, id):
        print ("Pasa por aqui")
        self.get_cursor().execute("delete from productos where id = ?", (id,))
        self.conn.commit()
        
    def insert_productos(self, nombre, marca, precio, stock):
        self.get_cursor().execute("insert into productos (nombre, marca, precio, stock) values(?,?,?,?)", (nombre, marca, precio, stock))
        self.conn.commit()
    
    def actualiza_productos(self, nombre, marca, precio, stock, id):
        self.get_cursor().execute("update productos set nombre = ?, marca = ?, precio = ?, stock = ? where id = ?", (nombre, marca, precio, stock, id))
        self.conn.commit()
        