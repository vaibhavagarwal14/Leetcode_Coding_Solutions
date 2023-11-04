# Write your MySQL query statement below
select name from Employee 
WHERE id in 
(select managerId from Employee Group BY managerID having Count(managerId)>=5);