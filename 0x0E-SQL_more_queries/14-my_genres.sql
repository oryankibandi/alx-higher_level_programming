-- lists all genres of the show Dexter

SELECT genres.name FROM tv_genres AS genres
INNER JOIN tv_show_genres AS shows ON genres.id = shows.genre_id

INNER JOIN tv_shows AS tv_shows ON tv_shows.id = shows.show_id
WHERE tv_shows.title = "Dexter" ORDER BY genres.name;
