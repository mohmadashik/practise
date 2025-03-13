-- table name : emp.
-- columns: emp_id, emp_name, salary, dept_id, manager_id
-- dept_id, manager_id are not foreign keys, they are just columns in same table
 
-- Get highest salary
-- Get second highest Salary
-- Get highest salary of departments available
-- Print emp_name when the number of employees in the department is equal to 3
-- Print emp_name and manager_name for emp_id = 2
-- Print emp_name that start with b (case insensitive)

select id,name,salary from employee order by salary desc limit 1 ;


select id,name,salary from employee order by salary desc limit 1 offset 2;

select name from employee group by dept_id having count(dept_id) = 3

select e.emp_name, m.emp_name from employee e join employee m on e.emp_id = m.emp_id where e.manager_id = 2;

select emp_name from employee where substring(emp_name,0,2) = 'b';

