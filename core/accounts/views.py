from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.urls import reverse_lazy

from .forms import RegistrationForm, LoginForm


@require_http_methods(["GET", "POST"])
def register_view(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# auto-login after registration
			user = authenticate(request, username=user.email, password=request.POST.get('password1'))
			if user:
				login(request, user)
			return redirect('blog:post_list')
	else:
		form = RegistrationForm()
	return render(request, 'accounts/register.html', {'form': form})


@require_http_methods(["GET", "POST"])
def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			next_url = request.GET.get('next') or reverse_lazy('blog:post_list')
			return redirect(next_url)
	else:
		form = LoginForm(request)
	return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
	logout(request)
	return redirect('blog:post_list')
