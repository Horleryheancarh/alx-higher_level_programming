-- List TV shows by title and genre
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
-- Query to join tv_shows and tv_shows_genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- condition
WHERE tv_show_genres.genre_id is NULL
-- Order by title and genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
