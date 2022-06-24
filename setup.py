from os import path
from setuptools import setup, find_packages

cwd = path.dirname(__file__)
with open(path.join(cwd, 'README'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(cwd, 'VERSION'), encoding='utf-8') as f:
    version = f.read()

setup(name="ml-dash",
      description="A Beautiful Visualization Dashboard For Machine Learning",
      long_description=long_description,
      version=version,
      url="https://github.com/dash-ml/dash-server",
      author="Ge Yang",
      author_email="ge.ike.yang@gmail.com",
      license=None,
      keywords=["ml_logger",
                "ml-logger",
                "ml dash",
                "ml-dash",
                "ml_dash",
                "dashboard",
                "machine learning",
                "vis_server",
                "logging",
                "debug",
                "debugging"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "Programming Language :: Python :: 3"
      ],
      packages=[p for p in find_packages() if p != "tests"],
      include_package_data=True,
      install_requires=[
          "cloudpickle==1.3.0",
          'dill',
          "graphene==2.1.3",
          "graphql-core==2.1",
          "graphql-relay==0.4.5",
          "graphql-server-core==1.1.1",
          "multidict==4.6.1",
          "numpy",
          'pandas',
          "params_proto",
          "requests",
          "requests_futures",
          'ruamel.yaml',
          'sanic',
          'sanic-cors',
          'Sanic-GraphQL',
          "termcolor",
          "typing"
      ])
