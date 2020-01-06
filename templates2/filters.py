import django_filters


from game.models import Characters


class CharacterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Characters
        fields = ['name', 'status', 'species','origin']