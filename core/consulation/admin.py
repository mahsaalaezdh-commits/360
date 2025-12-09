from django.contrib import admin
from .models import ConsultationRequest


@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'created_at')
	search_fields = ('name', 'email', 'phone', 'message')
	readonly_fields = ('created_at', 'ip_address')
