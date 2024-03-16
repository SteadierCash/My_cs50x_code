SELECT DISTINCT name FROM stars
JOIN movies ON movies.id = stars.movie_id
JOIN people on people.id = stars.person_id
where year = 2004 ORDER BY birth;
