# Personal Website

A personal website built with Django, featuring a blog, portfolio, and internationalization support.

## 🚀 Local Development Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
```bash
git clone https://github.com/haxybaxy/website_template.git
cd website_template
```

2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```


4. Run database migrations
```bash
python manage.py migrate
```

5. Create a superuser (admin) there is already an admin user with user: admin and password: 1234
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

The site should now be running at `http://127.0.0.1:8000/`
You should be able to access the admin portal to add items at http://127.0.0.1:8000/admin