from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'firstApp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'firstApp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'firstApp/results.html'

class FinishView():
    template_name = 'firstApp/finish.html'

def finish(request):
    return render(request, 'firstApp/firstApp/finish.html');


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'firstApp/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'firstApp/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'firstApp/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'firstApp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('firstApp:results', args=(question.id,)))
