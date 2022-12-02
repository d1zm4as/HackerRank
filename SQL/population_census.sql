select sum(c.population) from city c join country C1 on c1.code = c.countrycode where continent = 'Asia'
