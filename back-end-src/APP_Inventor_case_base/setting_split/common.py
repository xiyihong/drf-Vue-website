import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 限定请求中的host值,以防止黑客构造包来发送请求.只有在列表中的host才能访问
ALLOWED_HOSTS = ['*']

# 自定义用户验证模块（而不是默认的django.contrib.auth.models.User）
AUTH_USER_MODEL = 'users.UserProfile'

# 凡是涉及到数据库的类都需要在这里注册
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'cases.apps.CasesConfig',
    'questions.apps.CasesConfig',
    'user_operation.apps.UserOperationConfig',
    'crispy_forms',
    'django_filters',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'captcha',
    'favicon',
    'raven.contrib.django.raven_compat',
]

# 作用于全局的中间件，一个Request进来会从上到下调用各个中间件的process_request()方法，再传给具体的View，得到的Response从下到上调用各个中间件的process_response()方法
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 会话的存储机制使用数据库模式
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

'''
非Django原生setting项，仅用于corsheaders.middleware.CorsMiddleware
跨域增加忽略
'''
CORS_ORIGIN_ALLOW_ALL = True

# 在会话Cookie上使用HTTPOnly标志。如果设置为True，客户端JavaScript将无法访问会话Cookie
SESSION_COOKIE_HTTPONLY = True

# URL映射规则配置文件（也可以通过修改HttpRequest对象的urlconf属性）
ROOT_URLCONF = 'APP_Inventor_case_base.urls'

# 模板引擎的相关配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',   # 引擎后端，备选项还有'django.template.backends.jinja2.Jinja2'
        'DIRS': [os.path.join(BASE_DIR, 'templates')],      # 模板源文件存放目录列表（引擎会按顺序搜索符合规则的template源文件）
        'APP_DIRS': True,       # 是否会在installed_app里面搜索符合规则的template源文件
        'OPTIONS': {            # 传给引擎后端的额外参数（各后端之间的差异很大）
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Django的内建server（如manage.py runserver）所使用的WSGI应用对象的完整路径
WSGI_APPLICATION = 'APP_Inventor_case_base.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'zh-hans'  # 中文支持，django1.8以后支持；1.8以前是zh-cn
TIME_ZONE = 'Asia/Shanghai'     # 时区设置
USE_I18N = True     # 国际化(internationalization)又称为i18n(读法为i18n,据说是因为internationalization(国际化)这个单词从i到n之间有18个英文字母,i18n的名字由此而来).
USE_L10N = True     # 是 localization 的缩写形式，意即在 l 和 n 之间有 10 个字母，本意是指软件的“本地化”
USE_TZ = False   # 默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！

# 当需要验证一个用户的身份时，调用类的列表
AUTHENTICATION_BACKENDS = ('users.views.CustomBackend',)

# 搜索行为由STATICFILES_FINDERS这个列表来指定；如果含有FileSystemFinder，则会搜索STATICFILES_DIRS；如果含有AppDirectoriesFinder，则会搜索每个app的static子目录
# STATIC_URL：设置的static file的起始url，这个只是在template里边引用到
# 执行命令：python manage.py collectstatic 就可以方便的将所用到的app中的静态资源复制到同一目录（由STATIC_ROOT指定）
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# MEDIA_URL和STATIC_URL必须要有不同的取值，因为它专门用于存放用户上传的文件
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

'''
非Django原生setting项，仅用于REST-Framework-JWT
'''
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7), # 过期时间
    'JWT_AUTH_HEADER_PREFIX': 'JWT',    # 客户端回传TOKEN时，需要增加的前缀
}

'''
非Django原生setting项，仅用于REST-Framework-EXTENSIONS
'''
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 15 * 60,      # 设置缓存有效时间
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {  # Log to stdout
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'logs', 'django-logging.txt'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}