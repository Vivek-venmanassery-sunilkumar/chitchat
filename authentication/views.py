from rest_framework.views import APIView
# Create your views here.


class Signup(APIView):  
    def post(self, request):
        data = request.data
        
