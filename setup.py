from setuptools import setup, find_packages

setup(
    name="veracodetocsv",
    version="2018.10.3",
    packages=find_packages(),
    license="MIT",
    author="ctcampbell",
    url="https://github.com/ctcampbell/veracode-to-csv",
    author_email="chris@ctcampbell.com",
    description="Outputs one CSV file per scan per application profile visible in a Veracode platform account",
    install_requires=[
        "requests >= 2.18.4",
        "pytz >= 2018.4",
        "python-dateutil >= 2.7.3"
    ],
    entry_points={
        "console_scripts": ["veracodetocsv = veracodetocsv.veracodetocsv:run"]
    }
)