from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import asana
import time
from django.urls import reverse
from TaskCreater import outhelper
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import uuid
def home(request):
  (Sing_url_home,state)=outhelper.Sign_url()
  context = { 'signin_url': Sing_url_home}
  return render(request, 'home.html', context)
def gettoken(request):
  redirect_uri=reverse("TaskCreater:view")
  outhelper.save_token_from_code(request,redirect_uri)
  return HttpResponseRedirect(redirect_uri)
def view(request):
  try:
    workspaces=outhelper.workspaceIds(request)
  except:
    rdi=reverse("TaskCreater:index")
    return HttpResponseRedirect(rdi)
  context = {"gids" : workspaces}
  return render(request,'workspace_view.html',context)
def viewwork(request):
  try:
    access_token=request.session['access_token']
  except:
    rdi=reverse("TaskCreater:index")
    return HttpResponseRedirect(rdi)
  workspace_code = request.GET['gid']
  tasks_temp=outhelper.TasksViewer(requests,workspace_code,access_token)
  try:
    tasks=tasks_temp['data']
  except:
    rdi=reverse("TaskCreater:index")
    return HttpResponseRedirect(rdi)
  contex={"tasks" : tasks}
  return render(request,"mail.html",contex)
def createtask(request):
  try:
    workspaces=outhelper.workspaceIds(request)
  except:
    rdi=reverse("TaskCreater:index")
    return HttpResponseRedirect(rdi)
  context = {"gids" : workspaces}
  return render(request,"workspace.html",context)
@csrf_exempt
def taskset(request):
  if request.method=="POST":
    WorkSpaceId=request.POST['workspace']
    name=request.POST['name']
    response=outhelper.taskadd(request,WorkSpaceId,name)
    redirect_uri_temp=reverse("TaskCreater:view")
    redirect_uri=redirect_uri_temp+"tasks?gid={}".format(WorkSpaceId)
  return HttpResponseRedirect(redirect_uri)