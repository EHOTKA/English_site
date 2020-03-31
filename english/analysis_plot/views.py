from django.shortcuts import render

def post_list(request):
	return render(request, 'analysis_plot/post_list.html', {})