from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from rest_framework import viewsets

from .serializers import TesterSerializer

from .models import Choice, Question, TesterModel


# # def vote(request, question_id):
# #     return HttpResponse("You're voting on question %s." % question_id)

# # using templates
# # def index(request):
# #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #     output = ', '.join([q.question_text for q in latest_question_list])
# #     return HttpResponse(output)
# # def index(request):
# #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #     template = loader.get_template('polls/index.html')
# #     context = {
# #         'latest_question_list': latest_question_list,
# #     }
# #     return HttpResponse(template.render(context, request))
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# # raising errors
# # def detail(request, question_id):
# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist")
# #     return render(request, 'polls/detail.html', {'question': question})
# # using the shortcut feature:
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

#-------------------------------------------------------------------------------------------------------------
# using the generic view method. replaces the above format.
# Here ListView and DetailView are used
# seems like they are just page layout method?
# WHAT IS THE MODEL ATTRIBUITE BECAUSE "EACH VIEW NEED TO KNOW WHAT MODEL IT WILL BE ACTING UPON"? (apparently in our case it is Question)
# so detailvie expects primary key value captured form URL to be called 'pk' is is what it is hoho
# ---> # that's why urls.py format has been changed
# both ListView and DetailView needs template name --> don't use the default
# --> does it mean there is also a default template 
# --> yes :  <app name>/<model name>_detail.html for detailview and  <app name>/<model name>_list.html for listviw
# --> wonder if the template would be autogenerated probably not, probably ypou need to make it and it will search that default if not specified
# For DetailView the question variable is provided automatically – since we’re using a Django model (Question)
# for ListView, the automatically generated context variable is "question_list". To override this we provide the context_object_name attribute
#-------------------------------------------------------------------------------------------------------------
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        # pub_date that is less than or equal to timezone.now()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


