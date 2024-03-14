-- 15-comedy_only.sql
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id IN (
    SELECT show_id
    FROM tv_show_genres
    WHERE genre_id = (
        SELECT id 
        FROM tv_genres 
        WHERE name = 'Comedy'
    )
)
ORDER BY tv_shows.title ASC;

