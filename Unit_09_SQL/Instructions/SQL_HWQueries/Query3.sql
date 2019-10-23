--Question 3:
select e.emp_no, e.last_name, e.first_name, dm.dept_no, d.dept_name, dm.from_date, dm.to_date
from employees e
join dept_manager dm
	on e.emp_no = dm.emp_no
join departments d
	on dm.dept_no= d.dept_no
order by e.last_name asc;