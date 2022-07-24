import requests

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserProfileAPIView(APIView):
    def get(self, request, format=None):
        # platform = PC || PS4 || X1

        platform = request.GET.get('platform')
        username = request.GET.get('username')

        response = requests.get(
            url=f'https://api.mozambiquehe.re/bridge?'
                f'player={username}&platform={platform}&merge=true',
            headers={
                'Authorization': settings.STATUS_APEX_API_KEY
            }
        )

        if not response.ok:
            print(response)
            try:
                print(response.json())
            except Exception:
                pass
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = self.process_profile_data(response.json())
        return Response(data=data, status=status.HTTP_200_OK)

    def process_profile_data(self, data):
        keys_to_del = ['realtime', 'mozambiquehere_internal', 'ALS']

        for key in keys_to_del:
            del data[key]

        return data
