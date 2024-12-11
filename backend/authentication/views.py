from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

class HomeView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
       content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
       return Response(content)
    



class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

            # Attempt to parse the token as a RefreshToken
            token = RefreshToken(refresh_token)

            # Blacklist the token
            token.blacklist()

            return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response(
                {
                    "error": "Invalid or expired token",
                    "details": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except InvalidToken as e:
            return Response(
                {"error": "The provided token is not a valid refresh token", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": "An unexpected error occurred", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
