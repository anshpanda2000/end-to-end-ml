from typing import List

from setuptools import find_packages, setup


def get_requirements(file_path: str) -> List[str]:
    """
    This function gets the required Libraries
    from requirement.txt

    """
    install_requires = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("_"):
                install_requires.append(line)

    return install_requires


setup(
    name="my_project",
    version="0.1",
    author="Anshuman Panda",
    author_email="anshpanda2000@gmail.com.com",
    description="A sample Python project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
