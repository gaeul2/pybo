from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer


# Create your views here.



def index(request):
    if request.method == "GET":
        all_questions = Question.objects.order_by('-create_date')
        context = {
            'questions':all_questions
        }
        return render(request, 'board/index.html', context)


def detail(request, question_id):
    if request.method == "GET":
        clicked_question = get_object_or_404(Question, pk=question_id)
        context = {'question':clicked_question}
        return render(request, 'board/question_detail.html', context)


def answer_create(request, question_id):
    if request.method == "POST":
        question = get_object_or_404(Question, pk=question_id)
        answer = Answer.objects.create(question=question, content=request.POST['comment'])
        print(question, answer)
        answer.save()
        return redirect('board:question_detail', question_id=question_id)