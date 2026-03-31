from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from it430 import models, serializers
from datetime import datetime
from it430.authentication_jwt import JWTAuthentication
import bcrypt

class ActivityView(APIView):
    def get(self, request):
        activities = models.Activity.objects.all()
        serializer = serializers.ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityIdView(APIView):
    def get(self, request, activity_id):
        try:
            activity = models.Activity.objects.get(activity_id=activity_id)
        except models.Activity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.ActivitySerializer(activity)
        return Response(serializer.data)

    def patch(self, request, activity_id):
        try:
            activity = models.Activity.objects.get(activity_id=activity_id)
        except models.Activity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.ActivitySerializer(activity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, activity_id):
        try:
            activity = models.Activity.objects.get(activity_id=activity_id)
        except models.Activity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActivityFamilyView(APIView):
    def get(self, request, family_id):
        activities = models.Activity.objects.filter(family_id=family_id)
        serializer = serializers.ActivitySerializer(activities, many=True)
        return Response(serializer.data)

class CustomerView(APIView):
    def get(self, request):
        customers = models.Customer.objects.all()
        serializer = serializers.CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request.data['created_on'] = str(datetime.now())
        request.data['is_active'] = True
        # hash password
        salt = bcrypt.gensalt()
        hashed_pass = (bcrypt.hashpw(request.data['password'].encode('utf-8'), salt)).decode('utf-8')
        print(hashed_pass)
        request.data['passhash'] = hashed_pass
        del request.data["password"]
        serializer = serializers.CustomerSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(
                        family=models.Family.objects.get(pk=request.data['family_id'])
                    )
                return Response(serializer.data)
            except IntegrityError as ie:
                return Response({'error': 'username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(type(e))
                return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CustomerIdView(APIView):
    def get(self, request, customer_id):
        try:
            customer = models.Customer.objects.get(customer_id=customer_id)
        except models.Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.CustomerSerializer(customer)
        return Response(serializer.data)

    def patch(self, request, customer_id):
        try:
            customer = models.Customer.objects.get(customer_id=customer_id)
        except models.Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id):
        try:
            customer = models.Customer.objects.get(customer_id=customer_id)
        except models.Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerFamilyView(APIView):
    def get(self, request, family_id):
        customers = models.Customer.objects.filter(family_id=family_id)
        serializer = serializers.CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class FamilyView(APIView):
    def get(self, request):
        families = models.Family.objects.all()
        serializer = serializers.FamilySerializer(families, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FamilyIdView(APIView):
    def get(self, request, family_id):
        try:
            family = models.Family.objects.get(family_id=family_id)
        except models.Family.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.FamilySerializer(family)
        return Response(serializer.data)

    def patch(self, request, family_id):
        try:
            family = models.Family.objects.get(family_id=family_id)
        except models.Family.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.FamilySerializer(family, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, family_id):
        try:
            family = models.Family.objects.get(family_id=family_id)
        except models.Family.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        family.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GoalView(APIView):
    def get(self, request):
        goals = models.Goal.objects.all()
        serializer = serializers.GoalSerializer(goals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoalIdView(APIView):
    def get(self, request, goal_id):
        try:
            goal = models.Goal.objects.get(goal_id=goal_id)
        except models.Goal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.GoalSerializer(goal)
        return Response(serializer.data)

    def patch(self, request, goal_id):
        try:
            goal = models.Goal.objects.get(goal_id=goal_id)
        except models.Goal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.GoalSerializer(goal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, goal_id):
        try:
            goal = models.Goal.objects.get(goal_id=goal_id)
        except models.Goal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GoalFamilyView(APIView):
    def get(self, request, family_id):
        goals = models.Goal.objects.filter(family_id=family_id)
        serializer = serializers.GoalSerializer(goals, many=True)
        return Response(serializer.data)

class GoalFamilyGoalTypeView(APIView):
    def get(self, request, family_id, goal_type_id):
        goals = models.Goal.objects.filter(family_id=family_id, goal_type_id=goal_type_id)
        serializer = serializers.GoalSerializer(goals, many=True)
        return Response(serializer.data)

class GoalCustomerView(APIView):
    def get(self, request, customer_id):
        goals = models.Goal.objects.filter(created_by_id=customer_id)
        serializer = serializers.GoalSerializer(goals, many=True)
        return Response(serializer.data)

class GoalCustomerGoalTypeView(APIView):
    def get(self, request, customer_id, goal_type_id):
        goals = models.Goal.objects.filter(created_by_id=customer_id, goal_type_id=goal_type_id)
        serializer = serializers.GoalSerializer(goals, many=True)
        return Response(serializer.data)

class GoalTypeView(APIView):
    def get(self, request):
        goal_types = models.GoalType.objects.all()
        serializer = serializers.GoalTypeSerializer(goal_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.GoalTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoalTypeIdView(APIView):
    def get(self, request, goal_type_id):
        try:
            goal_type = models.GoalType.objects.get(goal_type_id=goal_type_id)
        except models.GoalType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.GoalTypeSerializer(goal_type)
        return Response(serializer.data)

    def patch(self, request, goal_type_id):
        try:
            goal_type = models.GoalType.objects.get(goal_type_id=goal_type_id)
        except models.GoalType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.GoalTypeSerializer(goal_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, goal_type_id):
        try:
            goal_type = models.GoalType.objects.get(goal_type_id=goal_type_id)
        except models.GoalType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        goal_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PriorityView(APIView):
    def get(self, request):
        priorities = models.Priority.objects.all()
        serializer = serializers.PrioritySerializer(priorities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.PrioritySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriorityIdView(APIView):
    def get(self, request, priority_id):
        try:
            priority = models.Priority.objects.get(priority_id=priority_id)
        except models.Priority.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.PrioritySerializer(priority)
        return Response(serializer.data)

    def patch(self, request, priority_id):
        try:
            priority = models.Priority.objects.get(priority_id=priority_id)
        except models.Priority.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.PrioritySerializer(priority, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, priority_id):
        try:
            priority = models.Priority.objects.get(priority_id=priority_id)
        except models.Priority.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        priority.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PriorityFamilyView(APIView):
    def get(self, request, family_id):
        priorities = models.Priority.objects.filter(family_id=family_id)
        serializer = serializers.PrioritySerializer(priorities, many=True)
        return Response(serializer.data)

class TaskView(APIView):
    def get(self, request):
        tasks = models.Task.objects.all()
        serializer = serializers.TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskIdView(APIView):
    def get(self, request, task_id):
        try:
            task = models.Task.objects.get(task_id=task_id)
        except models.Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.TaskSerializer(task)
        return Response(serializer.data)

    def patch(self, request, task_id):
        try:
            task = models.Task.objects.get(task_id=task_id)
        except models.Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        try:
            task = models.Task.objects.get(task_id=task_id)
        except models.Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskFamilyView(APIView):
    def get(self, request, family_id):
        tasks = models.Task.objects.filter(family_id=family_id)
        serializer = serializers.TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskAssignedToView(APIView):
    def get(self, request, customer_id):
        tasks = models.Task.objects.filter(assigned_to=customer_id)
        serializer = serializers.TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({'success': False,
                             'error': 'Username and Password must have a value'},
                             status = status.HTTP_400_BAD_REQUEST)

        check_user = models.Customer.objects.filter(username=username).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'Customer with this username does not exist'},
                             status=status.HTTP_404_NOT_FOUND)
        existing_user = models.Customer.objects.filter(username=username).values()[0]
        print(password.encode('utf-8'))
        if bcrypt.checkpw(password.encode('utf-8'), existing_user['passhash'].encode('utf-8')):
            # print("Password matches")
            user = models.Customer.objects.get(username=username)

            # add last login to Customer table
            serializer = serializers.CustomerSerializer(user, data={'last_login': str(datetime.now())}, partial=True)
            if serializer.is_valid():
                serializer.save()

            if user is not None:
                jwt_token = JWTAuthentication.create_jwt(user=user)
                data = {
                    'token': jwt_token
                }
                return Response({'success': True,
                                'token': jwt_token},
                                status=status.HTTP_200_OK)
            else:
                return Response({'success': False,
                                'error': 'Invalid Login Credentials'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            # print("Password does not match")
            return Response({'success': False,
                            'error': 'Incorrect password for user'},
                            status=status.HTTP_401_UNAUTHORIZED)

class EmployeeLogin(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({'success': False,
                             'error': 'Username and Password must have a value'},
                             status = status.HTTP_400_BAD_REQUEST)

        check_user = models.Customer.objects.filter(username=username).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'Customer with this username does not exist'},
                             status=status.HTTP_404_NOT_FOUND)
        existing_user = models.Customer.objects.filter(username=username).values()[0]
        print(password.encode('utf-8'))
        if bcrypt.checkpw(password.encode('utf-8'), existing_user['passhash'].encode('utf-8')):
            # print("Password matches")
            user = models.Customer.objects.get(username=username)

            # add last login to Customer table
            serializer = serializers.CustomerSerializer(user, data={'last_login': str(datetime.now())}, partial=True)
            if serializer.is_valid():
                serializer.save()

            if user is not None:
                jwt_token = JWTAuthentication.create_jwt(user=user)
                data = {
                    'token': jwt_token
                }
                return Response({'success': True,
                                'token': jwt_token},
                                status=status.HTTP_200_OK)
            else:
                return Response({'success': False,
                                'error': 'Invalid Login Credentials'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            # print("Password does not match")
            return Response({'success': False,
                            'error': 'Incorrect password for user'},
                            status=status.HTTP_401_UNAUTHORIZED)