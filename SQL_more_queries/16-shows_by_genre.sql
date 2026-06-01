--Lists all shows and all the genres linked to that show
SELECT tv_shows.title AS show, tv_genres.name AS genre
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id;