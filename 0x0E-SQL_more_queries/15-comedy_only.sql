-- Lists all Comedy shows in the database hbtn_0d_tvshows

SELECT tv_shows.title FROM tv_shows AS tv_shows
INNER JOIN tv_show_genres AS shows ON tv_shows.id = shows.show_id

INNER JOIN tv_genres AS genres ON genres.id = shows.genre_id
WHERE genres.name = "Comedy" ORDER BY tv_shows.title;
