import setuptools

with open("README.txt", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name='CloneFinderAPI',
    version="0.1",

    author='Sayaka Miura',
    author_email='tuf78332@temple.edu',

    description='Estimate clone genotypes and frequencies within a tumor sample using a phylogenetic approach.',
    long_description=long_description,
    long_description_content_type='text/plain',
    url='https://github.com/gstecher/CloneFinderAPI',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        ],

    python_requires='>=3',
    install_requires=['numpy', 'scipy', 'biopython'],
    packages = setuptools.find_packages(),

    entry_points = {
        'console_scripts' : [
            'clonefinder = clonefinder.clonefinder:clonefinder',
            ],
        },
    )
