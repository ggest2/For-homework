from django import forms
from mzfinder.models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # 사용할 모델
        fields = ['content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'content']