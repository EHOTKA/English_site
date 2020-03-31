from django.shortcuts import render

from .forms import PostForm

def index(request):
	return render(request, 'analysis_plot/index.html', {})

def analys(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			return
	else:
		form = PostForm()
	return render(request, 'analysis_plot/analys.html', {'form': form})