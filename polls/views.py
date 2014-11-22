import csv
import time
from django import forms
from django.shortcuts import get_object_or_404, render
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
    age = forms.CharField(label='1. Age', max_length = 100)
    gender = forms.ChoiceField(label="2. Gender", choices=GENDERS, widget=forms.RadioSelect())
    vision = forms.ChoiceField(label="3. Do you have normal or corrected to normal vision? ", choices=YES, widget=forms.RadioSelect())
    acuity = forms.CharField(required=False, label=mark_safe('If you answered no, please describe your Snellen visual acuity (ex. 20/200) and the degree of your visual field.<br /><br /> Visual acuity:'), max_length = 100)
    field = forms.CharField(required=False, label='Degree of visual field', max_length = 100)
    reading = forms.ChoiceField(label="4. Do you consider yourself to have a reading disability?", choices=YES, widget=forms.RadioSelect())
    hearing = forms.ChoiceField(label="5. Do you have a hearing impairment?", choices=YES, widget=forms.RadioSelect())
    english = forms.ChoiceField(label="6. Are you a native English speaker?", choices=YES, widget=forms.RadioSelect())
    language = forms.CharField(required=False, label='If no, what is your native language?', max_length = 100)
    ipaduse = forms.ChoiceField(required = False, label="7. How many hours per week do you use an iPad?", choices=IPAD, widget=forms.RadioSelect())
    ipadexpertise = forms.ChoiceField(label="8. Please rate your level of iPad expertise (1 = novice, 10 = expert)", choices=[(x, x) for x in range(1, 11)])
    political = forms.ChoiceField(label="9. What is your political affiliation", choices=POLITICAL, widget=forms.RadioSelect())
    political_other = forms.CharField(required = False, label = "Other Political Affiliation", max_length = 100)
    ipaduse = forms.ChoiceField(label="10. How many national elections have you voted in?", choices=ELECTIONS, widget=forms.RadioSelect())
    locationsnational = forms.CharField(label='11. In which state(s) and county(s) have you voted in a national election?', max_length = 100)
    othertypes = forms.CharField(label='12. How many other elections of any type (local, school board, etc.) have you voted in?', max_length = 100)
    locationsother = forms.CharField(label='13. In which state(s) and county(s) have you voted in other types of elections?', max_length = 100)
    absentee = forms.ChoiceField(required= False, label=mark_safe("<b>***For questions 14 - 22, please answer keeping in mind your previous voting experience in any type of election (not including voting you did in this study). If you have never voted, please skip questions 14 - 22.*** </b><br /><br />14. Do you typically cast your vote on an absentee ballot?"), choices=YES, widget=forms.RadioSelect())
    bubble = forms.CharField(required=False, label=mark_safe('15. Please indicate how many times you have used each type of technology or ballot to cast your vote in any election.<br /> <br /> Fill in the bubble (or box)'), max_length = 100)
    arrows = forms.CharField(required = False, label = "Connect the arrows (or lines)", max_length = 100)
    open_response = forms.CharField(required = False, label = "Open response", max_length = 100)
    lever = forms.CharField(required = False, label = "Lever machines", max_length = 100)
    punchcard = forms.CharField(required = False, label = "Punchcards", max_length = 100)
    touchscreen = forms.CharField(required = False, label = "Electronic - touchscreen", max_length = 100)
    other_elec = forms.CharField(required = False, label = "Electronic - other", max_length = 100)
    dont_know = forms.CharField(required = False, label = "Don't know", max_length = 100)
    other = forms.CharField(required = False, label = "Other, please specify", max_length = 100)
    worried = forms.ChoiceField(required = False, label="Have you ever felt worried about figuring out how to use the ballot or technology to cast your vote?", choices=YES, widget=forms.RadioSelect())
    time_pressure = forms.ChoiceField(required = False, label="17. Have you ever felt that time pressure caused you to rush, make a mistake, or leave a choice blank when you would not otherwise have done so?", choices=YES, widget=forms.RadioSelect())
    time_prevent = forms.ChoiceField(required = False, label="18. If you have felt time pressure, did this prevent you from voting?", choices=YES, widget=forms.RadioSelect())
    straight_party = forms.ChoiceField(required = False, label="19. Do you typically vote a straight-party ticket?", choices=YES, widget=forms.RadioSelect())
    every_office = forms.ChoiceField(required = False, label="20. Do you typically cast a vote for every office on the ballot?", choices=YES, widget=forms.RadioSelect())
    unsure_cast = forms.ChoiceField(required = False, label="21. When you voted in an election, have you ever been unsure if your vote was cast correctly or would be counted?", choices=YES, widget=forms.RadioSelect())
    describe = forms.CharField(required = False, label=mark_safe("If yes, please describe the situation: <br /><br />"), max_length = 1000, widget=forms.Textarea(attrs= {'cols' : 90, 'rows' : 10}))
    satisfied_overall = forms.ChoiceField(required = False, label="22. On a scale of 1-10, with 1 being least satisfied and 10 being most satisfied, how satisfied are you with your past voting experiences overall?", choices=[(x, x) for x in range(1, 11)])
    occupation = forms.CharField(required=False, label='23. What is your current occupation?', max_length = 100)
    education = forms.ChoiceField(required=False, label="24. Please indicate the highest level of education you have completed.", choices=EDUCATION, widget=forms.RadioSelect())
    race = forms.ChoiceField(required=False, label="25. Are you:", choices=RACE, widget=forms.RadioSelect())
    hispanic = forms.CharField(required=False, label='Other Hispanic or Latino (please specify)', max_length = 100)
    multiracial = forms.CharField(required=False, label='Multiracial (please specify)', max_length = 100)
    other_race = forms.CharField(required=False, label='Other', max_length = 100)
    income = forms.ChoiceField(required=False, label="26. Which of the following income ranges best describes your yearly wages?", choices=INCOME, widget=forms.RadioSelect())
    satisfied_system = forms.ChoiceField(required = False, label="28. On a scale of 1-10, with 1 being least satisfied and 10 being most satisfied, how satisfied are you with your experience using our voting system?", choices=[(x, x) for x in range(1, 11)])
    which_features_used = forms.CharField(required = False, label=mark_safe("29. Which accessibility features did you use? <br /><br />"), max_length = 1000, widget=forms.Textarea(attrs= {'cols' : 90, 'rows' : 10}))
    which_features_helpful = forms.CharField(required = False, label=mark_safe("30. Which accessibility features did you find most helpful? <br /><br />"), max_length = 1000, widget=forms.Textarea(attrs= {'cols' : 90, 'rows' : 10}))
    improvements = forms.CharField(required = False, label=mark_safe("31. What improvements would you suggest for this voting system? <br /><br />"), max_length = 1000, widget=forms.Textarea(attrs= {'cols' : 90, 'rows' : 10}))


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def get_new_survey(request):
    if request.method == 'POST':
        form = NewSurvey(request.POST)
        filename = 'survey' + '_' + time.strftime("%d_%m_%Y") + '_' + time.strftime("%H%M%S") + '.csv'
        if form.is_valid():
            with open(filename, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',')
                for value in form.cleaned_data.iteritems():
                    spamwriter.writerow([value])
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