-- scripts that lists all shows in the db hbtn_0d_tvshows

SELECT tv.title, tv_g_s.genre_id
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tv_g_s
ON tv_g_s.show_id = tv.id
ORDER BY tv.title, tv_g_s.genre_id;
