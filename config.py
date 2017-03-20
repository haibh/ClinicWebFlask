# Define the application directory
import os

# Statement for enabling the development environment
DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'clinic.db')

# SQLALCHEMY_BINDS = {
#     'patient':        'sqlite:///' + os.path.join(BASE_DIR, 'patient.db'),
#     'medicine':        'sqlite:///' + os.path.join(BASE_DIR, 'medicine.db'),
#     'diagnostic':        'sqlite:///' + os.path.join(BASE_DIR, 'diagnostic.db'),
#     'treatment':      'sqlite:///' + os.path.join(BASE_DIR, 'treatment.db')
# }

SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')

DATABASE_CONNECT_OPTIONS = {}

SQLALCHEMY_TRACK_MODIFICATIONS = 'TRUE'

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "23rsdafsdf23eadfsadfsadfsadf2rdsfdxcvxcv"
