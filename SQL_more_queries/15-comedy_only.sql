-- List of all comdey shows 
SELECT tv_shows.title AS comedy_show
FROM tv_shows
INNER JOIN tv_genres
ON tv_shows.id = tv_genres.id
WHERE tv_genres.name = 'Comedy';