from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from users.models import Student



User = get_user_model()

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'user',
            'enrollment_no',
            'gender',
            'date_of_birth',
            'phone_number',
            'course',
            'current_year',
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        field_classes = {"username": UsernameField}