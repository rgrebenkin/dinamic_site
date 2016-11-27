from django.shortcuts import render, get_object_or_404
from django.view.decorators.http import require_GET
from django.http import HttpResponse 
from django.core.paginator import Paginator

def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def get_new_questions(request, page = 1):
  questions = Question.objects.new()
  limit = 10
  #page = request.GET.get('page', 1)
  paginator = Paginator(questions, limit)
  paginator.baseurl = '/?page='
  page = paginator.page(page) # Page
  return render(request, 'qa/question_list.html', 
		{ 'questions' : page.object_list,
		  'paginator' : paginator,
		  'page' :page }

@require_GET
def get_popular_questions(request, page = 1):
  questions = Question.objects.popular()
  limit = 10
  #page = request.GET.get('page', 1)
  paginator = Paginator(questions, limit)
  paginator.baseurl = '/?page='
  page = paginator.page(page) # Page
  return render(request, 'qa/question_list.html', 
		{ 'questions' : page.object_list,
		  'paginator' : paginator,
		  'page' : page }

@require_GET
def get_question(request, id):
  question = get_object_or_404(Question, id=id)
  answers = Answer.objects.filter(question = question).all()
  return render(request, 'qa/question_details.html', { 'question' : question , 'answers' = answers }
  pass



