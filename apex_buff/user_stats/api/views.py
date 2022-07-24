import requests

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserProfileAPIView(APIView):
    def get(self, request, format=None):
        # platform = origin || xbl || psn
        # platformUserIdentifier = basically username
        platform = request.GET.get('platform')
        platform_user_identifier = request.GET.get('platformUserIdentifier')

        response = requests.get(
            url=f'https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{platform_user_identifier}',
            headers={
                'TRN-Api-Key': settings.TRACKER_API_KEY,
                'Accept': 'application/json',
                'Accept-Encoding': 'gzip'
            }
        )

        if not response.ok:
            print(response)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = self.process_profile_data(response.json())

        return Response(data=data, status=status.HTTP_200_OK)

    def process_profile_data(self, data):
        data = data['data']
        keys_to_del = ['userInfo', 'expiryDate']

        for key in keys_to_del:
            del data[key]

        return data
