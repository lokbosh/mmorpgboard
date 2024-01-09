from django import forms
from .models import Post,Response
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'text': CKEditorWidget(),
        }
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
        labels = ['Response']
        
        widgets = {'text':forms.Textarea(attrs={'rows':5,'cols':70,'placeholder':'Введите текст отклика'})}
        


