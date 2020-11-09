from django.shortcuts import render
from rest_framework import viewsets ,permissions, status
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from rest_framework.response import Response

class ListNote(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    #一覧取得
    def list(self,request):
        data = NoteSerializer(Note.objects.all().select_related('user').order_by('created_at').reverse(), many=True).data

        return Response(status=200 , data=data)

    #詳細の取得
    def retrieve(self,request,pk=None):
        note_id = pk
        data = NoteSerializer(Note.objects.filter(uuid=note_id), many=True).data

    def create(self, request):
        note = Note.objects.create(
            title=request.data['title'],
            body=request.data['body'],
            sanmi = request.data['sanmi'],
            nigami = request.data['nigami'],
            like = request.data['like'],
            user=request.user)
        serializer = NoteSerializer(note, many=False)
        response = {'message': 'Article created' , 'result': serializer.data}
        return Response(response, status=200)

class UserList(viewsets.ModelViewSet):

    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)