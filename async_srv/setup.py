import pathlib
from  setuptools import setup, find_packages

BASE_DIR = pathlib.Path(__file__).parent.absolute() #абсалютный путь

def get_version():
    with open(BASE_DIR/"VERSION") as file:
        return file.readline().strip() # путь для чтения версии из Version.txt

def get_licence():
    with open(BASE_DIR/"LICENCE") as file:
        return file.readline().strip()


def get_desc():
    with open(BASE_DIR/"README.md") as file:
        return file.readline().strip()

def get_packages():
    with open(BASE_DIR/"requirements.txt") as file:
        return [
            package.strip
            for package in file
            if package or not package.startswith("#")
        ]

setup(
    name = "asrv",
    version = "0.1.1",
    author = "OLeg",
    author_email="admin@google.com",
    #url = "https://doc.site.com"  обычно url репозитория
    packages = find_packages(".",include=["asrv","asrv.*"],exclude=["*tests*.py,*tests*"]),  #указываем откуда устанавливать модуль, фаилы которые игнорируются
    package_dir = {"asrv.*": "asrv"},
    include_package_data = True,
    license = get_licence(),
    description = "Описание",
    long_description = "text/markdown",
    install_requeres = ["lib","lib3==1.5"],
    python_requeres = ">=3.11",
    classifiers = [
        "Development Status :: 3 - Alpha"
        if "dev" in get_version()
        else "Development Status :: 4 Beta"
        if "rc" in get_version()
        else "Development Status :: 5 Production/Stable"
    ],
    entry_points = {
        "console_scripts": ["asrv_runner = asrv.app:run"]
    }



)