from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            'access': response.data.get('access'),
            'refresh': response.data.get('refresh'),
            'message': 'Login successful'
        }, status=status.HTTP_200_OK)