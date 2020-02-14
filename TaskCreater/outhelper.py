import asana
from django.urls import reverse
import time
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json
def Sign_url():
    client=ClientAsana()
    (sign_in_url, state) = client.session.authorization_url()
    return sign_in_url,state
def ClientAsana():
    client = asana.Client.oauth(
        client_id='1161736610121274',
        client_secret='9c85fbc468cc8c27dbd336abba18fb29',
        redirect_uri='https://asanataskcreater.herokuapp.com/taskcreater/gettoken/'
        )
    return client
def save_token_from_code(request,redirect_uri):
    client=ClientAsana()
    auth_code = request.GET['code']
    token=client.session.fetch_token(code=auth_code)
    access_token = token['access_token']
    refresh_token = token['refresh_token']
    expires_in = token['expires_in']
    expiration = int(time.time()) + expires_in - 300
    # Save the token in the session
    request.session['access_token'] = access_token
    request.session['refresh_token'] = refresh_token
    request.session['token_expires'] = expiration
    return access_token
def TasksViewer(request,workspace_code,access_token):
    url="https://app.asana.com/api/1.0/tasks?assignee=me&completed_since=now&limit=10&workspace={}".format(workspace_code)
    headers = {
              'Authorization' : 'Bearer {0}'.format(access_token),
               }
    response=requests.get(url,headers=headers).json()
    return response
def workspaceIds(request):
  access_token=request.session['access_token']
  access_token=request.session['access_token']
  client = asana.Client.access_token(access_token)
  workspaces = list(client.workspaces.find_all())
  return workspaces
def taskadd(request,workspaceIds,name):
    try:
      access_token=request.session['access_token']
    except:
      return HttpResponseRedirect(reverse("TaskCreater:home"))
    url="https://app.asana.com/api/1.0/tasks"
    headers = { 'User-Agent' : 'python_tutorial/1.0',
              'Content-Type' : 'application/json',
              'Authorization' : 'Bearer {0}'.format(access_token),
              'Accept' : 'application/json' }
    parameters={
        "data":{
            "assignee" : "me",
            "name": name,
            "workspace": workspaceIds
        },
    }
    response = requests.post(url, headers = headers, data =json.dumps(parameters), params =  parameters)
    return response

    
