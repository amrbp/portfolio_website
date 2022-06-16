from django import forms
from database.models import Contact

class ContactForm(forms.ModelForm):
  
    class Meta:
        model = Contact
        fields = "__all__"

