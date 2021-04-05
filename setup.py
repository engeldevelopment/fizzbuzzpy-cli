from setuptools import find_namespace_packages, setup


setup(
    name="fizzbuzz",
    version="1.0.0",
    author="Engel Pinto",
    description="FizzBuzz Kata.",
    author_email="engeljavierpinto@gmail.com",
    install_requires=["Click==7.1.2"],
    packages=find_namespace_packages(include="fizzbuzz"),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        fizzbuzz=fizzbuzz.scripts.fizzbuzz:fizzbuzz
    """,
)
