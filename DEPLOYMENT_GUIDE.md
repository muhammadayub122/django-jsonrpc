# Django Deployment Guide for PythonAnywhere

## 1. Upload Your Code
- Upload your project files to PythonAnywhere
- Create a virtual environment: `python3 -m venv venv`
- Activate it: `source venv/bin/activate`

## 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## 3. Database Setup
- Go to PythonAnywhere > Databases
- Create a MySQL database
- Update your .env file with database credentials

## 4. Environment Variables
Create/update your .env file with production settings:
```
SECRET_KEY=your-secure-secret-key
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
CORS_ALLOWED_ORIGINS=https://yourusername.pythonanywhere.com
DB_ENGINE=django.db.backends.mysql
DB_NAME=yourusername$dbname
DB_USER=yourusername
DB_PASSWORD=your_mysql_password
DB_HOST=yourusername.mysql.pythonanywhere-services.com
```

## 5. Run Migrations
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

## 6. Configure Web App
- Go to PythonAnywhere > Web
- Set up a new web app
- Point to your WSGI file: `yourprojectname/pythonanywhere_wsgi.py`
- Set static files directory to: `/home/yourusername/yourprojectname/staticfiles`
- Reload the web app

## 7. Common Issues
- **500 Error**: Check your WSGI configuration and .env file
- **Static files not loading**: Ensure STATIC_ROOT is set correctly
- **Database connection**: Verify MySQL credentials
- **CORS issues**: Check ALLOWED_HOSTS and CORS settings

## 8. Troubleshooting
- Check logs in PythonAnywhere > Web > Error log
- Test locally with production settings first
- Ensure all environment variables are set correctly