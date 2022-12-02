SELECT DISTINCT salary*months,
    (SELECT COUNT(salary*months) FROM Employee
    WHERE e.salary*months=salary*months)
FROM Employee e
ORDER BY salary*months DESC
LIMIT 1
