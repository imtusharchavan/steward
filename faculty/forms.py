from django import forms
from accounts.models import Faculty



class FacultyModelForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = (
            'user',
            'profile_picture',
            'phone_number',
            'title',
            'designation',
            'educational_qualification',
            'honors_awards',
            'research_interests',
            'publications',
            'other_responsibliites',
        )