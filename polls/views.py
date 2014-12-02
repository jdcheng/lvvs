import csv
import time
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils.safestring import mark_safe

from polls.models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        """Return the list of questions."""
        return Question.objects.order_by('-id')

class ReviewView(generic.ListView):
    template_name = 'polls/review.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        """Return the list of questions."""
        return Question.objects.order_by('id')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

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
    EDUCATION= [('Some high school', 'Some high school'),
    ('High school or G.E.D.','High school or G.E.D.'),("Some college or Associate's degree","Some college or Associate's degree"),
    ("Bachelor's degree or equivalent","Bachelor's degree or equivalent"),
    ('Postgraduate degree (such as M.A., Ph.D., M.D., J.D.)','Postgraduate degree (such as M.A., Ph.D., M.D., J.D.)')]
    RACE= [('African American','African American'),
    ('American Indian','American Indian'),
    ('Asian American','Asian American'),
    ('Caucasian','Caucasian'),
    ('Mexican American or Chicano','Mexican American or Chicano')]
    INCOME= [('below $20,000','below $20,000'),
    ('$20,000 to $40,000','$20,000 to $40,000'),
    ('$40,000 to $60,000','$40,000 to $60,000'),
    ('$60,000 to $80,000','$60,000 to $80,000'),
    ('Above $80,000','Above $80,000')]
    age = forms.CharField(required = False, label='1. Age\n', max_length = 100)
    gender = forms.ChoiceField(required = False, label="2. Gender\n", choices=GENDERS, widget=forms.RadioSelect())
    vision = forms.ChoiceField(required = False, label="3. Do you have normal or corrected to normal vision? \n", choices=YES, widget=forms.RadioSelect())
    acuity = forms.CharField(required=False, label=mark_safe('If you answered no, please describe your Snellen visual acuity (ex. 20/200) and the degree of your visual field.<br /><br /> Visual acuity:'), max_length = 100)
    field = forms.CharField(required=False, label='Degree of visual field\n', max_length = 100)
    reading = forms.ChoiceField(required = False, label="4. Do you consider yourself to have a reading disability?\n", choices=YES, widget=forms.RadioSelect())
    hearing = forms.ChoiceField(required = False, label="5. Do you have a hearing impairment?\n", choices=YES, widget=forms.RadioSelect())
    english = forms.ChoiceField(required = False, label="6. Are you a native English speaker?\n", choices=YES, widget=forms.RadioSelect())
    language = forms.CharField(required=False, label='If no, what is your native language?\n', max_length = 100)
    ipaduse = forms.ChoiceField(required = False, label="7. How many hours per week do you use an iPad?\n", choices=IPAD, widget=forms.RadioSelect())
    ipadexpertise = forms.ChoiceField(required = False, label="8. Please rate your level of iPad expertise (1 = novice, 10 = expert)\n", choices=[(x, x) for x in range(1, 11)])
    political = forms.ChoiceField(required = False, label="9. What is your political affiliation\n", choices=POLITICAL, widget=forms.RadioSelect())
    political_other = forms.CharField(required = False, label = "Other Political Affiliation\n", max_length = 100)
    ipaduse = forms.ChoiceField(required = False, label="10. How many national elections have you voted in?\n", choices=ELECTIONS, widget=forms.RadioSelect())
    locationsnational = forms.CharField(required = False, label='11. In which state(s) and county(s) have you voted in a national election?\n', max_length = 100)
    othertypes = forms.CharField(required = False, label='12. How many other elections of any type (local, school board, etc.) have you voted in?\n', max_length = 100)
    locationsother = forms.CharField(required = False, label='13. In which state(s) and county(s) have you voted in other types of elections?\n', max_length = 100)
    absentee = forms.ChoiceField(required= False, label=mark_safe("<b>***For questions 14 - 22, please answer keeping in mind your previous voting experience in any type of election (not including voting you did in this study). If you have never voted, please skip questions 14 - 22.*** </b><br /><br />14. Do you typically cast your vote on an absentee ballot?"), choices=YES, widget=forms.RadioSelect())
    bubble = forms.CharField(required=False, label=mark_safe('15. Please indicate how many times you have used each type of technology or ballot to cast your vote in any election.<br /> <br /> Fill in the bubble (or box)'), max_length = 100)
    arrows = forms.CharField(required = False, label = "Connect the arrows (or lines)\n", max_length = 100)
    open_response = forms.CharField(required = False, label = "Open response\n", max_length = 100)
    lever = forms.CharField(required = False, label = "Lever machines\n", max_length = 100)
    punchcard = forms.CharField(required = False, label = "Punchcards\n", max_length = 100)
    touchscreen = forms.CharField(required = False, label = "Electronic - touchscreen\n", max_length = 100)
    other_elec = forms.CharField(required = False, label = "Electronic - other\n", max_length = 100)
    dont_know = forms.CharField(required = False, label = "Don't know\n", max_length = 100)
    other = forms.CharField(required = False, label = "Other, please specify\n", max_length = 100)
    worried = forms.ChoiceField(required = False, label="Have you ever felt worried about figuring out how to use the ballot or technology to cast your vote?\n", choices=YES, widget=forms.RadioSelect())
    time_pressure = forms.ChoiceField(required = False, label="17. Have you ever felt that time pressure caused you to rush, make a mistake, or leave a choice blank when you would not otherwise have done so?\n", choices=YES, widget=forms.RadioSelect())
    time_prevent = forms.ChoiceField(required = False, label="18. If you have felt time pressure, did this prevent you from voting?\n", choices=YES, widget=forms.RadioSelect())
    straight_party = forms.ChoiceField(required = False, label="19. Do you typically vote a straight-party ticket?\n", choices=YES, widget=forms.RadioSelect())
    every_office = forms.ChoiceField(required = False, label="20. Do you typically cast a vote for every office on the ballot?\n", choices=YES, widget=forms.RadioSelect())
    unsure_cast = forms.ChoiceField(required = False, label="21. When you voted in an election, have you ever been unsure if your vote was cast correctly or would be counted?\n", choices=YES, widget=forms.RadioSelect())
    describe = forms.CharField(required = False, label=mark_safe("If yes, please describe the situation:\n"), max_length = 1000, widget=forms.Textarea(attrs= {'cols' : 100, 'rows' : 10}))
    satisfied_overall = forms.ChoiceField(required = False, label="22. On a scale of 1-10, with 1 being least satisfied and 10 being most satisfied, how satisfied are you with your past voting experiences overall?\n", choices=[(x, x) for x in range(1, 11)])
    occupation = forms.CharField(required=False, label='23. What is your current occupation?\n', max_length = 100)
    education = forms.ChoiceField(required=False, label="24. Please indicate the highest level of education you have completed.\n", choices=EDUCATION, widget=forms.RadioSelect())
    race = forms.ChoiceField(required=False, label="25. Are you:\n", choices=RACE, widget=forms.RadioSelect())
    hispanic = forms.CharField(required=False, label='Other Hispanic or Latino (please specify)\n', max_length = 100)
    multiracial = forms.CharField(required=False, label='Multiracial (please specify)\n', max_length = 100)
    other_race = forms.CharField(required=False, label='Other\n', max_length = 100)
    income = forms.ChoiceField(required=False, label="26. Which of the following income ranges best describes your yearly wages?\n", choices=INCOME, widget=forms.RadioSelect())
    satisfied_system = forms.ChoiceField(required = False, label="28. On a scale of 1-10, with 1 being least satisfied and 10 being most satisfied, how satisfied are you with your experience using our voting system?\n", choices=[(x, x) for x in range(1, 11)])
    which_features_used = forms.CharField(required = False, label=mark_safe("29. Which accessibility features did you use?\n"), max_length = 1000, widget=forms.Textarea(attrs= {'cols' : 100, 'rows' : 10}))
    which_features_helpful = forms.CharField(required = False, label=mark_safe("30. Which accessibility features did you find most helpful?\n"), max_length = 1000, widget=forms.Textarea(attrs= {'cols' : 100, 'rows' : 10}))
    improvements = forms.CharField(required = False, label=mark_safe("31. What improvements would you suggest for this voting system?\n"), max_length = 1000, widget=forms.Textarea(attrs= {'cols' : 100, 'rows' : 10}))

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def get_new_survey(request):
    if request.method == 'POST':
        form = NewSurvey(request.POST)
        filename = 'survey' + '_' + time.strftime("%d_%m_%Y") + '_' + time.strftime("%H%M%S") + '.csv'
        if form.is_valid():
            with open(filename, 'wb') as csvfile:
                votewriter = csv.writer(csvfile, delimiter=',')
                for data in form.fields.iteritems():
                    tag = data[0]
                    label = data[1].label
                    choice = form.cleaned_data[tag]
                    votewriter.writerow([label]+[choice])
            return render(request, 'polls/thanks.html')
    else:
        form = NewSurvey()
    return render(request, 'newsurvey.html', {'form': form})

def survey(request):
    return render(request, 'polls/survey.html')

all_questions = {}
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        all_questions[question_id] = request.POST['choice']
        request.session['all_questions'] = all_questions
    except (KeyError, Choice.DoesNotExist):
        # Go to the next race; a no vote
        p = get_object_or_404(Question, pk=question_id)
        # TODO: remove this hardcoded number
        if p.id == 162: # go to review page when done with voting
            return HttpResponseRedirect('http://lvvs.me/polls/review')
        return HttpResponseRedirect(reverse('polls:detail', args=(p.id+1,)))
        #return render(request, 'polls/detail.html', {
        #    'question': p,
        #    'error_message': "You didn't select a choice.",
        #})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # TODO: remove this hardcoded number
        if p.id == 162: # go to review page when done with voting
            return HttpResponseRedirect('http://lvvs.me/polls/review')
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:detail', args=(p.id+1,)))

def vote_previous(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        all_questions[question_id] = request.POST['choice']
        request.session['all_questions'] = all_questions
    except (KeyError, Choice.DoesNotExist):
        # Go to the next race; a no vote
        p = get_object_or_404(Question, pk=question_id)
        return HttpResponseRedirect(reverse('polls:detail', args=(p.id-1,)))
        #return render(request, 'polls/detail.html', {
        #    'question': p,
        #    'error_message': "You didn't select a choice.",
        #})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:detail', args=(p.id-1,)))

def forward(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    return HttpResponseRedirect(reverse('polls:detail', args=(p.id+1,)))

def back(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    return HttpResponseRedirect(reverse('polls:detail', args=(p.id-1,)))

def toballot(request):
    #p = get_object_or_404(Question, pk=question_id)
    if request.session['current_question_id'] is not None:
        return HttpResponseRedirect(reverse('polls:detail', args=(request.session['current_question_id'],)))
    else:
        return HttpResponseRedirect('polls/136')

def welcome(request):
    if request.method == 'POST':
        return render(request, 'polls/help.html')
        #return render(request, 'polls/options_initial.html')
    return render(request, 'polls/welcome.html')

def help(request):
    return render(request, 'polls/help.html')

def options_initial(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        return render(request, 'polls/options_initial.html')
        #return render(request, 'polls/help.html')
    return render(request, 'polls/welcome.html')

def options(request, question_id):
    request.session['current_question_id'] = question_id
    return render(request, 'polls/options.html')

def options_base(request):
    return render(request, 'polls/first_settings.html')

def submit_options(request):
    return render(request, 'polls/thanks.html')

def slider(request):
    return render(request, 'polls/slider.html')
