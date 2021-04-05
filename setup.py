from setuptools import find_namespace_packages, setup


setup(
    name="fizzbuzz",
    version="1.0.0",
    author="Engel Pinto",
    install_requires=["Click"],
    packages=find_namespace_packages(include="fizzbuzz"),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        fizzbuzz=fizzbuzz.scripts.fizzbuzz:fizzbuzz
    """,
)
