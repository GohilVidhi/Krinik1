from django.shortcuts import render
from .serializers import*
from .models import*
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


def index(request):
    return render(request,"index.html")



# Create your views here.

#------------------League View---------------------

class League_view(APIView):
    def get(self,request,id=None):  
        if id:
        
            try:
                uid=League.objects.get(id=id)
                serializer=League_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        else:
            uid=League.objects.all()
            serializer=League_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})
      
    def post(self,request):
        serializer=League_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
     
    def patch(self,request,id=None):
        try:
            uid=League.objects.get(id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=League_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
        
        
        
              
    def delete(self,request,id=None):
        if id:
            try:
                uid=League.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        else:
            return Response({'status':"invalid data"})



#---------------Team View----------------------



class Team_view(APIView):
    def get(self,request,id=None):  
        if id:
        
            try:
                uid=Team.objects.get(id=id)
                serializer=Team_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        else:
            uid=Team.objects.all()
            serializer=Team_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})
      
    def post(self,request):
        serializer=Team_serializers(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
     
    def patch(self,request,id=None):
        try:
            uid=Team.objects.get(id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=Team_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
        
        
        
              
    def delete(self,request,id=None):
        if id:
            try:
                uid=Team.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        else:
            return Response({'status':"invalid data"})



#---------------Player View----------------------

class Player_view(APIView):
    def get(self,request,id=None):  
        if id:
        
            try:
                uid=Player.objects.get(id=id)
                serializer=Player_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        else:
            uid=Player.objects.all()
            serializer=Player_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})
      
    def post(self,request):
        serializer=Player_serializers(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
     
    def patch(self,request,id=None):
        try:
            uid=Player.objects.get(id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=Player_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data"})
        
        
        
        
              
    def delete(self,request,id=None):
        if id:
            try:
                uid=Player.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        else:
            return Response({'status':"invalid data"})
