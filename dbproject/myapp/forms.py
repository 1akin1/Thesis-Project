from django import forms
from myapp.models import Thesis

class ThesisForm(forms.ModelForm):  
    class Meta:  
        model = Thesis  
        fields = [
            'author', 'type', 'title', 'abstract', 'university', 'institute', 
            'keyword', 'language', 'subject', 'supervisor', 'cosupervisor', 'date'
        ]  
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),  # Added missing type field
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}),
            'institute': forms.TextInput(attrs={'class': 'form-control'}),
            'keyword': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'supervisor': forms.TextInput(attrs={'class': 'form-control'}),
            'cosupervisor': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Added date field
        }
