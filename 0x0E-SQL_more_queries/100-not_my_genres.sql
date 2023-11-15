-- List genres not linked to Dexter
SELECT name FROM genres WHERE id NOT IN (SELECT genre_id FROM tv_show_genres JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE title = 'Dexter') ORDER BY name;
