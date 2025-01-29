# Django Task Manager

A web-based task management application built with Django. This project provides user authentication and task management features, allowing users to efficiently track and manage their tasks.

## Features
- **User Authentication:** Secure user login, registration, and logout functionalities.
- **Task Management:** Add, edit, update, and delete tasks.
- **Media Support:** Upload and manage task-related screenshots and user profile images.
- **Responsive Design:** A clean and responsive user interface using custom CSS.
- **Database Support:** Includes postgresql for development and can be extended for other databases.


## Technologies Used
- **Backend:** Django Framework
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** postgresql

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Django 4.x
- Pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django_task_manager.git
   cd django_task_manager
   ```
2. Install dependencies:

  ```bash
  pip install -r requirements.txt
```
3. Apply migrations:
  ```bash
  python manage.py migrate
```
4. Run the server:

```bash
  python manage.py runserver
```

## Folder Structure
- **Authenticateapp:** User authentication logic (views, forms, models).
- **taskmanager:** Task management logic.
- **templates:** HTML templates for pages.
- **static:** CSS and image files.
- **media:** Uploaded files like screenshots and user images.

