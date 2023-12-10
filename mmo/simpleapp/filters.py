from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter
from .models import Post,Response

class PostFilter(FilterSet):
    dateCreation_filter = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
        }


class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = [
            'res_post'
        ]

    def __init__(self, *args, **kwargs):
        super(ResponseFilter, self).__init__(*args, **kwargs)
        self.filters['res_post'].queryset = Post.objects.filter(to_reg_user_id=self.request)