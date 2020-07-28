from rest_framework import Serializers
from.models import register,authentication,deposit,withdraw

class registerSerializer(Serializers.ModelSerializer):
class meta:
	 model=register
         field='_all_'
class authenticationSerializer(Serializers.ModelSerializer):
class meta:
	 model=authentication
         field='_all_'
class depositSerializer(Serializers.ModelSerializer):
class meta:
	 model=deposit
         field='_all_' 
class withdrawSerializer(Serializers.ModelSerializer):
class meta:
	 model=withdraw
         field='_all_'        