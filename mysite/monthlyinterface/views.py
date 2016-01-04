from django.http import HttpResponse
import sys
sys.path.insert(0, '/home/fabien/Prototypes/CC2015Goal3Month1')

#import BlendMeAPicture
# problem between Python2 and Python3...

def BlendMeAPicture(string):
    return string
    #cheating until it (month1) becomes a library compatible to python3

def index(request):
   return HttpResponse("Just testing so far : " + BlendMeAPicture("rewrite month1 to blend several pictures based on given topics"))
    # make it work outside of main

