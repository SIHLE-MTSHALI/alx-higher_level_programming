-- 101-not_a_comedy.sql
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_shows.title
HAVING COUNT(CASE WHEN tv_genres.name = 'Comedy' THEN 1 END) = 0
ORDER BY tv_shows.title ASC;

