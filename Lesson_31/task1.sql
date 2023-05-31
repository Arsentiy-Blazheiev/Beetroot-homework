--SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
--FROM employees
--JOIN department ON employees.department_id = department.department_id;

--SELECT employees.first_name, employees.last_name, department.department_name, locations.city, locations.state_province
--FROM employees
--JOIN department ON employees.department_id = department.department_id
--JOIN locations ON department.location_id = locations.location_id;

--SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
--FROM employees
--JOIN department ON employees.department_id = department.department_id
--WHERE employees.department_id IN (40, 80);

--SELECT department.department_name, COUNT(employees.employee_id) AS employee_count
--FROM department
--LEFT JOIN employees ON department.department_id = employees.department_id
--GROUP BY department.department_id;

--SELECT employees.first_name || ' ' || employees.last_name AS employee_name, managers.first_name || ' ' || managers.last_name AS manager_name
--FROM employees
--LEFT JOIN employees managers ON employees.manager_id = managers.employee_id;

--SELECT jobs.job_title, employees.first_name || ' ' || employees.last_name AS employee_name, (jobs.max_salary - employees.salary) AS salary_difference
--FROM employees
--JOIN jobs ON employees.job_id = jobs.job_id;

--SELECT jobs.job_title, AVG(employees.salary) AS average_salary
--FROM employees
--JOIN jobs ON employees.job_id = jobs.job_id
--GROUP BY jobs.job_id;

--SELECT employees.first_name || ' ' || employees.last_name AS employee_name, employees.salary
--FROM employees
--JOIN department ON employees.department_id = department.department_id
--WHERE department.location_id IN (
  --SELECT location_id
  --FROM locations
  --WHERE city = 'London');
  
--SELECT department.department_name, COUNT(employees.employee_id) AS employee_count
--FROM department
--LEFT JOIN employees ON department.department_id = employees.department_id
--GROUP BY department.department_name;