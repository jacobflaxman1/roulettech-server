from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TextAPIView(APIView):
    def get(self, request):
        data = {
            "bio_text": "I love tinkering with electronics of all forms. From embedded systems to full-stack development, I have done it all. In my free time, I build and design digital instruments and synthesizers. I love learning new technologies and ways to improve my skills as an engineer. Thank you for your interest in my application!",
            "header_text": "Hi, I'm",
            "header_text_color": "Jacob",
            "sub_header_text": "Computer Engineer"
        }
        return Response(data, status=status.HTTP_200_OK)
    

class GitHubLinkAPIView(APIView):
    def get(self, request):
        data = {
            "github_link": "https://github.com/jacobflaxman1/SeniorDesignElephant"
        }
        return Response(data, status=status.HTTP_200_OK)