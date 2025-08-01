Text Editor Web App using Django
A simple Django-based web application that takes input text and applies various text-processing functions such as removing punctuation, converting to uppercase, removing newlines, etc.

Features:
Remove Punctuation
Convert to UPPERCASE
Remove Newlines
Remove Extra Spaces
Count Characters

Tech Stack:
Backend: Django (Python)
Frontend: HTML, CSS (with Django templates)
Tools: Python string manipulation, basic regex

How to Run the Project:-
Clone the repository:
git clone https://github.com/yourusername/django-text-editor.git
cd django-text-editor

Create and activate virtual environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Install required packages:
pip install -r requirements.txt

Run migrations (not strictly needed for this project):
python manage.py migrate

Start the development server:
python manage.py runserver
