from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    return HttpResponse("fuck all")
	
def all_data(request):
	latest_question_list = Question.objects.order_by('-telecast_data')
	output = ', '.join(["	||	" +"name: " + q.telecast_text + "	||	" + 
						"length: " + str(q.telecast_length) + "	||	"  +
						"time: " + str(q.telecast_data) + "	||	" 
	for q in latest_question_list])
	return HttpResponse(output)
	
def add_data(request, name, length, description, spamf):
	q = Question(telecast_text=name, telecast_length=length, telecast_data='2016-12-07%2016:41:47.716200+00:00', telecast_description=description, spam_on_off=spamf)
	return q.save()
	