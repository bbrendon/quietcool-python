from setuptools import setup

setup(name='quietcool',
      version='0.1',
      description='QuietCool Fan Library',
      url='https://github.com/bbrendon/quietcool-python',
      author='David Stone',
      author_email='david@stabbylambda.com',
      license='ASL',
      packages=['quietcool'],
      install_requires=[
          'aiocoap==0.4.7',
      ],
      zip_safe=False,
      )
