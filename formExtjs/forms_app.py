import sys
from django.forms.models import ModelForm
from django import forms
from django.forms import widgets
import models

TESTING = 'test' in sys.argv
if TESTING:
    class FormTesteTT(ModelForm):
        choice_field = forms.ChoiceField(choices=((1, 'Um'), (2, 'Dois')))
        typed_choice_field = forms.TypedChoiceField(choices=((1, 'Um'), (2, 'Dois')))
        multiple_choice_field = forms.MultipleChoiceField(choices=((1, 'Um'), (2, 'Dois')))
        typed_multiple_choice_field = forms.TypedMultipleChoiceField(choices=((1, 'Um'), (2, 'Dois')))
        regex_field = forms.RegexField(regex='[0-9]')
        file_field = forms.FileField()
        image_field = forms.ImageField()
        password_field = forms.CharField(widget=widgets.PasswordInput)
        hidden_field = forms.CharField(widget=widgets.HiddenInput)
        file_widget_field = forms.CharField(widget=widgets.FileInput)
        text_area_field = forms.CharField(widget=widgets.Textarea)
        radio_field = forms.ChoiceField(choices=((1, 'Um'), (2, 'Dois')), widget=widgets.RadioSelect)
        checkbox_select_multiple_field = forms.MultipleChoiceField(choices=((1, 'Um'), (2, 'Dois')), widget=widgets.CheckboxSelectMultiple)
        
        class Meta:
            model = models.ModeloParaTesteTT

    class ChildForm(forms.ModelForm):
        class Meta:
            model = models.Child

    class CharFieldWithChoicesForm(forms.ModelForm):
        class Meta:
            model = models.CharFieldWithChoices

    class ChoiceForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(ChoiceForm, self).__init__(*args, **kwargs)
            for arg in args:
                if 'poll' in arg:
                    choices = models.Choice.objects.filter(poll=arg['poll'])
                    self.fields['choice'].queryset = choices
                    self.fields['choice'].widget = forms.Select(choices=[(choice.pk, str(choice)) for choice in choices])

        class Meta:
            model = models.Choice