-- scripts that lists all shows in the db hbtn_0d_tvshows

SELECT tv.title, tv_g.genre_id
FROM tv_shows AS tv
INNER JOIN tv_show_genres AS tv_g
ON tv_g.show_id = tv.id
WHERE tv_g.genre_id >= 1
ORDER BY tv.title, tv_g.genre_id;
