import pytest

from courses.models.course import Course
from courses.models.lecture import Lecture
from courses.models.task import Task
from users.models import User


@pytest.mark.django_db
class TestEducationalPlatform:
    """
        Test CRUD operations + authorization based on the following models:
        - Task
        - Lecture
        - Course
        - User
    """

    def setup(self):
        """
            add initial data
        """
        self.credentials = {
            'username': 'test_user',
            'password': '12345678',
            'email': 'test@test.com'
        }
        self.course = Course.objects.create(name='test_course')
        User.objects.create_superuser(**self.credentials)
        self.teacher = User.objects.create(username='derek_teacherson', password='qwerty', role='teacher')
        self.lecture = Lecture.objects.create(topic='New topic', author_id=self.teacher.id)
        task_data = {
            'topic': 'New topic',
            'description': 'New description',
            'lecture': self.lecture,
        }
        self.task = Task.objects.create(**task_data)

    def test_course_detail(self, client):
        """
            test successful getting of course object detail
        """
        response = client.post('/api/token/',
                               {'username': self.credentials['username'], 'password': self.credentials['password']})
        token = 'JWT ' + response.data.get('access')
        result = client.get('/api/course/', {'pk': self.course.id}, HTTP_AUTHORIZATION=token)
        assert result.status_code == 200
        course_dict = result.json()
        fields = ['id', 'name', 'teachers', 'students', 'lectures']
        article_keys = list(course_dict[0].keys())
        assert fields == article_keys

    def test_course_detail_error(self, client):
        """
            test details for non-existing course
        """
        response = client.post('/api/token/',
                               {'username': self.credentials['username'], 'password': self.credentials['password']})
        token = 'JWT ' + response.data.get('access')
        invalid_course_id = 123456789
        result = client.get(f'/api/course/{invalid_course_id}/', {}, HTTP_AUTHORIZATION=token)
        assert result.status_code == 404

    def test_course_detail_unauthorized(self, client):
        """
            test authorization
        """

        result = client.get('/api/course/', {'pk': self.course.id})
        assert result.status_code == 401

    def test_create_lecture_detail(self, client):
        """
            test lecture object creation
        """

        response = client.post('/api/token/',
                               {'username': self.credentials['username'], 'password': self.credentials['password']})
        token = 'JWT ' + response.data.get('access')
        data = {'topic': 'Test topic'}
        result = client.post('/api/lecture/', data, HTTP_AUTHORIZATION=token)
        assert result.status_code == 201

    def test_create_invalid_lecture(self, client):
        """
            test invalid lecture object creation
        """
        response = client.post('/api/token/',
                               {'username': self.credentials['username'], 'password': self.credentials['password']})
        token = 'JWT ' + response.data.get('access')
        data = {'topic': 3,
                'author': 12413489137491308}
        result = client.post('/api/lecture/', data, HTTP_AUTHORIZATION=token)
        assert result.status_code == 400

    def test_update_course_detail(self, client):
        """
            test course object update
        """
        response = client.post('/api/token/',
                               {'username': self.credentials['username'], 'password': self.credentials['password']})
        token = 'JWT ' + response.data.get('access')
        new_course = Course.objects.create(name='Name')
        new_name = 'New course title'
        result = client.put(f'/api/course/{new_course.id}/', {'name': new_name},
                            HTTP_AUTHORIZATION=token,
                            content_type='application/json')
        assert result.status_code == 200
        assert result.data.get('name') == new_name

    def test_update_task_detail_invalid(self, client):
        """
            test invalid task object update
        """

        response = client.post('/api/token/',
                               {'username': self.credentials['username'], 'password': self.credentials['password']})
        token = 'JWT ' + response.data.get('access')

        result = client.put(f'/api/task/{self.task.id}/', {'lecture': 'invalid_number'},
                            HTTP_AUTHORIZATION=token,
                            content_type='application/json')
        assert result.status_code == 400

    def test_delete_lecture_detail(self, client):
        """
            test lecture object deletion + checking task object deletion
        """

        response = client.post('/api/token/',
                               {'username': self.credentials['username'], 'password': self.credentials['password']})
        token = 'JWT ' + response.data.get('access')

        lecture_id = self.lecture.id
        result_lecture_deletion = client.delete(f'/api/lecture/{lecture_id}/', {}, HTTP_AUTHORIZATION=token)
        result_lecture_list = client.get('/api/lecture/', {}, HTTP_AUTHORIZATION=token).data
        result_task_list = client.get('/api/task/', {}, HTTP_AUTHORIZATION=token).data

        assert result_lecture_deletion.status_code == 204
        assert len(result_lecture_list) == 0
        assert len(result_task_list) == 0
