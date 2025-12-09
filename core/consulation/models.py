from django.db import models
from django.utils import timezone


class ConsultationRequest(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	phone = models.CharField(max_length=50, blank=True, null=True)
	message = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	ip_address = models.GenericIPAddressField(blank=True, null=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"Consultation from {self.name} <{self.email}> at {self.created_at:%Y-%m-%d %H:%M}"
