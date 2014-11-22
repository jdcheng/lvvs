import csv
import time
from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        """Return the list of questions."""
        return Question.objects.order_by('-id')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class SizeForm(forms.Form):
    title_size = forms.CharField(label='Size of title', max_length = 100)
    choice_size = forms.CharField(label='Size of choices', max_length = 100)

class NewSurvey(forms.Form):
    GENDERS=[('Male', 'Male'), ('Female', 'Female')]
    YES= [('Yes', 'Yes'), ('No', 'No')]
    IPAD= [('less than 5 hours','less than 5 hours'),
     ('between 5 and 10 hours','between 5 and 10 hours'),
      ('between 10 and 20 hours','between 10 and 20 hours'),
       ('between 20 and 30 hours','between 20 and 30 hours'),
        ('between 30 and 40 hours','between 30 and 40 hours'),
         ('over 40 hours','over 40 hours')]
    POLITICAL= [('Republican','Republican'),
     ('Democrat','Democrat'),
      ('Libertarian','Libertarian'),
       ('Independent','Independent'),
        ('Other, please specify:','Other, please specify:')]
    ELECTIONS = [('None','None'),
     ('1 to 8','1 to 8'),
      ('9 to 15','9 to 15'),
       ('15 or more','15 or more')]
    age = forms.CharField(label='1. Age', max_length = 100)
    gender = forms.ChoiceField(label="2. Gender", choices=GENDERS, widget=forms.RadioSelect())
    vision = forms.ChoiceField(label="3. Do you have normal or corrected to normal vision? finish 3!!", choices=YES, widget=forms.RadioSelect())
    reading = forms.ChoiceField(label="4. Do you consider yourself to have a reading disability?", choices=YES, widget=forms.RadioSelect())
    hearing = forms.ChoiceField(label="5. Do you have a hearing impairment?", choices=YES, widget=forms.RadioSelect())
    english = forms.ChoiceField(label="6. Are you a native English speaker?", choices=YES, widget=forms.RadioSelect())
    language = forms.CharField(required=False, label='If no, what is your native language?', max_length = 100)
    ipaduse = forms.ChoiceField(label="7. How many hours per week do you use an iPad?", choices=IPAD, widget=forms.RadioSelect())
    ipadexpertise = forms.ChoiceField(label="8. Please rate your level of iPad expertise (1 = novice, 10 = expert)", choices=[(x, x) for x in range(1, 11)])
    political = forms.ChoiceField(label="9. What is your political affiliation", choices=POLITICAL, widget=forms.RadioSelect())
    political_other = forms.CharField(required = False, label = "Other Political Affiliation", max_length = 100)
    ipaduse = forms.ChoiceField(label="10. How many national elections have you voted in?", choices=ELECTIONS, widget=forms.RadioSelect())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def get_new_survey(request):
    if request.method == 'POST':
        form = NewSurvey(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            return HttpResponseRedirect(reverse('polls:options'))
    else:
        form = NewSurvey()
    return render(request, 'newsurvey.html', {'form': form})

def survey(request):
    return render(request, 'polls/survey.html')

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
            "titleSize": 40,
            "choiceSize": 30,
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:detail', args=(p.id+1,)))

def forward(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    return HttpResponseRedirect(reverse('polls:detail', args=(p.id+1,)))

def back(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    return HttpResponseRedirect(reverse('polls:detail', args=(p.id-1,)))

def get_title_size(request):
    if request.method == 'POST':
        form = SizeForm(request.POST)
        if form.is_valid():
            title_size = form.cleaned_data['title_size']
            choice_size = form.cleaned_data['choice_size']
            return render(request, 'polls/options.html')
    else:
        form = SizeForm()
    return render(request, 'sizeform.html', {'form': form})

def toballot(request):
    return render(request, 'polls/survey.html')

def options(request, question_id):
    return render(request, 'polls/options.html')

def options_base(request):
    return render(request, 'polls/options.html')

def submit_options(request):
    return render(request, 'polls/thanks.html')

def submit_survey(request):
    filename = 'survey' + '_' + time.strftime("%d_%m_%Y") + '_' + time.strftime("%H%M%S") + '.csv'
    with open(filename, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    return render(request, 'polls/thanks.html')