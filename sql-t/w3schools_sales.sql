-- 1. Retrieve Customers with Their Orders
-- Get the CustomerID, CustomerName, OrderID, and OrderDate of all customers who have placed an order.
-- Include customers who haven’t placed an order as well.


select c.CustomerID, c.CustomerName,o.OrderID,o.OrderDate from customers c left join orders o on c.CustomerID = o.CustomerID order by c.CustomerID;

-- 2. Find Employees and Their Orders
-- Get the EmployeeID, FirstName, LastName, OrderID, and OrderDate of employees who have handled orders.
-- Modify the query to also include employees who have not handled any orders.



-- 3. Find Products That Have Never Been Ordered
-- Get the ProductID, ProductName of products that haven't been ordered.
-- Modify the query to include category names from the Categories table.

 select p.ProductID,p.ProductName,o.OrderID from products p left join order_details o on o.ProductID = p.ProductID group by p.productID having o.OrderID is Null;
-- difference between orderid is null vs orderid = null


-- 4. Retrieve Orders with Customer and Employee Details
-- Get the OrderID, OrderDate, CustomerName, EmployeeName for all orders.
-- Modify the query to only show orders placed in the year 1997.


-- 5. Find the Total Revenue Per Customer
-- Get the CustomerID, CustomerName, and TotalAmountSpent (sum of Quantity * UnitPrice for each customer).
-- Modify the query to only include customers who have spent more than $5000.
-- 6. Get the Top 5 Best-Selling Products
-- Find the ProductID, ProductName, TotalQuantitySold for the top 5 best-selling products (based on SUM(Quantity)).
-- 7. Find the Customers Who Placed the Most Orders
-- Get the CustomerID, CustomerName, TotalOrdersPlaced, sorted in descending order.
-- Limit the result to the top 10 customers.
-- 8. Find the Employees Who Processed the Most Orders
-- Get the EmployeeID, EmployeeName, TotalOrdersProcessed.
-- Modify the query to show only employees who processed more than 50 orders.
-- 9. Retrieve All Orders with Product Details
-- Get the OrderID, CustomerName, ProductName, Quantity, TotalPrice (Quantity * UnitPrice) for each order.
-- 10. Find the Customers Who Have Ordered All Products from a Specific Category
-- Get the CustomerID, CustomerName of customers who have ordered every product from a particular category.