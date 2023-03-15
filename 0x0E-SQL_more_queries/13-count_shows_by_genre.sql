-- Count number of shows by genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
-- Join tables
FROM tv_show_genres JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
-- Group
GROUP BY tv_show_genres.genre_id
-- Sort by number of shows
ORDER BY number_of_shows DESC, tv_genres.id ASC;
