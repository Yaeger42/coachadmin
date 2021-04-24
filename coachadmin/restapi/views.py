from django.shortcuts import render
from coach.models import Coach
from restapi.serializers import CoachSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.
"""API VIEWS"""

@api_view(['GET']) 
def get_all_coaches(request):
    if request.method == 'GET':
        coaches = Coach.objects.all()
        serializer = CoachSerializer(coaches, many=True)
        return Response(serializer.data, 200)

@api_view(['GET'])
def get_one_coach(request, id):
    if request.method == 'GET':
        try:
            coach = Coach.objects.get(pk=id)
            serializer = CoachSerializer(coach, many=False)
            return Response(serializer.data)
        except Coach.DoesNotExist:
            return Response({ 'message': 'The coach with the given id does not exist'}, 404)
        

@api_view(['POST'])
def insert_coach(request):
    if request.method == 'POST':
        payload = request.body.decode('utf-8')
        post_insert = json.loads(payload)
        new_coach = Coach(**post_insert)
        new_coach.save()
        return Response({'message': 'The coach was saved successfully'}, 201) 


@api_view(['DELETE'])
def delete_coach(request, id):
    if request.method == 'DELETE':
        coach = Coach.objects.filter(pk=id).delete()
        return Response({'message': 'Coach deleted successfully'}, 202)


@csrf_exempt
@api_view(['PUT'])
def edit_coach(request):
    if request.method == 'PUT':
        payload = request.body.decode('utf-8')
        json_coach = json.loads(payload)
        try:
            edited_coach = Coach.objects.get(email=json_coach['email'])
            print(f'Edited coach: {edited_coach.lastName}')
            for i in json_coach.keys():
                if getattr(edited_coach, i, None) is not None:
                    setattr(edited_coach, i, json_coach[i])
            if 'new_email' in json_coach:
                setattr(edited_coach, 'new_email', json_coach['new_email'])
            edited_coach.save()
            return Response({'message': 'Coach edited successfully', 'coach' : CoachSerializer(edited_coach).data}, 202)
        except Coach.DoesNotExist:
            return Response({'message': f'The coach with {json_coach["email"]} does not exist'}, 404)