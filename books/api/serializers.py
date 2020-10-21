from rest_framework import serializers
from books import models

class BooksSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Books
		fields = '__all__'
		#fields = ['id_book','pages','image']