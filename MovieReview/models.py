from django.db import models

class MovieInfo(models.Model):
    movie_name= models.CharField(max_length=200)
    movie_review= models.CharField(max_length=3)
    movie_release_date= models.CharField(max_length=50)
    movie_genre= models.CharField(max_length=50)
    movie_desc= models.TextField(max_length=500)

    def __str__(self):
        return self.movie_name

class MovieInfo_Test(models.Model):
    movie_test= models.CharField(max_length=200)

    def __str__(self):
        return self.movie_test