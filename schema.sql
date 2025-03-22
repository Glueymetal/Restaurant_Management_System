CREATE TABLE Tables (
    table_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_number INTEGER NOT NULL UNIQUE,
    capacity INTEGER NOT NULL,
    location TEXT
);

CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Manager', 'Chef', 'Waiter', 'Host')), -- Replacing ENUM with CHECK
    phone_number TEXT,
    email TEXT,
    hire_date DATE NOT NULL
);

CREATE TABLE Shifts (
    shift_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    shift_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    manager_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);

CREATE TABLE Reservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    phone_number TEXT,
    table_id INTEGER NOT NULL,
    waiter_id INTEGER,
    host_id INTEGER,
    manager_id INTEGER, -- Track which manager approved the reservation
    reservation_date DATE NOT NULL,
    reservation_time TIME NOT NULL,
    status TEXT DEFAULT 'Pending' CHECK(status IN ('Pending', 'Confirmed', 'Cancelled')), -- Replacing ENUM with CHECK
    FOREIGN KEY (table_id) REFERENCES Tables(table_id),
    FOREIGN KEY (waiter_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (host_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);

CREATE TABLE Menu (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    category TEXT,
    price REAL NOT NULL,
    availability BOOLEAN DEFAULT TRUE
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    reservation_id INTEGER NOT NULL,
    waiter_id INTEGER,
    manager_approval BOOLEAN DEFAULT FALSE,
    order_date DATE NOT NULL,
    total_amount REAL NOT NULL,
    FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id),
    FOREIGN KEY (waiter_id) REFERENCES Employees(employee_id)
);

CREATE TABLE OrderDetails (
    order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    cook_id INTEGER,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (item_id) REFERENCES Menu(item_id),
    FOREIGN KEY (cook_id) REFERENCES Employees(employee_id)
);

-- View for available tables at a specific date and time
CREATE VIEW AvailableTables AS
SELECT Tables.table_id, Tables.table_number, Tables.capacity,Tables.location
FROM Tables
WHERE Tables.table_id NOT IN (
    SELECT table_id
    FROM Reservations
    WHERE reservation_date = DATE('now') AND reservation_time = TIME('now')
);

-- View for daily total sales
CREATE VIEW DailySales AS
SELECT order_date, SUM(total_amount) AS total_sales
FROM Orders
GROUP BY order_date;

-- Index for quickly checking available tables by their table numbers
CREATE INDEX check_table_number ON Tables (table_number);
-- Index for checking reservations by date and time
CREATE INDEX check_reservation_datetime ON Reservations (reservation_date, reservation_time);
-- Index for filtering employees by role
CREATE INDEX filter_employee_role ON Employees (role);
-- Index for scheduling and querying shifts by date
CREATE INDEX check_shift_date ON Shifts (shift_date);
-- Index for querying orders by date
CREATE INDEX check_order_date ON Orders (order_date);
