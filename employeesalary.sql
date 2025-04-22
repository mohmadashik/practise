-- Write an SQL query to find the top three departments with the highest average salary.
-- Include the department name and the average salary in the result.
-- Employees
-- ---------
-- id (integer)
-- name (text)
-- department (text)
-- salary (numeric)

select name, avg(salary) from Employees 
group by department 
order by avg(salary) desc limit 3;

