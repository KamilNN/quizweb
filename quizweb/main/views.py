from django.shortcuts import render, redirect
from .models import Question, Category, TestResult
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
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
        score = count
        TestResult.objects.create(user=request.user, category_id=category_id, score=score)
        return render(request, 'main/result.html', {'count': count, 'total': questions.count()})
    return redirect('quiz')


def category_view(request):
    categories = Category.objects.all()
    return render(request, 'main/category.html', {'categories': categories})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('category')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('category')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


@login_required
def view_results(request):
    results = TestResult.objects.filter(user=request.user)
    return render(request, 'main/myresults.html', {'results': results})


class WordList(ListView):
    model = Question
    context_object_name = 'words'
    template_name = 'main/word_list.html'

