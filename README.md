# API de Tareas - Django REST Framework

Este proyecto es una API RESTful construida con Django y Django REST Framework para gestionar tareas (ToDo List). Incluye autenticación mediante tokens JWT, paginación, filtros, pruebas unitarias y relaciones entre modelos.

## 🔧 Tecnologías utilizadas

- Python 3.12
- Django 5.x
- Django REST Framework
- SimpleJWT
- django-filter
- Postman (para pruebas de endpoints)
- Git y GitHub

## 🚀 Características

- CRUD completo para tareas.
- Autenticación JWT (login y protección de rutas).
- Relación entre usuarios y tareas.
- Filtros por estado de completado y búsqueda por título.
- Paginación de resultados.
- Pruebas unitarias para verificación de seguridad y creación.
- Documentación del uso de endpoints con ejemplos en Postman.

## 📂 Estructura principal

apiproject/
├── apiproject/ # Configuración de Django
├── tareas/ # App principal con modelos, vistas y tests
├── manage.py
├── requirements.txt
└── README.md

## ✅ Endpoints disponibles

| Método | Endpoint              | Descripción                    |
|--------|------------------------|--------------------------------|
| POST   | /api/token/            | Obtener token JWT              |
| POST   | /api/token/refresh/    | Refrescar token                |
| GET    | /api/tareas/           | Listar tareas                  |
| POST   | /api/tareas/           | Crear nueva tarea              |
| GET    | /api/tareas/?search=x  | Buscar por título              |
| GET    | /api/tareas/?completada=true | Filtrar tareas completadas     |

## 🧪 Pruebas

- Verifica que un usuario autenticado puede crear una tarea.
- Verifica que un usuario no autenticado no puede crear tareas.

## 🔐 Autenticación

Utiliza tokens JWT proporcionados por SimpleJWT. Para autenticarte en Postman:
1. Realiza un `POST` a `/api/token/` con usuario y contraseña.
2. Copia el `access` token recibido.
3. En cada solicitud protegida, agrega un header:

## 💻 Cómo ejecutar

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
