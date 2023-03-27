from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt

from api.models import Risk

from api.serializers import RiskSerializer

# add a risk
@api_view(['POST'])
def AddRiskAPI(request):
    serializer = RiskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# get all risk
@api_view(['GET'])
def RisksAPI(request):
    Risks = Risk.objects.all()
    serialized = RiskSerializer(Risks, many=True)
    return Response(serialized.data)

# retrieve, edit and delete a Risk
@api_view(['GET', 'PUT', 'DELETE'])
def RiskAPI(request, pk):
    try:
        risk = Risk.objects.get(id=pk)
        if request.method == 'GET':
            serialized = RiskSerializer(risk, many=False)
            return Response(serialized.data)
        
        elif request.method == 'PUT':
            serializer = RiskSerializer(risk, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
        elif request.method == 'DELETE':
            risk.delete()
            return Response({'message': 'Risk was deleted successfully!'}, status=200)

    except Risk.DoesNotExist:
        return Response({'message': 'Risk does not exist!'}, status=404)