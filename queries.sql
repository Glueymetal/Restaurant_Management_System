-- Inserting values into the tables

-- Insert data into Tables
INSERT INTO Tables (table_number, capacity, location)
VALUES
    (1, 4, 'Main Hall'),
    (2, 6, 'Main Hall'),
    (3, 2, 'Patio'),
    (4, 4, 'Private Room');

-- Insert data into Employees
INSERT INTO Employees (name, role, phone_number, email, hire_date)
VALUES
    ('John', 'Manager', '1234567890', 'john@star_resturant.com', '2020-01-15'),
    ('Jane', 'Chef', '9876543210', 'jane@star_resturant.com', '2021-03-01'),
    ('Emily', 'Waiter', '5551234567', 'emily@star_resturant.com', '2022-05-20'),
    ('White', 'Host', '4449876543', 'michael@star_resturant.com', '2023-06-12'),
    ('Maggie','Chef','9874352109', 'Maggie@star_resturant.com','2020-01-03');

-- Insert data into Shifts
INSERT INTO Shifts (employee_id, shift_date, start_time, end_time, manager_id)
VALUES
    (3, '2024-12-13', '10:00:00', '14:00:00', 1),
    (4, '2024-12-13', '12:00:00', '16:00:00', 1),
    (2, '2024-12-13', '18:00:00', '22:00:00', 1);

-- Insert data into Reservations
INSERT INTO Reservations (customer_name, phone_number, table_id, waiter_id, host_id, manager_id, reservation_date, reservation_time, status)
VALUES
    ('Alan Johnson', '3337779999', 1, 3, 4, 1, '2024-12-15', '18:30:00', 'Confirmed'),
    ('Beatrice Wilson', '2226668888', 3, 3, 4, 1, '2024-12-15', '19:00:00', 'Pending');

-- Insert data into Menu
INSERT INTO Menu (item_name, category, price, availability)
VALUES
    ('Margherita Pizza', 'Main Course', 12.50, 1),
    ('Caesar Salad', 'Appetizer', 7.25, 1),
    ('Chocolate Lava Cake', 'Dessert', 6.00, 1),
    ('Espresso', 'Beverage', 3.50, 1);

-- Insert data into Orders
INSERT INTO Orders (reservation_id, waiter_id, manager_approval, order_date, total_amount)
VALUES
    (1, 3, TRUE, '2024-12-15', 26.50),
    (2, 3, FALSE, '2024-12-15', 19.75),
    (2, 3, TRUE, '2024-12-15', 15.00);

-- Insert data into OrderDetails
INSERT INTO OrderDetails (order_id, item_id, cook_id, quantity)
VALUES
    (1, 1, 2, 1), -- Margherita Pizza
    (1, 2, 2, 1), -- Caesar Salad
    (2, 3, 2, 1), -- Chocolate Lava Cake
    (2, 4, 2, 2), -- 2 Espressos
    (3, 4, 5, 1), -- 1 Espresso
    (3, 3, 5, 1); -- Chocolate Lava Cake

-- Select Queries Using Tables

-- Get Menu Items with Their Prices
SELECT item_name, price
FROM Menu
WHERE availability = TRUE;

-- Get All Reservations and Their Status
SELECT reservation_id, customer_name, reservation_date, reservation_time, status
FROM Reservations;

-- Get employee shift details of a particular role and at a particular date
SELECT Employees.name, Shifts.shift_date, Shifts.start_time, Shifts.end_time
FROM Employees
JOIN Shifts ON Employees.employee_id = Shifts.employee_id
WHERE Employees.role = 'Chef' AND Shifts.shift_date > '2020-12-11';

-- Get order details with total price per item
SELECT Orders.order_id, Orders.order_date, Menu.item_name, OrderDetails.quantity, (OrderDetails.quantity * Menu.price) AS total_price
FROM Orders
JOIN OrderDetails ON Orders.order_id = OrderDetails.order_id
JOIN Menu ON OrderDetails.item_id = Menu.item_id;


-- Select Queries Using Views

--  Get Available Tables for a Specific Date and Time
SELECT *
FROM AvailableTables
WHERE reservation_date = '2024-12-15' AND reservation_time = '19:00:00';

-- Get Total Sales until to the present moment
SELECT SUM(total_sales) FROM DailySales;
