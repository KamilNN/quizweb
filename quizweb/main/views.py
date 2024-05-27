from django.shortcuts import render, redirect
from .models import Question, Category, Word
from django.views.generic import ListView


def index(request):
    return render(request, 'main/index.html')


def quiz_view(request, category_id):
    questions = Question.objects.filter(category_id=category_id)
    return render(request, 'main/quiz.html', {'questions': questions})


def check(request, category_id):
    if request.method == 'POST':
        count = 0
        questions = Question.objects.filter(category_id=category_id)
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            if selected_option == question.correct_option:
                count += 1
        return render(request, 'main/result.html', {'count': count, 'total': questions.count()})
    return redirect('quiz')

def category_view(request):
    categories = Category.objects.all()
    return render(request, 'main/category.html', {'categories': categories})


class WordList(ListView):
    model = Question
    context_object_name = 'words'
    template_name = 'main/word_list.html'

