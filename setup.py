from setuptools import setup, find_packages


def load_requires_from_file(filepath):
    return [pkg_name.rstrip('\r\n') for pkg_name in open(filepath).readlines()]

exclude_packages = ['server/tests', 'client/tests']

TEST_REQUIREMENTS = [
    'pytest',
    'pytest-runner'
]
TEST_PATHS = ['server/tests', 'client/tests']

setup(name='autoRecorder',
      version='0.0.1',
      description='Automatic playing of recorder project',
      packages=find_packages(exclude=exclude_packages),
      setup_requires=['pytest-runner'],
      tests_require=TEST_REQUIREMENTS,
      entry_points="""
        [console_scripts]
        ARclient = client.main:main
        ARserver = server.main:main
        """,
      )
