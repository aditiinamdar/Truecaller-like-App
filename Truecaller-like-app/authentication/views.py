
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer,ContactSerializer, NamesearchcontactsSerializer,NamesearchuserSerializer,SpamSerializer, AddContactSerializer
from django.db.models import Q
from django.contrib.auth import get_user_model,authenticate
from rest_framework.views import APIView
from authentication import models
User = get_user_model()
from .models import Contact, CustomUser, Spam
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import api_view


from django.db.models import Q,F

class AddContactViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = AddContactSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def get_contacts_name(request):
        authentication_classes = [JWTAuthentication]
        permission_classes = [permissions.IsAuthenticated]
        names = request.query_params.get('name','')
        users = User.objects.filter(name=names)
        if users:
            users = User.objects.filter(Q(name__icontains=names))
            serializer = NamesearchuserSerializer(users,many=True)
            return Response(serializer.data)
        else:
            if names:
                obj = Contact.objects.filter(
                Q(contact_name__istartswith=names) | Q(contact_name__icontains=names)
                )
                serializer = NamesearchcontactsSerializer(obj,many=True)
                return Response(serializer.data)
            else:
                return Response("not found")
            
@api_view(['GET'])
def get_contacts_phone(request):
        phone = request.query_params.get('phone','')
        users = User.objects.filter(Q(phone_number__icontains=phone))
        if users:
            users = User.objects.filter(Q(phone_number__icontains=phone))
            serializer = UserSerializer(users,many=True)
            return Response(serializer.data)
        else:
            if users:
                obj = Contact.objects.filter(Q(contact_phone_number__icontains=phone))
                
                serializer = NamesearchcontactsSerializer(obj,many=True)
                return Response(serializer.data)
            else:
                return Response("not found")

class SpamViewSet(viewsets.ModelViewSet):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer

    @action(detail=False, methods=['post'])
    def mark_number_as_spam(self, request):
        number_to_mark = request.data.get('number', None)
        if not number_to_mark:
            return Response({"error": "Number is required for marking as spam."}, status=400)
        try:
            phone_number = Spam.objects.get(phone_number=number_to_mark)
            phone_number.spam_likelihood = 1
            phone_number.save()
        except Spam.DoesNotExist:
            Spam.objects.create(phone_number=number_to_mark, spam_likelihood=1)
        User.objects.filter(phone_number=number_to_mark).update(spam_likelihood=F('spam_likelihood') + 1)
        Contact.objects.filter(contact_phone_number=number_to_mark).update(spam_likelihood=F('spam_likelihood') + 1)
        return Response({"message": f"Number {number_to_mark} marked as spam."}, status=201)

    


   

   
    
    

   

    

    