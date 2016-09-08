from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
   		"name": "Big Fat Quiz of Maja",
	   	"description": "Take me to the quiz!"
	},
	{
		"quiz_number": 2,
   	   	"name": "Största 1slagen",
	   	"description": "Kan du dina lag?"
	},
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
	    "question": "Hur många bultar har ölandsbron?",
		"answer1": "12",
	   	"answer2": "66 400",
	    "answer3": "7 428 954",
	    "quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def results(request, quiz_number):
	context = {
	    "correct": 12,
	    "total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)


