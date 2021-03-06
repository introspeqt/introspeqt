try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'introspeqt',
    'description': 'Simple introspector for PySide applications.',
    'author': 'David Martinez',
    'author_email': 'david.martinez.anim@gmail.com',
    'url': 'https://github.com/davidmartinezanim/introspeqt',
    'version': '0.0.2',
    'packages': ['introspeqt'],
    'install_requires': ['PySide', ],
    'scripts': []
}

setup(**config)
