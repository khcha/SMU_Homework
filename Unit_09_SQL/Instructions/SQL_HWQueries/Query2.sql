--Question 2:
select emp_no, first_name, last_name, gender, hire_date
from employees
where extract(year from hire_date)=1986
order by last_name asc;