-- list all genres from hbtn_0d_tvshows and display number of shows linked to each
-- record is in the form <tv show genre> - <number of shows linked to it>
-- sorted in desc order of number of shows linked

SELECT tv_g.name AS genre, COUNT(show_id) AS number_of_shows FROM tv_genres tv_g
INNER JOIN tv_show_genres tvs_g
ON tv_g.id = tvs_g.genre_id
GROUP BY tvs_g.genre_id
ORDER BY number_of_shows DESC;

