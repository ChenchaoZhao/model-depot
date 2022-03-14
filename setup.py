from setuptools import find_packages, setup
from torchvision_extra import __version__

# load readme
with open("README.md", "r") as f:
    long_description = f.read()


def load_requirements():
    with open("requirements.txt", "r") as f:
        r = [name.split()[0] for name in f.readlines() if not name.startswith("#")]
    return r


setup(
    name="modeldepot",
    version=__version__,
    author="Chenchao Zhao",
    author_email="chenchao.zhao@gmail.com",
    description="Common neural network components.",
    packages=find_packages(exclude=["tests"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=load_requirements(),
    license="MIT",
)
