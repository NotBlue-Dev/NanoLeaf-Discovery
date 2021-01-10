from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='NanoLeafDiscovery',
  version='0.0.3',
  description='Discovery module for nanoleaf',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='NotBlue',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='nanoleaf',
  packages=find_packages(),
  install_requires=['requests', 'socket'] 
)