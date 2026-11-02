# TaskHub

A small Django website where each user registers, logs in and manages their own tasks. Built step by step as a backend learning project.

## Features

- User registration, login and logout (Django built-in authentication)
- Dashboard with task statistics (total, completed, pending) and recent tasks
- Task manager with full CRUD: add, view, edit and delete
- Mark a task as done or undo it
- Each user sees only their own tasks (ownership check on every view)
- Flash messages after actions, with auto-hide after 3 seconds
- Custom frontend: sticky navbar with active link, cards, badges, styled forms, CSS Grid stat boxes
- CSS variables for easy theming

## Tech Stack

| Part | Technology |
|---|---|
| Backend | Python, Django |
| Database | SQLite |
| Frontend | HTML, CSS, a little JavaScript |
| Auth | `django.contrib.auth` |

## Project Structure

```
manage.py
auth/                 # project settings and main urls
auth_app/             # register, login, dashboard, logout
  templates/auth_app/
    layout/app.html   # base layout (navbar, messages, script)
    dashboard.html
    login.html
    register.html
tasks/                # task manager app
  models.py           # Task model
  forms.py            # TaskForm (ModelForm)
  views.py            # list, add, edit, delete, toggle
  urls.py
  templates/tasks/
static/
  css/style.css       # all styles, with CSS variables
```

## Pages and URLs

| Page | URL | Name |
|---|---|---|
| Login | `/login/` | `login` |
| Register | register page | `register` |
| Dashboard | dashboard page | `dashboard` |
| Task list | `/tasks/` | `task_list` |
| Add task | `/tasks/add/` | `add_task` |
| Edit task | `/tasks/<id>/edit/` | `edit_task` |
| Delete task | `/tasks/<id>/delete/` | `delete_task` |
| Toggle done | `/tasks/<id>/toggle/` (POST only) | `toggle_task` |

## How It Works

**Task model**

```python
class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

**Ownership check.** Edit, delete and toggle views fetch the task with the logged-in user, so another user's task returns a 404:

```python
task = get_object_or_404(Task, pk=pk, owner=request.user)
```

**Safe actions.** Toggle accepts only POST (`@require_POST`) and delete changes data only on POST, so a URL typed in the browser or a pre-loaded link can never change data. All forms use `{% csrf_token %}`.

**Template inheritance.** Every page extends `auth_app/layout/app.html`, which provides the navbar, the messages loop and the auto-hide script.

## Getting Started

1. Clone the repository and open the project folder.

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
```

3. Install Django:

```bash
pip install django
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Create an admin user (optional):

```bash
python manage.py createsuperuser
```

6. Start the server:

```bash
python manage.py runserver
```

7. Open `http://127.0.0.1:8000/` in your browser.

## What I Learned

- Django authentication: register, login, logout, `@login_required`
- Models, `ForeignKey` and the ORM (`filter`, `order_by`, slicing, `count`)
- `ModelForm` and `form.save(commit=False)`
- URL path converters such as `<int:pk>`
- GET vs POST and why data changes must use POST
- Django messages framework
- Template inheritance and static files
- CSS variables, flexbox and CSS Grid

## Roadmap

- Mobile hamburger menu
- Dark mode toggle
- Live task search
- Delete confirmation modal
- Task due dates and priorities
- Pagination
- Deployment

## Author

Saphal, BSc. CSIT student, learning Django backend development.