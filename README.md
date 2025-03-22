# Restaurant Management System Database

## Overview
This project is a database design for a **Restaurant Management System**, covering key aspects such as reservations, orders, employees, and menu management. The database is implemented using **SQLite** and ensures data integrity through structured relationships and constraints.

## Video Overview
For a visual explanation, refer to the video overview: [Watch Here](https://youtu.be/wsD1MKzy-yY)

## Scope
The database supports functionalities essential for managing restaurant operations efficiently, including:
- **Tables**: Information about dining tables.
- **Employees**: Staff details and roles.
- **Shifts**: Employee work schedules.
- **Reservations**: Customer reservation tracking.
- **Menu**: Menu items with pricing and availability.
- **Orders**: Customer order records.

### Out of Scope
- Detailed financial reports.
- Supplier inventory management.
- Customer loyalty programs.

## Functional Requirements
This database supports:
- **Manage Tables**: Add, update, and remove tables.
- **Employee Management**: Add/update/remove employee details and assign shifts.
- **Handle Reservations**: Create, update, cancel, and confirm reservations.
- **Order Management**: Track customer orders and calculate total amounts.
- **Menu Management**: Add, update, and remove menu items.
- **Shift Scheduling**: Assign employees to shifts.
- **Real-Time Table Availability**: Check table availability.
- **Sales and Performance Tracking**: Generate sales and employee schedule reports.

## Database Representation
The database is implemented in **SQLite** with the following entities:

### Entities and Schema
#### Tables
- `table_id` (INTEGER, PRIMARY KEY)
- `table_number` (INTEGER, UNIQUE, NOT NULL)
- `capacity` (INTEGER, NOT NULL)
- `location` (TEXT, NOT NULL)

#### Employees
- `employee_id` (INTEGER, PRIMARY KEY)
- `name` (TEXT, NOT NULL)
- `role` (TEXT, CHECK role IN ['Manager', 'Chef', 'Waiter', 'Host'])
- `phone_number` (TEXT)
- `email` (TEXT)
- `hire_date` (DATE, NOT NULL)

#### Shifts
- `shift_id` (INTEGER, PRIMARY KEY)
- `employee_id` (INTEGER, FOREIGN KEY references Employees)
- `shift_date` (DATE, NOT NULL)
- `start_time` (TIME, NOT NULL)
- `end_time` (TIME, NOT NULL)
- `manager_id` (INTEGER, FOREIGN KEY references Employees)

#### Reservations
- `reservation_id` (INTEGER, PRIMARY KEY)
- `customer_name` (TEXT, NOT NULL)
- `phone_number` (TEXT)
- `table_id` (INTEGER, FOREIGN KEY references Tables)
- `waiter_id` (INTEGER, FOREIGN KEY references Employees)
- `host_id` (INTEGER, FOREIGN KEY references Employees)
- `manager_id` (INTEGER, FOREIGN KEY references Employees)
- `reservation_date` (DATE, NOT NULL)
- `reservation_time` (TIME, NOT NULL)
- `status` (TEXT, CHECK status IN ['Pending', 'Confirmed', 'Cancelled'])

#### Menu
- `item_id` (INTEGER, PRIMARY KEY)
- `item_name` (TEXT, NOT NULL)
- `category` (TEXT, NOT NULL)
- `price` (REAL, NOT NULL)
- `availability` (BOOLEAN)

#### Orders
- `order_id` (INTEGER, PRIMARY KEY)
- `reservation_id` (INTEGER, FOREIGN KEY references Reservations)
- `waiter_id` (INTEGER, FOREIGN KEY references Employees)
- `manager_approval` (BOOLEAN)
- `order_date` (DATE, NOT NULL)
- `total_amount` (REAL, NOT NULL)

#### OrderDetails
- `order_detail_id` (INTEGER, PRIMARY KEY)
- `order_id` (INTEGER, FOREIGN KEY references Orders)
- `item_id` (INTEGER, FOREIGN KEY references Menu)
- `cook_id` (INTEGER, FOREIGN KEY references Employees)
- `quantity` (INTEGER, NOT NULL)

## Entity Relationships
- A **table** can have 0 to many **reservations**.
- A **reservation** is linked to one **table**.
- Employees (waiters, hosts, managers) handle **reservations**.
- A **reservation** can generate 0 to 1 **order**.
- An **order** can have 1 to many **order details**.
- A **menu item** can appear in multiple **order details**.
- A **cook** can prepare multiple **order details**.
- **Employees** are assigned **shifts**.

## Optimizations
To enhance performance:
- **Indexes**:
  - `check_table_number`: Speeds up table availability checks.
  - `check_reservation_datetime`: Optimizes reservation searches.
  - `filter_employee_role`: Improves role-based filtering.
  - `check_shift_date` & `check_order_date`: Enhances scheduling and sales reports.
- **Views**:
  - `AvailableTables`: Provides real-time available tables.
  - `DailySales`: Summarizes daily revenue.

## Limitations
- Assumes linear relationships (scalability concerns for large datasets).
- No flexible seating arrangements.
- No support for custom menu modifications.
- Employees cannot hold multiple roles in the same shift.

## How to Use
1. **Setup Database**:
   - Install **SQLite**.
   - Run the provided SQL script to initialize the database.
2. **Managing Tables**:
   - Add, update, and remove tables.
3. **Managing Employees**:
   - Insert employees with roles.
   - Assign employees to shifts.
4. **Handling Reservations**:
   - Create and modify reservations.
   - Assign tables and employees.
5. **Managing Orders**:
   - Add orders to reservations.
   - Track ordered items.
   - Generate total bills.
6. **Querying Reports**:
   - Use **views** for available tables and sales tracking.

## Future Enhancements
- Support for **multi-role employees**.
- Implement **flexible seating arrangements**.
- Add **menu customizations and special requests**.
- Extend **financial reporting and supplier inventory tracking**.

## Author
**Jeyashree Muthukumaran**



