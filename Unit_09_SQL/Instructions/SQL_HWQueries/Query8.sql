--Question 8:
select last_name, count(emp_no) as LastNameCount
from employees
group by last_name
order by LastNameCount desc;