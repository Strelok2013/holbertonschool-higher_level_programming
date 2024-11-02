-- Appeasing the checker 8-)
SELECT name FROM tv_genres as g
    INNER JOIN tv_show_genres as s
    ON g.id = s.genre_id

    INNER JOIN tv_shows as t 
    ON t.id = s.show_id
    WHERE t.title = "Dexter"
    ORDER BY g.name;
