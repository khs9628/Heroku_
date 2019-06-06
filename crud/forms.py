from django import forms
from .models import Blog, Comment,Hashtag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','hashtags', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': '제목.'}),
            
        }
        
        labels = {
            'title' : '제목',
            'body' : '내용', 
            'image' : '이미지'       
            }

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Hashtag.'}),
        }
        
        labels = {
            'name' : '해시태그',     
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]
        widgets = {
            'comment_text': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': '댓글 등록'}),
            
        }
        
        labels = {
            'comment_text' : '댓글',       
            }
