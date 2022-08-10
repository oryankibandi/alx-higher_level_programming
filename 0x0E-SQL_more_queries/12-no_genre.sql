-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT shows.title, genres.genre_id FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS genres ON shows.id = genres.show_id
WHERE genres.genre_id IS NULL ORDER BY shows.title, genres.genre_id;
