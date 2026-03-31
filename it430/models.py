# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_description = models.CharField(max_length=200)
    is_active = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    family = models.ForeignKey('Family', models.DO_NOTHING)
    created_by = models.ForeignKey('Customer', models.DO_NOTHING, db_column='created_by')

    class Meta:
        managed = False
        db_table = 'activity'

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    username = models.CharField(unique=True, max_length=30)
    email = models.CharField(max_length=40, blank=True, null=True)
    passhash = models.CharField(max_length=150, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    family = models.ForeignKey('Family', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'customer'

class Family(models.Model):
    family_id = models.AutoField(primary_key=True)
    family_name = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'family'


class Goal(models.Model):
    goal_id = models.AutoField(primary_key=True)
    goal_description = models.CharField(max_length=200)
    is_active = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    goal_type = models.ForeignKey('GoalType', models.DO_NOTHING)
    family = models.ForeignKey(Family, models.DO_NOTHING)
    created_by = models.ForeignKey(Customer, models.DO_NOTHING, db_column='created_by')

    class Meta:
        managed = False
        db_table = 'goal'


class GoalType(models.Model):
    goal_type_id = models.AutoField(primary_key=True)
    goal_type_description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'goal_type'


class Priority(models.Model):
    priority_id = models.AutoField(primary_key=True)
    priority_description = models.CharField(max_length=50)
    weight = models.IntegerField()
    is_active = models.BooleanField(blank=True, null=True)
    family = models.ForeignKey(Family, models.DO_NOTHING)
    created_by = models.ForeignKey(Customer, models.DO_NOTHING, db_column='created_by')

    class Meta:
        managed = False
        db_table = 'priority'


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_description = models.CharField(max_length=200)
    is_active = models.BooleanField(blank=True, null=True)
    is_completed = models.BooleanField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completion_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    family = models.ForeignKey(Family, models.DO_NOTHING)
    created_by = models.ForeignKey(Customer, models.DO_NOTHING, db_column='created_by')
    assigned_to = models.ForeignKey(Customer, models.DO_NOTHING, db_column='assigned_to', related_name='task_assigned_to_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'
