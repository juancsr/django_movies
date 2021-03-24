-- Country
INSERT INTO public.movies_country("name") VALUES('Colombia');
INSERT INTO public.movies_country("name") VALUES('México');
INSERT INTO public.movies_country("name") VALUES('Chile');

SELECT * FROM public.movies_country;

-- Movies
INSERT INTO public.movies_movie(title, country_id)
VALUES('Terminator dark fate', 1);
INSERT INTO public.movies_movie(title, country_id)
VALUES('Terminar 1', 1);
INSERT INTO public.movies_movie(title, country_id)
VALUES('Terminator 2', 1);
INSERT INTO public.movies_movie(title, country_id)
VALUES('La Katarina', 2);
INSERT INTO public.movies_movie(title, country_id)
VALUES('El manicomio', 3);

SELECT * FROM public.movies_movie;

-- Scores
-- Terminator dark fate
INSERT INTO public.movies_score(value, movie_id)
VALUES(1, 1);
INSERT INTO public.movies_score(value, movie_id)
VALUES(3, 1);
INSERT INTO public.movies_score(value, movie_id)
VALUES(4, 1);
INSERT INTO public.movies_score(value, movie_id)
VALUES(5, 1);
INSERT INTO public.movies_score(value, movie_id)
VALUES(2, 1);
-- Terminator 1
INSERT INTO public.movies_score(value, movie_id)
VALUES(4, 2);
INSERT INTO public.movies_score(value, movie_id)
VALUES(5, 2);
INSERT INTO public.movies_score(value, movie_id)
VALUES(4, 2);
-- Terminator 2
INSERT INTO public.movies_score(value, movie_id)
VALUES(5, 3);
INSERT INTO public.movies_score(value, movie_id)
VALUES(5, 3);
INSERT INTO public.movies_score(value, movie_id)
VALUES(5, 3);
-- La katarina
INSERT INTO public.movies_score(value, movie_id)
VALUES(2, 4);
INSERT INTO public.movies_score(value, movie_id)
VALUES(5, 4);
INSERT INTO public.movies_score(value, movie_id)
VALUES(3, 4);
-- El manicomio
INSERT INTO public.movies_score(value, movie_id)
VALUES(4, 5);
INSERT INTO public.movies_score(value, movie_id)
VALUES(4, 5);
INSERT INTO public.movies_score(value, movie_id)
VALUES(4, 5);

SELECT * FROM public.movies_score;