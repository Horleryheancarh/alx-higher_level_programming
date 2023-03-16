-- List shows and reviews
SELECT tv_shows.title, SUM(tv_show_rating.rate) AS rating FROM tv_shows
	-- Get ratings
	JOIN tv_show_ratings
		ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title ORDER BY rating DESC;
