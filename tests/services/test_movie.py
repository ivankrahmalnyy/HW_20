import pytest
from service.movie import MovieService


class TestMovieService:
	@pytest.fixture(autouse=True)
	def movie_service(self, movie_dao):
		self.movie_service = MovieService(dao=movie_dao)

	def test_get_one(self):
		movie = self.movie_service.get_one(1)
		assert movie is not None
		assert movie.id is not None

	def test_get_all(self):
		movies = self.movie_service.get_all()
		assert len(movies) == 2

	def test_create(self):
		movie_d = {
			"title": "Game",
			"description": "pass",
			"trailer": "long video",
			"year": 2014,
			"rating": 5.2,
			"genre_id": 2,
			"director_id": 1
		}
		movie = self.movie_service.create(movie_d)
		assert movie.id is not None
		assert movie is not None

	def test_delete(self):
		self.movie_service.delete(1)

	def test_update(self):
		movie_d = {
			"title": "Holiday",
			"description": "pass",
			"trailer": "long video",
			"year": 2013,
			"rating": 6.0,
			"genre_id": 2,
			"director_id": 1
		}
		movie = self.movie_service.update(movie_d)

		assert movie is not None
		assert movie.title is not None