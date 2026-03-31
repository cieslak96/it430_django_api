from rest_framework import serializers
from it430 import models

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        depth = 2
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        depth = 2
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Family
        depth = 2
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Goal
        depth = 2
        fields = '__all__'

class GoalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GoalType
        fields = '__all__'

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Priority
        depth = 2
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        depth = 2
        fields = '__all__'