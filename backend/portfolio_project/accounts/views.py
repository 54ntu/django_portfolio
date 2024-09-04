from django.shortcuts import render,HttpResponse
from rest_framework import viewsets,status
from django.contrib.auth import get_user_model,authenticate
from accounts.serializers import UserLoginSerializers,RegisterUserSerializer
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

User = get_user_model()

# Create your views here.

class UserViewsets(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    @action(detail =False, methods=['POST'])
    def login(self,request):
        serializer= UserLoginSerializers(data= request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username = serializer.validated_data['email'],
            password = serializer.validated_data['password']

        )

        if user is not None:
            token,_ = Token.objects.get_or_create(user=user)
            return Response({
                'token':token.key,
                'user':serializer.data,
                'message':'user logged in successfully...!!!!!'
            },
            status=status.HTTP_200_OK)
        
        else:
            return Response({
                'errors':"email or password doesnot matched..!!"
            },
            status=status.HTTP_401_UNAUTHORIZED)
        