from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as f:
    long_desc = f.read()

setup(
    name='encodeC',
    description='Tons of basic text manipulation',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    version='5.0.0',
    url='https://github.com/kingsiddhu/encodec',
    author='Siddharth Katabathula',
    author_email='help.siddhu@gmail.com',
    license='MIT',
    keywords='text',
    packages=find_packages(),
    include_package_data=True,
    #install_requires=[],
    python_requires='>=3.6',
)
