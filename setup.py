from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='ckanext-dcat_ap_no',
    version=version,
    description="Norwegian DCAP AP profile to be used with CKAN and the dcat plugin",
    long_description='''\
    ''',
    classifiers=[],
    keywords='',
    author='Erling Børresen',
    author_email='erling.borresen@gmail.com',
    url='https://github.com/vegvesen/ckanext-dcat_ap_no',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
    [ckan.rdf.profiles]
    norwegian_dcat_ap=ckanext.dcat_ap_no.profiles:NorwegianDCATAPProfile
    ''',
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    },
)
