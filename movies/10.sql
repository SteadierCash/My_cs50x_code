SELECT DISTINCT name FROM directors
JOIN movies ON movies.id = directors.movie_id
JOIN people ON people.id = directors.person_id
JOIN ratings ON ratings.movie_id = movies.id
WHERE rating >= 9.0;

