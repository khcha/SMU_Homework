--Question 1:
select e.emp_no, e.last_name, e.first_name, e.gender, s.salary 
from employees as e
left join salaries as s
on e.emp_no = s.emp_no
order by e.last_name asc;