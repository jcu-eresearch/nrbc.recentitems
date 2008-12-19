from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='nrbc.portlet.recentitems',
      version=version,
      description="A customised portlet which only shows recent changes that are local to the given folderish type",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone portlet recent items changes',
      author='David Breitkreutz',
      author_email='david.breitkreutz@jcu.edu.au',
      url='http://eresearch.jcu.edu.au/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['nrbc', 'nrbc.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
