from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Tarea

class TareaAPITestCase(APITestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(username='jorge', password='test1234')
        self.url = '/api/tareas/'
        self.data = {
            'titulo': 'Tarea de prueba',
            'descripcion': 'Creada por prueba',
            'completada': False
        }

    def autenticar_usuario(self):
        refresh = RefreshToken.for_user(self.usuario)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

    def test_usuario_autenticado_puede_crear_tarea(self):
        self.autenticar_usuario()
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarea.objects.count(), 1)
        self.assertEqual(Tarea.objects.get().titulo, 'Tarea de prueba')

    def test_usuario_no_autenticado_no_puede_crear_tarea(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
