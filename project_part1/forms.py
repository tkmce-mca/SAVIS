from django import forms
from django.forms import ModelForm
from .models import upload

class SimpleForm(forms.ModelForm):
    class Meta:
        model=upload
        #fields=['chapter','teacher_name','teacher_id','upload_mal','upload_eng','upload_sci']
        fields = "__all__"
