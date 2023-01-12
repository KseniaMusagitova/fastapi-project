from setuptools import setup

setup(
    name='app-example',
    version='0.0.1',
    author='Ksenia M',
    author_email='kseniamusagitova@gmail.com',
    description='FastApi app',
    install_requires=[
        'fastapi==0.89.1',
        'uvicorn==0.20.0',
        'SQLAlchemy==1.4.46',
        'pytest==7.2.0',
        'requests==2.28.1'
    ],
    scripts=['app/main.py']

)