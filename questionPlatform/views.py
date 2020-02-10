from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Question, Answer
from questionPlatform.forms import questionForm, answerForm
from django.db.models import Q
from django.contrib import messages


def home(request):
    show_all = Question.objects.all()

    context_dict = {
        'show_all': show_all,
    }

    return render(request, 'home.html', context_dict)


def answers(request, id):
    ques = Question.objects.get(id=id)

    ans = Answer.objects.filter(question=ques)

    context_dict = {
        'questions': ques,
        'answers': ans,
    }

    return render(request, 'answers.html', context_dict)


@login_required
def add_questions(request):
    form = questionForm()
    if request.method == "POST":
        form = questionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            # messages.success(request, "Added Question Sucessfully")
            return redirect('home')

    context_dict = {'form': form}
    return render(request, 'addQuestions.html', context_dict)


def edit_question(request, id):
    edit_ques = Question.objects.get(id=id)

    if request.method == "POST":
        form = questionForm(request.POST, request.FILES, instance=edit_ques)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = questionForm(instance=edit_ques)
    context_dict = {'form': form}
    return render(request, 'edit_question.html', context_dict)


@login_required
def post_answer(request, id):
    ques_post = Question.objects.get(id=id)
    form = answerForm()

    if request.method == 'POST':
        form = answerForm(request.POST)
        if form.is_valid():
            cmt_ans = form.save(commit=False)
            cmt_ans.question = ques_post
            cmt_ans.ans_author = request.user
            cmt_ans.save()

            return redirect('/question/answers/' + id)

    context_dict = {'form': form}
    return render(request, 'postAnswer.html', context_dict)


def delete_question(request, id):
    ques = Question.objects.get(id=id)
    ques.delete()

    return redirect('/')


def search(request):
    sqs = request.POST.get('q')
    if sqs:
        ques = Question.objects.filter(Q(question__icontains=sqs))
    else:
        ques = []
    context_dict = {"ques": ques}
    return render(request, 'search_result.html', context_dict)


def own_posts(request):
    filter_author = Question.objects.filter(author=request.user)
    context_dict = {
        'filter_author': filter_author,
    }

    return render(request, "my_posts.html", context_dict)


def latest_posts(request):
    try:
        latest_posts = Question.objects.all().order_by('-post_date')
    except:
        latest_posts = []

    context_dict = {
        'latest_posts': latest_posts,
    }

    return render(request, 'latest_posts.html', context_dict)

# # Create your views here.
# def upload_question(request):
#     if request.method == "POST":
#         form = OurForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('question_list')
#     else:
#         form = OurForm()
#     return render(request, "upload.html", {"form":form})
#
# def book_list(request):
#
#     context = {}
#     query = " "
#
#     if request.method == "GET":
#         query = request.GET['q']
#
#         question = get_data_queryset(str(query))
#     # book = Book.objects.all()
#     return render(request, "question_list.html", context)
#
# def get_data_queryset(query=None):
#     queryset = []
#     queries = query.split(" ") #
#     for q in queries:
#         questions = Question.objects.filter(
#
#             Q(title__icontains=q) |
#             Q(name__icontains=q)
#         )
#
#         for question in questions:
#             queryset.append(question)
#
#     return list(set(queryset))
