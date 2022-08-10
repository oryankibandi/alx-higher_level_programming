-- Lists show contained in hbtn_0d_tvshows

SELECT shows.title, genres.genre_id  FROM tv_shows AS shows
INNER JOIN tv_show_genres AS genres ON shows.id = genres.show_id
ORDER BY shows.title, genres.genre_id;
