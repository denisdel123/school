from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materialsApp.models import Course, Lesson
from usersApp.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@mail.ru', is_superuser=True)
        self.client.force_authenticate(self.user)
        self.course = Course.objects.create(name='Python develop', owner=self.user)
        self.lesson = Lesson.objects.create(name='OOP', owner=self.user)

    def test_course_retrieve(self):
        url = reverse('materialsApp:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEquals(
            data.get('name'), self.course.name
        )

    def test_course_create(self):
        url = reverse('materialsApp:course-list')
        data = {
            "name": "English",
        }
        response = self.client.post(url, data)

        self.assertEquals(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEquals(
            data.get('name'), 'English'
        )

    def test_course_list(self):
        url = reverse('materialsApp:course-list')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "num_lesson": 0,
                    "lesson": [],
                    "name": self.course.name,
                    "description": self.course.description,
                    "image": self.course.image,
                    "owner": self.user.pk
                }
            ]
        }

        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )

        self.assertGreaterEqual(
            len(response.data), 1
        )

        self.assertEquals(
            data, result
        )

    def test_course_update(self):
        url = reverse("materialsApp:course-detail", args=(self.course.pk,))
        data = {
            "name": "English"
        }

        response = self.client.put(url, data, format='json')

        data = response.json()
        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEquals(
            data.get("name"), "English"
        )

    def test_course_delete(self):
        url = reverse('materialsApp:course-detail', args=(self.course.pk,))
        response = self.client.delete(url)

        self.assertEquals(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

        self.assertEquals(
            Course.objects.all().count(), 0
        )


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@mail.ru')
        self.client.force_authenticate(self.user)
        self.course = Course.objects.create(name='Python develop', owner=self.user)
        self.lesson = Lesson.objects.create(name='OOP', owner=self.user)

    def test_lesson_create(self):
        url = reverse('materialsApp:lesson_create')

        data = {
            "name": "Python 1",
            "owner": self.user.pk
        }
        response = self.client.post(url, data, format="json")

        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEquals(
            data.get("name"), "Python 1"
        )

    def test_lesson_update(self):
        url = reverse('materialsApp:lesson_update', args=(self.lesson.pk,))

        date = {
            "name": "English",
        }

        response = self.client.patch(url, date, format="json")

        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )

        response_data = response.json()

        self.assertEquals(
            response_data.get("name"), "English"
        )

    def test_lesson_list(self):
        url = reverse("materialsApp:lesson_list")

        response = self.client.get(url)

        data2 = [
            {
                'id': 8,
                'url_to_video': None,
                'name': 'OOP',
                'description': None,
                'image': None,
                'course': None,
                'owner': 8
            }
        ]

        data_response = response.json()

        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEquals(
            data_response, data2
        )

    def test_lesson_retriever(self):
        url = reverse('materialsApp:lesson_detail', args=(self.lesson.pk,))

        response = self.client.get(url)

        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )
        data = {'id': self.lesson.pk,
                'url_to_video': self.lesson.url_to_video,
                'name': self.lesson.name,
                'description': self.lesson.description,
                'image': self.lesson.image,
                'course': self.lesson.course,
                'owner': self.lesson.owner.pk
                }
        response_data = response.json()

        self.assertEquals(
            response_data, data
        )

    def test_lesson_delete(self):
        url = reverse('materialsApp:lesson_destroy', args=(self.lesson.pk,))

        response = self.client.delete(url)

        self.assertEquals(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

        self.assertEquals(
            Lesson.objects.all().count(), 0
        )
