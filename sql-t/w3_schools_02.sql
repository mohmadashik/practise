--  Intermediate Level Questions


-- Find all orders shipped by 'Speedy Express'.


select od.OrderId, p.ProductName, od.Quantity, o.ShipperId, s.ShipperName
from order_details od join products p on p.ProductId = od.ProductId join orders o on o.OrderId=od.OrderId join shippers s on s.ShipperId= o.ShipperId
where s.ShipperName = 'Speedy Express';

-- Which employee handled the most orders?
select e.FirstName , count(o.OrderId) as no_of_orders
from employees e join orders o on e.EmployeeId = o.EmployeeId
group by e.EmployeeId
order by no_of_orders desc
limit 1;

-- copilot don't recommend anything. i'm preparing in this file for my interview
-- Get a list of products that are out of stock.

select ProductName
from products 
where Unit = 0;


-- Find products that were never ordered.
select p.ProductName, o.OrderId
from products p left join order_details o on p.ProductId= o.ProductId
where o.OrderId is Null;

SELECT ProductName
FROM products
WHERE ProductID NOT IN (SELECT DISTINCT ProductID
FROM order_details);


-- how will you update all females to male and male to female in a single query?

CREATE TABLE Users
(
    UserID INT PRIMARY KEY,
    UserName VARCHAR(50),
    Gender VARCHAR(10)
);

INSERT INTO Users
    (UserID, UserName, Gender)
VALUES
    (1, 'John Doe', 'Male'),
    (2, 'Jane Smith', 'Female'),
    (3, 'Bob Johnson', 'Male'),
    (4, 'Emily Davis', 'Female'),
    (5, 'Chris Brown', 'Male');

UPDATE Users
SET Gender = CASE
    WHEN Gender = 'Male' THEN 'Female'
    WHEN Gender = 'Female' THEN 'Male'
    ELSE Gender
END;

select *
from users
order by id desc;


