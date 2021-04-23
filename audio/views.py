from django.shortcuts import render
from .models import Song, Podcast, Audiobook
from rest_framework.serializers import ValidationError
from .serializers import SongSerializer, PodcastSerializer, AudiobookSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

audio_type_serializer = {'song': SongSerializer, 'podcast': PodcastSerializer, 'audiobook': AudiobookSerializer}

audio_type_model = {'song': Song, 'podcast': Podcast, 'audiobook': Audiobook}


@api_view(["POST"])
@csrf_exempt
def create(request):
    data = request.data
    audio_type = data.get("audioFileType", None)

    if audio_type not in ['song','podcast','audiobook']:
        return Response("audioFileType must be one of the 3 audio types(song, podcast, audiobook)", 
            status=status.HTTP_400_BAD_REQUEST)
    
    metadata = data.get('audioFileMetadata')
    if audio_type == 'podcast':
        participent = metadata.get("participents", None)
        if (participent is None or len(participent) > 10 or 
            any(i for i in participent if len(i) > 100)):
            return Response({"invalid":"list of strings, each string cannot be larger than 100 characters, maximum of 10 participants possible"}, 
            status=status.HTTP_400_BAD_REQUEST)
    audio_serializer = audio_type_serializer.get(audio_type)
    serializer = audio_serializer(data=metadata)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get(request,audioFileType,audioFileID=None):
    if audioFileID:
        try:
            model = audio_type_model.get(audioFileType)
            data = model.objects.get(id=audioFileID)
            audio_serializer = audio_type_serializer.get(audioFileType)
            serializer = audio_serializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    else:
        model = audio_type_model.get(audioFileType)
        data = model.objects.all()
        audio_serializer = audio_type_serializer.get(audioFileType)
        serializer = audio_serializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
@api_view(["DELETE"])
def delete(request,audioFileType,audioFileID):
    if audioFileID:
        try:
            model = audio_type_model.get(audioFileType)
            data = model.objects.get(id=audioFileID)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["PUT"])
def update(request,audioFileType,audioFileID):
    if audioFileID:
        try:
            data = request.data
            audio_type = data.get("audioFileType", None)

            if audio_type not in ['song','podcast','audiobook']:
                return Response("audioFileType must be one of the 3 audio types(song, podcast, audiobook)", 
                    status=status.HTTP_400_BAD_REQUEST)
    
            model = audio_type_model.get(audioFileType)
            inst = model.objects.get(id=audioFileID)
            audio_serializer = audio_type_serializer.get(audioFileType)
            metadata = data.get('audioFileMetadata')
            if audio_type == 'podcast':
                participent = metadata.get("participents", None)
                if (participent is None or len(participent) > 10 or 
                    any(i for i in participent if len(i) > 100)):
                    return Response({"invalid":"list of strings, each string cannot be larger than 100 characters, maximum of 10 participants possible"}, 
                    status=status.HTTP_400_BAD_REQUEST)
            serializer = audio_serializer(instance=inst,data=metadata)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
        except ObjectDoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
