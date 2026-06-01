-- List all TV shows with at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

INSERT INTO tv_genres VALUES (1,'Drama'),
(2,'Mystery'),(3,'Adventure'),
(4,'Fantasy'),(5,'Comedy'),(6,'Crime'),
(7,'Suspense'),(8,'Thriller');

-- import database dump from hbtn_0d_tvshows to MySQL server
DROP TABLE IF EXISTS "tv_genres";
CREATE TABLE tv_genres (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(256) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;