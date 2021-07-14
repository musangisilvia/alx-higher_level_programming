-- lists all shows in the comedy genre
-- record shows tv_shows.title
-- sorted in ascending order by show title

SELECT title FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;
