from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class TestView(APIView):
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]

    #authentication_classes = []
    #permission_classes = []


    def get(self, request, format=None):
        # use request.query_params

        data = {'test_val': 'hello'}

        return Response(data)


    def post(self, request, format=None):
        data = request.data['test_val']

        return Response(data)

