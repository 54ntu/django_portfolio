from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length= 100,write_only=True)
    class Meta:
         model = User
         fields = ['email','password']

    def validate_email(self,value):
        if User.objects.filter(email= value).exists():
            raise serializers.ValidationError("email already exists go with login....!!!!")
        return value
    

    def create(self,validate_data,*args,**kwargs):
        user = User.objects.create_user(
            email= validate_data['email'],
            password= validate_data['password']
        )
        return user
    


class UserLoginSerializers(serializers.Serializer):
        email =serializers.EmailField()
        password = serializers.CharField(write_only = True)