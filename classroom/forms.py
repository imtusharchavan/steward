from django import forms
from .models import Classroom



class ClassroomModelForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = (
            'code',
            'name',
            'subject',
        )