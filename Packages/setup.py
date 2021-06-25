from setuptools import setup,find_packages

setup(
        name = 'Veda',
        version = '0.1',
        packages = find_packages(),
        author = 'shihua',
        description = 'Veda Module',
        install_requires = ['ansible','clickhouse-driver'],
        entry_points = {
            'console_scripts': [
                'vedainit = Veda.scripts.cli_init:vedainit',
                'vedactl = Veda.scripts.cli:veda'
            ]
        }      
)