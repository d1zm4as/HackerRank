SELECT 
    CASE
        WHEN A=B AND B=C THEN 'Equilateral'
        WHEN (A=B OR B=C OR C=A) AND A+B > C  THEN 'Isosceles'
        WHEN A+B > C THEN 'Scalene'
        ELSE 'Not A Triangle'
    END AS 'TRIANGLE'
FROM TRIANGLES
