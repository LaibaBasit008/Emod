from django.shortcuts import render
from django.http import HttpResponse
from .test import test
import os
from django.conf.urls.static import static

def hi(req):
	context={}
	context["val"]="none"
	if req.method == 'POST' :
		context={}
		context["val"]=test()
		
        
	return render(req,'emod/home.html',context)
        

    