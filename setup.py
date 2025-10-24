import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.1"

REPO_NAME = "TEXT-summarizer-project"
AUTHOR_USER_NAME = "rajeevkush1"
SRC_REPO = "MyProject"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),)