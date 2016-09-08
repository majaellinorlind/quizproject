from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
   		"name": "Big Fat Quiz of Maja",
	   	"description": "Take me to the quiz!"
	},
	{
		"quiz_number": 2,
   	   	"name": "How much do you know about Majas?",
	   	"description": "Take me to the quiz!"
	}
]

def start(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number) - 1],
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
	    "correct": 8,
	    "total": 15,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)


