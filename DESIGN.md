# Design Document

By Jeyashree Muthukumaran

Video overview: <URL HERE>

## Scope
The database for Restaurant Management System includes all the entities neccessary to manage and track reservations and orders.The scope of the database covers
* Tables: Information about the dining tables.
* Employees: Basic identifying details about the restaurant staff.
* Shifts: Details of the employee work schedule.
* Reservations: Information about customer reservations at the restaurant.
* Menu: Details about menu items.
* Orders: Records of customer orders.

Out of scope elements include detailed financial reports,supplier inventories and customer loyalty programs.

## Functional Requirements

This database will support:

* Manage Tables: Add, update, and remove tables, as well as view their capacity and location.
* Employee Management: Add, update, and remove employee details, including assigning roles and managing shifts.
* Handle Reservations: Create, update, cancel, or confirm reservations, including assigning tables and staff to reservations.
* Order Management: Create and update orders, track items ordered, and calculate total amounts.
* Menu Management: Add, update, or remove menu items, modify pricing, and set availability.
* Shift Scheduling: Assign employees to shifts, with manager oversight where needed.
* Real-Time Table Availability: Check table availability for a specific date and time to assist with reservations.
* Sales and Performance Tracking: Generate reports on total sales, individual order details, and employee schedules.

This database does not cover detailed financial reports,supplier inventories and customer loyalty programs currently.

## Representation

Entities are captured in SQLite tables with the following schema.

### Entities

The entities represented in the database are:

1. ### Tables
   - **Attributes**: 
     - `table_id`: `INTEGER` (unique identifier, `PRIMARY KEY`)
     - `table_number`: `INTEGER`.
     - `capacity`: `INTEGER`.
     - `location`: `TEXT`.

   - **Constraints**:
     - `PRIMARY KEY` on `table_id` ensures uniqueness for table identification.
     - `UNIQUE` on `table_number` ensures no duplication of table numbers.
     - `NOT NULL` on all columns ensures that no table record is incomplete.

2.  ### Employees
   - **Attributes**: 
     - `employee_id`: `INTEGER` (unique identifier, `PRIMARY KEY`).
     - `name`: `TEXT` .
     - `role`: `TEXT`.
     - `phone_number`: `TEXT`.
     - `email`: `TEXT`.
     - `hire_date`: `DATE`.

   - **Constraints**:
     - `PRIMARY KEY` on `employee_id` ensures uniqueness for each employee.
     - `CHECK` on `role` ensures that only valid roles like 'Manager', 'Chef', 'Waiter', 'Host' can be used.
     - `NOT NULL` on essential columns (`name`, `role`, `hire_date`) ensures that these fields cannot be left blank.

3.  ### Shifts
   - **Attributes**: 
     - `shift_id`: `INTEGER` (unique identifier, `PRIMARY KEY`).
     - `employee_id`: `INTEGER`.
     - `shift_date`: `DATE`.
     - `start_time`: `TIME`. 
     - `end_time`: `TIME`.
     - `manager_id`: `INTEGER`.

   - **Constraints**:
     - `PRIMARY KEY` on `shift_id` ensures each shift is unique.
     - `FOREIGN KEY` on `employee_id` and `manager_id` ensures relational integrity with `Employees`.
     - `NOT NULL` on all attributes ensures no essential data (employee, manager, shift times) is missing.

4. ### Reservations
   - **Attributes**: 
     - `reservation_id`: `INTEGER` (unique identifier, `PRIMARY KEY`).
     - `customer_name`: `TEXT`.
     - `phone_number`: `TEXT`.
     - `table_id`: `INTEGER`. 
     - `waiter_id`: `INTEGER`. 
     - `host_id`: `INTEGER`. 
     - `manager_id`: `INTEGER`.
     - `reservation_date`: `DATE`. 
     - `reservation_time`: `TIME`. 
     - `status`: `TEXT`.

   - **Constraints**:
     - `PRIMARY KEY` on `reservation_id` ensures each reservation is uniquely identifiable.
     - `FOREIGN KEY` on `table_id`, `waiter_id`, `host_id`, and `manager_id` ensures data integrity between related tables.
     - `CHECK` on `status` to ensure the reservation status can only be 'Pending', 'Confirmed', or 'Cancelled'.
     - `NOT NULL` on most fields to ensure complete reservation records.

5. ### Menu
   - **Attributes**: 
     - `item_id`: `INTEGER` (unique identifier, `PRIMARY KEY`).
     - `item_name`: `TEXT`. 
     - `category`: `TEXT`.
     - `price`: `REAL`. 
     - `availability`: `BOOLEAN`.

   - **Constraints**:
     - `PRIMARY KEY` on `item_id` ensures each menu item is uniquely identifiable.
     - `NOT NULL` on all attributes except `availability` ensures that the essential information about the menu item is always present.

6. ### Orders
   - **Attributes**: 
     - `order_id`: `INTEGER` (unique identifier, `PRIMARY KEY`).
     - `reservation_id`: `INTEGER`.
     - `waiter_id`: `INTEGER`.
     - `manager_approval`: `BOOLEAN`.
     - `order_date`: `DATE`.
     - `total_amount`: `REAL`.

   - **Constraints**:
     - `PRIMARY KEY` on `order_id` ensures each order is uniquely identifiable.
     - `FOREIGN KEY` on `reservation_id` and `waiter_id` ensures relational integrity with `Reservations` and `Employees`.
     - `NOT NULL` on essential fields like `reservation_id`, `order_date`, and `total_amount` ensures the completeness of the order record.

7.  ### OrderDetails
   - **Attributes**: 
     - `order_detail_id`: `INTEGER` (unique identifier, `PRIMARY KEY`).
     - `order_id`: `INTEGER`.
     - `item_id`: `INTEGER`.
     - `cook_id`: `INTEGER`.
     - `quantity`: `INTEGER`.

   - **Constraints**:
     - `PRIMARY KEY` on `order_detail_id` ensures each order detail is uniquely identifiable.
     - `FOREIGN KEY` on `order_id`, `item_id`, and `cook_id` ensures relational integrity with `Orders`, `Menu`, and `Employees`.
     - `NOT NULL` on all fields to ensure complete order details.

### Relationships

The below entity relationship diagram describes the relationships among the entities in the database.

![ER Diagram](ER_diagram.png)

As Detailed by the diagram:

1. **Tables and Reservations**  
   - A **table** can have **0 to many reservations**.  
   - A **reservation** is linked to **one table**.

2. **Employees and Reservations**  
   - Employees (as **waiters**, **hosts**, or **managers**) can handle **0 to many reservations**.  
   - A **reservation** is linked to **one waiter, host, and manager** (optional).

3. **Employees and Shifts**  
   - An **employee** can have **0 to many shifts**.  
   - A **shift** is assigned to **one employee** and optionally managed by a **manager**.

4. **Reservations and Orders**  
   - A **reservation** can generate **0 to 1 order**.  
   - An **order** is linked to **one reservation**.

5. **Orders and OrderDetails**  
   - An **order** can have **1 to many order details**.  
   - An **order detail** belongs to **one order**.

6. **Menu and OrderDetails**  
   - A **menu item** can appear in **0 to many order details**.  
   - An **order detail** references **one menu item**.

7. **Employees and OrderDetails**  
   - A **cook** can prepare **0 to many order details**.  
   - An **order detail** is optionally prepared by **one cook**.

## Optimizations

* Indexes were created to optimize common queries. For instance, `check_table_number` speeds up table availability checks, while `check_reservation_datetime` ensures efficient searches for reservations by date and time. Employee role filtering is enhanced by `filter_employee_role`, and both shift scheduling and daily sales reporting are supported by `check_shift_date` and `check_order_date`. 

* Views like `AvailableTable`s provide a real-time snapshot of available tables, and `DailySales` offers quick financial summaries.

## Limitations

* The design assumes linear relationships and may not scale well with large datasets. 
* It cannot handle flexible seating or overlapping shifts effectively.
* Menu customizations and special requests are unsupported. 
* Multi-role employees may challenge the current schema.
