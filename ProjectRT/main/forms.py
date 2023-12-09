from django import forms
from .models import TableInTarget

class UserForm(forms.ModelForm):
    class Meta:
        model = TableInTarget
        fields = ['kk_result']  # Укажите поля, которые вы хотите отображать в форме