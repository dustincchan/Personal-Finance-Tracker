from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import datetime, pytz, requests



class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

def login(request):
    oauth = {
            'REDIRECT_URI_ENCODED': "http%3A//127.0.0.1%3A8000/home",
            'CLIENT_ID_ENCODED': 'DE6WMy4AgB529A0znKttGySkWF31AJ6ZqgRvikrS',
            'SCOPES_ENCODED': 'unsure_at_the_moment'
            }
    return render(request, "registration/login.html", oauth)

def home(request):
    get_params = request.GET

    if 'error' in get_params:
        raise ValueError('Error authorizing application: %s' % get_params[error])

    response = requests.post('https://drchrono.com/o/token/', data={
        'code': get_params['code'],
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://127.0.0.1:8000/home',
        'client_id': 'DE6WMy4AgB529A0znKttGySkWF31AJ6ZqgRvikrS',
        'client_secret': 'LxGI0TJ05agf3E8XJocB4BXyfxfB3TpLron8iAlltlbt4IsXbHNccP1O3rsIUTTbUQCWio8TL6fCWvn32HdfFQJ0fenBfqDBplhy3ha56zPlGc0UpgR5vn8juB0HqRNv',
    })
    response.raise_for_status()
    data = response.json()

    # Save these in your database associated with the user
    print request.user
    access_token = data['access_token']
    refresh_token = data['refresh_token']
    expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])

    return render(request, "home.html")

@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)
