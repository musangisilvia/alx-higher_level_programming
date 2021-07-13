-- list all cities in the database hbtn_0d_usa
-- record is in the form cities.id cities.name states.name

SELECT c.id, c.name, s.name
FROM cities c, states s
WHERE c.state_id = s.id
ORDER BY c.id;
