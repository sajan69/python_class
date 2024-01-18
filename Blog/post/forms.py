from django import forms
from django.forms.widgets import TextInput
from post.models import BlogPost, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all().filter(is_active=True),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    content = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':'3'
            }
        )
    )

    image = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    is_active = forms.BooleanField(required=False,initial=True)
    is_featured = forms.BooleanField(required=False,initial=False)

    class Meta:
        model = BlogPost
        fields = ['title','category', 'content', 'image','is_featured', 'is_active']

