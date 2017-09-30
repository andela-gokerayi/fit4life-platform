from rest_framework import serializers
from menu_list.models import Menu


class MenuSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Menu
        fields = ('benefit', 'id', 'created', 'name')
        extra_kwargs = {
            'url': {
                'view_name': 'menu:menu-detail',
            }
        }