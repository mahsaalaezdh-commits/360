from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.core.mail import mail_admins
from django.conf import settings

from .forms import ConsultationForm
from .models import ConsultationRequest


@require_http_methods(["GET", "POST"])
def consultation_view(request):
	"""Public consultation form. Saves submission to DB and emails site admins."""
	if request.method == 'POST':
		form = ConsultationForm(request.POST)
		if form.is_valid():
			consult = form.save(commit=False)
			# capture IP if available
			ip = request.META.get('REMOTE_ADDR')
			consult.ip_address = ip
			consult.save()

			# send email to site admins (uses ADMINS in settings)
			subject = f"درخواست مشاوره از {consult.name}"
			message_lines = [
				f"نام: {consult.name}",
				f"ایمیل: {consult.email}",
				f"تلفن: {consult.phone}",
				"",
				"پیام:",
				consult.message,
				"",
				f"زمان: {consult.created_at}",
				f"IP: {consult.ip_address}",
			]
			message = "\n".join(message_lines)
			try:
				mail_admins(subject, message, fail_silently=False)
			except Exception:
				# don't break user flow if email fails; admin can find submission in DB
				pass

			# Optionally redirect to a thank-you page or show a success message
			return render(request, 'consulation/consultation_thanks.html', {'consult': consult})
	else:
		form = ConsultationForm()

	return render(request, 'consulation/consultation_form.html', {'form': form})
