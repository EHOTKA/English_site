from django import forms


class PostForm(forms.Form):
	field = ('title', 'text',)


'''from .models import Post

class PostForm(forms.ModelForm):


	class Meta:
		model = Post
		field = ('title', 'text',)'''