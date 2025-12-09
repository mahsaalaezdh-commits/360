from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import BlogPost


class PostListView(ListView):
	"""Public list of published blog posts."""
	model = BlogPost
	template_name = 'blog/post_list.html'
	context_object_name = 'posts'
	paginate_by = 10

	def get_queryset(self):
		# Only show published posts to the public
		return BlogPost.objects.filter(status='published').order_by('-created_at')


class PostDetailView(DetailView):
	"""Detail view for a single blog post. Publicly visible only for published posts."""
	model = BlogPost
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'

	def get_object(self, queryset=None):
		obj = super().get_object(queryset=queryset)
		# Prevent viewing drafts via the public detail view
		if obj.status != 'published':
			raise Http404("Post not found")
		return obj



