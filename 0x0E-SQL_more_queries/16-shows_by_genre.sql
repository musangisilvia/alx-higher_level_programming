-- lists all shows and all genres linked to it from hbtn_0d_tvshows
-- if the show doesn't have a genre display NULL.
-- result is sorted in ascending order by show title and genre name
-- record is in the form tv_show.title - tv_genres.name

SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
LEFT OUTER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
