import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from django_testing.students.models import Course, Student


def test_example():
    assert False, "Just test example"

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory




@pytest.mark.django_db
def test_first_course(api_client, course_factory):
    courses = course_factory(_quantity = 10)

    response = api_client.get('/courses/')
    data = response.json

    assert response.status_code == 200
    assert courses[0].id == data.get('id')
    assert courses[0].name == data.get('name')


@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    courses = course_factory(_quantity = 10)

    response = api_client.get('/courses/')
    data = response.json

    assert response.status_code == 200
    assert len(courses) == len(data) 


@pytest.mark.django_db
def test_filtering_courses_id(api_client, course_factory):
    courses = course_factory(_quantity = 10)

    response = api_client.get('/courses/', {'id': courses[3].id})
    data = response.json

    assert response.status_code == 200
    assert courses[3].id == data[0].id[3].id


@pytest.mark.django_db
def test_filtering_courses_name(api_client, course_factory):
    courses = course_factory(_quantity = 10)

    response = api_client.get('/courses/', {'name': courses[3].name})
    data = response.json

    assert response.status_code == 200
    assert courses[3].name  == data[0].name 

@pytest.mark.django_db
def test_successful_course_creation(api_client):

    response = api_client.post('/courses/', data = {'name': 'IT'})
    data = response.json

    assert response.status_code == 201
    assert data['name']  == 'IT'
    
 
@pytest.mark.django_db
def test_successful_course_update(api_client, course_factory):
    courses = course_factory(_quantity = 10)

    response = api_client.patch('/courses/', data = {'id':2, 'name': 'Mathematics'})
    data = response.json

    assert response.status_code == 200
    assert courses[2].name  == 'Mathematics' 

@pytest.mark.django_db
def test_successful_course_deletion(api_client, course_factory):
    courses = course_factory(_quantity = 10)
        
    response = api_client.delete('/courses/', data = {'name': courses[6].name})
    data = response.json

    assert response.status_code == 204
    assert len(courses[6].name) == 0

