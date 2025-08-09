# microsoft_2025_platform/microsoft_2025_platform/settings.py

from pathlib import Path
import os 
import dj_database_url  # Importamos a biblioteca para gerenciar a URL do banco de dados

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/development/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Usa a SECRET_KEY de uma variável de ambiente se estiver em produção.
# Se não estiver disponível (durante o desenvolvimento local), usa a chave padrão.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-^sr*xib55=c#9c=jyc6j@*dzi=k%6!5g*b#)2mriqava7k1x)p')

# SECURITY WARNING: don't run with debug turned on in production!
# Define DEBUG como False em produção, exceto se a variável de ambiente DEBUG estiver definida.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS para produção. Render irá fornecer uma URL.
# Usaremos uma variável de ambiente para isso.
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
# Adicionamos 'localhost' e '127.0.0.1' para desenvolvimento local
ALLOWED_HOSTS += ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', # Adicione esta linha para registrar seu app 'core'
    'widget_tweaks', 
    'localflavor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'microsoft_2025_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Correção aqui: Aponte para a pasta 'templates' na RAIZ do projeto e também
        # para a pasta 'templates' dentro do seu app 'core'.
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'core' / 'templates', # <--- ADICIONE ESTA LINHA
        ], 
        'APP_DIRS': True, # Mantenha True para que o Django procure também em 'app_name/templates/'
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'microsoft_2025_platform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# A nova configuração de banco de dados usa uma variável de ambiente para o PostgreSQL
# E mantém o SQLite para desenvolvimento local.
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4, # Mínimo de 4 caracteres
        }
    },
    # Os validadores abaixo foram REMOVIDOS/COMENTADOS para permitir maior flexibilidade na senha:
    # {
    #    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'pt-br' # Altere para 'pt-br' para mensagens padrão do Django em português
# Se quiser mensagens de erro de validação de senha em português, o Django as traduzirá
# se você tiver os validadores padrão e o LANGUAGE_CODE estiver em 'pt-br'.
# Como removemos a maioria dos validadores, as mensagens virão do nosso forms.py ou das que restaram.

TIME_ZONE = 'Africa/Luanda' # Definindo o fuso horário para Luanda

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/topics/i18n/

STATIC_URL = '/static/' 

# ***** CORREÇÃO AQUI para STATICFILES_DIRS *****
# Onde o Django DEVE PROCURAR arquivos estáticos DURANTE O DESENVOLVIMENTO
# A pasta 'static' DEVE estar na raiz do projeto (ao lado de manage.py)
STATICFILES_DIRS = [
    BASE_DIR / "static", 
]

# Onde o Django DEVE COLETAR arquivos estáticos para DEPLOYMENT (produção)
# Rode 'python manage.py collectstatic' para que esta pasta seja preenchida.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Media files (user uploads)
MEDIA_URL = '/media/' # URL para servir arquivos de mídia
MEDIA_ROOT = BASE_DIR / 'media' # Diretório onde os arquivos de mídia serão armazenados

# Define o modelo de usuário personalizado
AUTH_USER_MODEL = 'core.CustomUser'

# Adições para URLs de login e redirecionamento
LOGIN_URL = '/login/' 
LOGIN_REDIRECT_URL = 'home' 
LOGOUT_REDIRECT_URL = 'login'


# Configuração adicional para o Render servir arquivos estáticos e de mídia
# Isso é crucial para o deployment no Render
# STATIC_ROOT já foi definido acima
if not DEBUG:
    # Use o WhiteNoise para servir arquivos estáticos e de mídia em produção
    # Adicione a biblioteca whitenoise em seu requirements.txt
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware', # Adiciona WhiteNoise para servir arquivos estáticos
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'