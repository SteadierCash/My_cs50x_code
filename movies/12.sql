SELECT title FROM movies WHERE id in
(
    SELECT movie_id FROM stars
    JOIN people ON people.id = stars.person_id
    WHERE people.name = "Bradley Cooper"
)
AND id IN
(
    SELECT movie_id FROM stars
    JOIN people ON people.id = stars.person_id
    WHERE people.name = "Jennifer Lawrence"
)
