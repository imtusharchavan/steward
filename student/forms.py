from django import forms
from accounts.models import Student



class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'user',
            'gender',
            'date_of_birth',
            'phone_number',
            'course',
            'semester',
            'current_year',
        )