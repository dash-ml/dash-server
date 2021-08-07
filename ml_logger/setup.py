from os import path
from setuptools import setup

with open(path.join(path.abspath(path.dirname(__file__)), 'README'), encoding='utf-8') as f:
    long_description = f.read()
with open(path.join(path.abspath(path.dirname(__file__)), 'VERSION'), encoding='utf-8') as f:
    version = f.read()

setup(name="ml_logger",
      description="A Simple and Scalable Logging Utility With a Beautiful Visualization Dashboard",
      long_description=long_description,
      version=version,
      url="https://github.com/episodeyang/ml_logger",
      author="Ge Yang",
      author_email="yangge1987@gmail.com",
      license=None,
      keywords=["ml_logger", "visualization", "logging", "debug", "debugging"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "Programming Language :: Python :: 3"
      ],
      packages=[
          "ml_logger",
          "ml_logger.caches",
          "ml_logger.helpers",  # ml_dash is now in a different package
      ],
      install_requires=[
          "boto3",
          "cloudpickle==1.3.0",
          "dill",
          "imageio",
          "imageio-ffmpeg",
          "matplotlib",
          "more-itertools",
          "numpy",
          "pillow",
          "params-proto",
          "pycurl",
          "numpy",
          "requests",
          "requests-futures",
          "requests-toolbelt",
          "ruamel.yaml",
          "sanic",
          "sanic-cors",
          "scipy",
          "termcolor",
          "typing",
          "urllib3",
      ])
