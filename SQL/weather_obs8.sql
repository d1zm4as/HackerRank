SELECT DISTINCT CITY FROM STATION

WHERE RIGHT(CITY, 1) IN ('a','e','i','o','u') and LEFT(CITY,1) IN ('a','e','i','o','u')
