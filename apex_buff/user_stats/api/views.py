import requests

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserProfileAPIView(APIView):
    def get(self, request, format=None):
        # platform = origin || xbl || psn

        platform = self.handle_platform_type(request.GET.get('platform'))
        username = request.GET.get('username')

        response = requests.get(
            url=f'https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{username}',
            headers={
                'Trn-Api-Key': settings.TRACKER_APEX_API_KEY
            }
        )
        data = response.json()
        return Response(data=data, status=status.HTTP_200_OK)

    def handle_platform_type(self, platform):
        allowed_platforms = ['PC', 'PS4', 'X1', 'origin', 'psn', 'xbl']

        if platform not in allowed_platforms:
            return 'origin'

        status_tracker_apis_map = {
            'PC': 'origin',
            'PS4': 'psn',
            'X1': 'xbl'
        }

        if platform in status_tracker_apis_map:
            platform = status_tracker_apis_map[platform]
        return platform
