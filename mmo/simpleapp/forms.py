from django import forms
from .models import Post,Response
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        text = forms.CharField(min_length=2)
    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")

        if title == text:
            raise ValidationError(
                "Текст не должно быть идентично названию."
            )
        return cleaned_data
    
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']
        widgets = {'res_user': forms.HiddenInput()}