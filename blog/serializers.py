from rest_framework import serializers

from .models import Post
from django.contrib.auth import authenticate


class PostModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('author','title','text')



class AuthTokenSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(
		style={'input_type': 'password'},
		trim_whitespace = False

		)


	def validate(self, attrs):
		self.username = attrs.get('username')
		self.password = attrs.get('password')


		user = authenticate(
			request=self.context.get('request'),
			username=self.username,
			password=self.password
		)


		if not user:
			msg = 'Failure authentication'

			raise serializers.validationErro(msg, code='authentication')


		attrs['user'] = user
		return attrs