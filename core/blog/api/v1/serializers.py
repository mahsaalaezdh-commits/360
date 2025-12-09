from rest_framework import serializers

from ...models import BlogPost

class BlogPostSerializers(serializers.ModelSerializer):
    relative_url = serializers.URLField(source='get_absolute_url', read_only=True)
    absolute_url = serializers.HyperlinkedIdentityField(view_name='blog:api-v1:post-detail', lookup_field='pk')
    category = serializers.SlugRelatedField(many=False, slug_field='name', read_only=True)
    class Meta:
        model = BlogPost
        fields = "__all__"


