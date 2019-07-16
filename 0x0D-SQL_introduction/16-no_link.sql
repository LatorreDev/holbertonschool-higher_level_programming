-- Count repeated scores
SELECT `score`, COUNT(`id`) AS number FROM `second_table` WHERE name IS NOT NULL GROUP BY `score` ORDER BY score DESC;
