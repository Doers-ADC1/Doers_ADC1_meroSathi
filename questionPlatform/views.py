from django.shortcuts import render, redirect
from .forms import OurForm
from .forms import Question
from django.db.models import Q
# Create your views here.
def upload_question(request):
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = OurForm()
    return render(request, "upload.html", {"form":form})

def book_list(request):

    context = {}
    query = " "

    if request.method == "GET":
        query = request.GET['q']

        question = get_data_queryset(str(query))
    # book = Book.objects.all()
    return render(request, "question_list.html", context)

def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ") #
    for q in queries:
        questions = Question.objects.filter(

            Q(title__icontains=q) |
            Q(name__icontains=q)
        )

        for question in questions:
            queryset.append(question)

    return list(set(queryset))