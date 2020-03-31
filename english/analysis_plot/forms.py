from django import forms


class PostForm(forms.Form):
	analysText = forms.CharField(max_length=200)


'''from .models import Post

class PostForm(forms.ModelForm):


	class Meta:
		model = Post
		field = ('title', 'text',)'''