DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sopds',
        'HOST': 'localhost',
        'USER': 'sopds',
        'PASSWORD' : 'sopds',
        'OPTIONS' : {
            'init_command': "SET default_storage_engine=MyISAM;\
                             SET sql_mode='';"
        }
    }
}
