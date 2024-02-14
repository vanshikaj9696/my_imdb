from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200)
    length = models.PositiveIntegerField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    genre = models.ForeignKey(Genre, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.year:
            return f"{self.title} ({self.year})"
        return self.title
    
    def get_fields(self):
        fields_list = []
        for field in self.__class__._meta.fields[1:]:
            label = field.verbose_name
            value = field.value_from_object(self)

            
            if label == 'genre':
                if value is not None:
                    genre_obj = Genre.objects.get(pk=value)
                    value = genre_obj.name
                else:
                    value = 'No Genre'

            fields_list.append((label, value))

        return fields_list

