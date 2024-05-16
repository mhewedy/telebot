# This Python file uses the following encoding: utf-8

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import and use built-in open()
from io import open as io_open
from os import path

from setuptools import setup

summary = "Telegram bot library abstraction on top of python-telegram-bot"
project_homepage = "https://github.com/mhewedy/telebot"
here = path.abspath(path.dirname(__file__))


def readall(*args):
    with io_open(path.join(here, *args), encoding="utf-8") as fp:
        return fp.read()


with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

documentation = readall("README.md")
# metadata = dict(
#     re.findall(r"""__([a-z]+)__ = "([^"]+)""", readall("instapy", "__init__.py"))
# )
metadata = {"version": "0.0.2"}

setup(
    name="telebot",
    version=metadata["version"],
    description=summary,
    long_description=documentation,
    long_description_content_type="text/markdown",
    author="mohammad hewedy",
    author_email="mhewedy@gmail.com",
    maintainer="mhewedy at Github",
    license="Apache2",
    url=project_homepage,
    download_url=(project_homepage + "/archive/master.zip"),
    project_urls={
        "How Tos": (project_homepage + "/tree/master/docs"),
        "Examples": (project_homepage + "/tree/master/quickstart_templates"),
        "Bug Reports": (project_homepage + "/issues"),
        "Source": (project_homepage + "/tree/master/telebot"),
    },
    packages=["telebot"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Programming Language :: SQL",
        "Topic :: Utilities",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: English",
    ],
    install_requires=dependencies,
    python_requires=">=3.5",
    platforms=["win32", "linux", "linux2", "darwin"],
    zip_safe=False,
    entry_points={"console_scripts": []},
)