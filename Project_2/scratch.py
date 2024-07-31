import mysql.connector as connector


class DBHelper:

    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='1234#MD',
                                     database='food_ordering')

    def create_table_customer(self):
        query = 'CREATE TABLE if not exists persons (id INT AUTO_INCREMENT primary key,name VARCHAR(255),password ' \
                'VARCHAR(20),' \
                'email VARCHAR(255),contact_no VARCHAR(20))'
        cur = self.con.cursor()
        cur.execute(query)
        print("customers_table_Created")

    def create_table_orders(self):
        query = 'create table if not exists orders (order_id INT  PRIMARY KEY,customer_id varchar(20) ,' \
                ' item_id INT ,order_date DATE ,total_price DECIMAL(10, 2) ,' \
                'FOREIGN KEY (item_id) REFERENCES menu(' \
                'S_no)) '
        cur = self.con.cursor()
        cur.execute(query)
        print("table_orders_Created")

    def register_customer(self, id, name, password, email, phone):
        query = "INSERT INTO persons (id, name, password,email, contact_no)  VALUES ({},'{}','{}','{}','{}')".format(id,
                                                                                                                     name,
                                                                                                                     password,
                                                                                                                     email,
                                                                                                                     phone)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Customer registered successfully")

    def delete_table(self):
        query = "drop table persons"
        cur = self.con.cursor()
        cur.execute(query)

    def delete_table_orders(self):
        query = "drop table orders"
        cur = self.con.cursor()
        cur.execute(query)


helper = DBHelper()

#helper.create_table_customer()
#helper.create_table_menu()
#helper.delete_table_orders()
# helper.delete_table()
helper.create_table_orders()
# helper.register_customer(1, 'Ram', 'Ram123', 'ram.ram@gmail.com', '9877864532')
# helper.register_customer(2, 'Gita', 'Gita345', 'gita.gita@gmail.com', '7698986754')
# helper.register_customer(3, 'Manan', 'Manan567', 'manan.manan@gmail.com', '9453674528')
# helper.register_customer(4, 'Shyam', 'Shyam897', 'shyam.shyam@gmail.com', '9234563456')
# helper.register_customer(5, 'Sita', 'Sita123', 'sita.sita@gmail.com', '8756453750')
