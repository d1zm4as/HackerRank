SELECT DISTINCT CITY FROM STATION

WHERE LEFT(CITY, 1) NOT IN ('a','e','i','o','u','A','E','I','O','U') and RIGHT(CITY,1) NOT IN ('a','e','i','o','u','A','E','I','O','U');
