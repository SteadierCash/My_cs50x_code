SELECT name FROM people WHERE id in
(SELECT DISTINCT person_id FROM stars WHERE movie_id in
(SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people where name = "Kevin Bacon" and birth = 1958))) AND name != "Kevin Bacon"
