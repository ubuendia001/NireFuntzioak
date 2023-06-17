from setuptools import setup

setup(
    name='NireFuntzioak',
    version='1.0',
    description='Este es un paquete con funciones útiles para el análisis de datos',
    author='Urko Buendia',
    author_email='urkobuendia@hotmail.com',
    url='https://github.com/ubuendia001/NireFuntzioak.git',
    packages=['Nire funtzioak'],
    install_requires=[
        'pandas',
        'numpy',
        'sqlite3',
        'pyodbc',
        'python-docx',
        'docxtpl',
        'matplotlib',
        'scikit-learn',
        'requests',
        'pywin32',
        'smtplib',
        'email',
        'setuptools'
    ],
)

