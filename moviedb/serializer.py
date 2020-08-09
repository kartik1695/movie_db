from rest_framework import serializers
from moviedb.models import Movie, Genre

# class GenreSerializer(serializers.ModelSerializer):
       
#     class Meta:
#         model = Genre
#         fields = ['genre']

# class MovieSerializer(serializers.ModelSerializer):
#     genre = GenreSerializer(many=True, read_only=True)

    # class Meta:
    #     model = Movie
    #     fields = ['name', 'score', 'popularity' , 'director' , 'genre']
    
class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='genre'
     )
    
    class Meta:
        model = Movie
        fields = ['id','name', 'score', 'popularity' , 'director' , 'genre']
    
    # def update(self, instance, validated_data):
    #     genre_data = validated_data.pop('genre')
    #     genre = (instance.genre).all()
    #     genre = list(genre)
    #     print(genre)
    #     instance.name = validated_data.get(instance.get('name', instance.name))
    #     instance.popularity = validated_data.get(instance.get('99popularity', instance.name))
    #     instance.director = validated_data.get(instance.get('director', instance.name))
    #     instance.score = validated_data.get(instance.get('imdb_score', instance.name))   
    #     instance.save(genre)
    #     return instance