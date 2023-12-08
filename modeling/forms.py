from django import forms
from modeling.models import Modeling, Comment


class ModelingForm(forms.ModelForm):
    class Meta:
        model = Modeling
        fields = ['title', 'model_file', 'thumbnail', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글',
        }