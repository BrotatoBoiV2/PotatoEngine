from setuptools import setup, find_packages

setup(
    name="PotatoEngine",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.6.1"
    ],
    author="Aaron Cassell",
    description="A flexible game engine created with pygame",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta"
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Games/Entertainment :: Arcade",
        "Topic :: Software Development :: Libraries :: pygame",
        "License :: OSI Approved :: MIT License"
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.7',
)