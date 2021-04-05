from setuptools import find_packages, setup

setup(
    name="demo",
    use_scm_version=False,
    version="0.0.1",
    setup_requires=["setuptools_scm", "pytest-runner"],
    tests_require=["pytest"],
    include_package_data=True,
    packages=find_packages(exclude=["tests", "tests/*"]),
    description="Demo Flask App",
    author="Victor Ng",
    author_email="victor@draper.ai",
    license="MPL 2.0",
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
    ],
    zip_safe=False,
)
