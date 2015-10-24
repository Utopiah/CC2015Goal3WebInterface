from django.http import HttpResponse
import sys
sys.path.insert(0, '/home/fabien/Prototypes/CC2015Goal3Month1')

#import BlendMeAPicture
# problem between Python2 and Python3...

def BlenMeAPicture(string):
    return string
    #cheating until it becomes a library compatible to python3

def index(request):
   return HttpResponse("Just testing so far : " + BlenMeAPicture("Brussels"))
    # make it work outside of main

