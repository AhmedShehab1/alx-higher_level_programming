-- Script that lists all shows and all genres linked to that show from the hbtn_0d_tvshows db
SELECT tv_s.title, tv_s_g.genre_id
FROM tv_shows AS tv_s
LEFT JOIN tv_show_genres AS tv_s_g
ON tv_s_g.show_id = tv_s.id
WHERE tv_s_g.genre_id IS NULL
ORDER BY tv_s.title, tv_s_g.genre_id;
