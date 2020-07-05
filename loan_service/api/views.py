from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from loan_service.api.serializers import LoanRequestSerializerSave, LoanRequestSerializerReturn


@api_view(['POST'])
def create_loan(request):
    serializer = LoanRequestSerializerSave(data=request.data)

    if serializer.is_valid():
        loan = serializer.save()
        test = LoanRequestSerializerReturn(instance=loan)
        return Response(test.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'erros': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
