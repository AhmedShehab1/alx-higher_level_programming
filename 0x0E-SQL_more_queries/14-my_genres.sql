-- Script all genres from hbtn_0d_tvshows db and displays number of shows linked to each
SELECT tv_g.name
FROM tv_genres AS tv_g
INNER JOIN tv_show_genres AS tv_s_g
ON tv_g.id = tv_s_g.genre_id
INNER JOIN tv_shows AS tv_s
ON tv_s.id = tv_s_g.show_id
WHERE tv_s.title = 'Dexter'
ORDER BY tv_g.name;
