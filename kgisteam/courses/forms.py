from django import forms

from courses.models import Problem
from courses.validators import validate_math_expression
from courses.maths import sn_round


class WorksheetProblemForm(forms.Form):
    user_answer = forms.CharField(
        label='',
        validators=[validate_math_expression],
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            }
        )
    )

    def clean_user_answer(self):
        """https://docs.djangoproject.com/en/2.2/ref/forms/validation/"""
        user_answer = eval(self.cleaned_data['user_answer'])
        user_answer_rounded = sn_round(user_answer)
        return user_answer_rounded
