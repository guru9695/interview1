
from rest_framework import serializers 
from testapp.models import detail
 
 
class detailSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = detail
        fields = ('id',
                  'name',
                  'usernamedata',
                  'price',
                  'type'
                  )
                  
                  