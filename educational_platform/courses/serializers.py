from rest_framework import serializers


from courses.models.course import Course
from courses.models.lecture import Lecture
from courses.models.task import Task
from courses.models.homework import Homework
from courses.models.rating import Rating
from courses.models.comment import Comment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'teachers', 'students', 'lectures']


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'topic', 'attachments', 'author']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'topic', 'description', 'lecture']


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ['id', 'task', 'student', 'attachment', 'progress']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'value', 'homework']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'rating', 'text']
