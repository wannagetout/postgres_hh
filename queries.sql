create table employees(employee_id INT primary key, name varchar(80));
create table vacancies(vacancy_id INT primary key, name varchar(150), salary int, description text, employee_id int REFERENCES employees(employee_id));
