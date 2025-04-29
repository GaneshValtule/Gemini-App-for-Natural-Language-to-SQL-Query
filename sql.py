import sqlite3

connection = sqlite3.connect('sales.db')

cursor = connection.cursor()

table_info = """
CREATE TABLE sales (
    id INT PRIMARY KEY,
    sale_date DATE,
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10, 2),
    total DECIMAL(10, 2)
);

"""

cursor.execute(table_info)

cursor.executescript("""
INSERT INTO sales VALUES
(1, '2025-04-01', 'Alice Johnson', 'Laptop', 1, 850.00, 850.00),
(2, '2025-04-01', 'Bob Smith', 'Smartphone', 2, 400.00, 800.00),
(3, '2025-04-02', 'Charlie Evans', 'Tablet', 1, 300.00, 300.00),
(4, '2025-04-02', 'Diana King', 'Monitor', 2, 150.00, 300.00),
(5, '2025-04-03', 'Ethan Green', 'Keyboard', 5, 20.00, 100.00),
(6, '2025-04-03', 'Fiona Baker', 'Mouse', 3, 15.00, 45.00),
(7, '2025-04-04', 'George Allen', 'Printer', 1, 200.00, 200.00),
(8, '2025-04-04', 'Hannah Scott', 'Laptop', 1, 870.00, 870.00),
(9, '2025-04-05', 'Ian Clark', 'Smartwatch', 2, 120.00, 240.00),
(10, '2025-04-05', 'Jane Lewis', 'Tablet', 2, 310.00, 620.00),
(11, '2025-04-06', 'Kyle Young', 'Laptop', 1, 900.00, 900.00),
(12, '2025-04-06', 'Laura Walker', 'Monitor', 1, 180.00, 180.00),
(13, '2025-04-07', 'Mike Hall', 'Keyboard', 2, 25.00, 50.00),
(14, '2025-04-07', 'Nina Adams', 'Mouse', 4, 18.00, 72.00),
(15, '2025-04-08', 'Oliver Wright', 'Smartphone', 1, 420.00, 420.00),
(16, '2025-04-08', 'Paula Turner', 'Tablet', 1, 305.00, 305.00),
(17, '2025-04-09', 'Quentin Harris', 'Printer', 1, 210.00, 210.00),
(18, '2025-04-09', 'Rachel Wood', 'Smartwatch', 3, 115.00, 345.00),
(19, '2025-04-10', 'Sam Cooper', 'Monitor', 2, 160.00, 320.00),
(20, '2025-04-10', 'Tina Reed', 'Laptop', 1, 890.00, 890.00),
(21, '2025-04-11', 'Uma Perry', 'Keyboard', 3, 22.00, 66.00),
(22, '2025-04-11', 'Victor Bell', 'Mouse', 2, 16.00, 32.00),
(23, '2025-04-12', 'Wendy Jenkins', 'Tablet', 2, 295.00, 590.00),
(24, '2025-04-12', 'Xavier Price', 'Smartphone', 1, 430.00, 430.00),
(25, '2025-04-13', 'Yasmine Barnes', 'Monitor', 1, 170.00, 170.00),
(26, '2025-04-13', 'Zack Morgan', 'Printer', 2, 190.00, 380.00),
(27, '2025-04-14', 'Alice Johnson', 'Smartwatch', 1, 125.00, 125.00),
(28, '2025-04-14', 'Bob Smith', 'Mouse', 3, 14.00, 42.00),
(29, '2025-04-15', 'Charlie Evans', 'Laptop', 1, 880.00, 880.00),
(30, '2025-04-15', 'Diana King', 'Tablet', 1, 310.00, 310.00),
(31, '2025-04-16', 'Ethan Green', 'Smartphone', 2, 410.00, 820.00),
(32, '2025-04-16', 'Fiona Baker', 'Monitor', 1, 165.00, 165.00),
(33, '2025-04-17', 'George Allen', 'Keyboard', 4, 23.00, 92.00),
(34, '2025-04-17', 'Hannah Scott', 'Mouse', 2, 17.00, 34.00),
(35, '2025-04-18', 'Ian Clark', 'Smartwatch', 1, 130.00, 130.00),
(36, '2025-04-18', 'Jane Lewis', 'Printer', 1, 220.00, 220.00),
(37, '2025-04-19', 'Kyle Young', 'Laptop', 2, 860.00, 1720.00),
(38, '2025-04-19', 'Laura Walker', 'Tablet', 1, 300.00, 300.00),
(39, '2025-04-20', 'Mike Hall', 'Smartphone', 1, 440.00, 440.00),
(40, '2025-04-20', 'Nina Adams', 'Monitor', 2, 155.00, 310.00),
(41, '2025-04-21', 'Oliver Wright', 'Keyboard', 3, 21.00, 63.00),
(42, '2025-04-21', 'Paula Turner', 'Mouse', 1, 15.00, 15.00),
(43, '2025-04-22', 'Quentin Harris', 'Tablet', 2, 310.00, 620.00),
(44, '2025-04-22', 'Rachel Wood', 'Smartwatch', 2, 110.00, 220.00),
(45, '2025-04-23', 'Sam Cooper', 'Printer', 1, 205.00, 205.00),
(46, '2025-04-23', 'Tina Reed', 'Monitor', 1, 175.00, 175.00),
(47, '2025-04-24', 'Uma Perry', 'Laptop', 1, 865.00, 865.00),
(48, '2025-04-24', 'Victor Bell', 'Smartphone', 2, 400.00, 800.00),
(49, '2025-04-25', 'Wendy Jenkins', 'Tablet', 1, 290.00, 290.00),
(50, '2025-04-25', 'Xavier Price', 'Mouse', 4, 16.00, 64.00);

""")

print("Data of Sales table is ")

data = cursor.execute(" SELECT * FROM sales")

for row in data:
    print(row)

connection.commit()
connection.close()