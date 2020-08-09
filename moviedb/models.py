from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=50)
    popularity = models.IntegerField(blank=False)
    director = models.CharField(max_length=30)
    score = models.FloatField(max_length=5)

    def __str__(self):
        return self.name

    def get_genre(self):
        genre = Genre.objects.filter(movie_name=self).values('genre')
        genre_list = [data['genre'] for data in genre]
        return genre_list

    def to_json(self):
        data = {
            'popularity': self.popularity,
            'name': self.name,
            'genre': self.get_genre(),
            'imdb_score': self.score,
            'director': self.director

        }
        return data

    # def save(self, genre ,*args, **kwargs):
    #     super(Movie, self).save(*args,**kwargs)
    #     if genre:
    #         for i in genre:
    #             Genre(movie_name=self, genre=i).save()
        


class Genre(models.Model):
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='genre')
    genre = models.CharField(max_length=30)

    def __str__(self):
        return self.genre
