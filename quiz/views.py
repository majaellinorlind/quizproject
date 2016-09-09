from django.shortcuts import render
from quiz.models import Quiz

def start(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
	    "question": "Do you use the company instagram soley for seminar/conference/meeting pictures?",
		"answer1": "Yes",
	   	"answer2": "No",
	    "quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def results(request, quiz_number):
	context = {
	    "correct": 1,
	    "total": 15,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)


