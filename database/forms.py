from django import forms
from database.models import *

class ContactForm(forms.ModelForm):
  
    class Meta:
        model = Contact
        fields = "__all__"

class FeedbackForm(forms.ModelForm):
  
    class Meta:
        model = Feedback
        fields = ('name','from_where','massage')


