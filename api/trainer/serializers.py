from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Trainer
from api.user.models import CustomUser

class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    # email= serializers.SerializerMethodField()
    # role = serializers.SerializerMethodField()

    # def get_role(self, obj):
    #     return obj.email.get_role_display()  # Assuming 'role' is in CustomUser

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        
        instance.save()
        return instance

    class Meta:
         model = Trainer
         fields = ['email', 'name', 'password', 'gender', 'dob', 'contact_no', 'state', 'domain','password',]
         extra_kwargs = {'password': {'write_only': True}}

       