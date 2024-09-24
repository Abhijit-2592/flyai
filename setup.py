import os

import setuptools

classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
]

with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as f:
    install_requires = f.readlines()
    print("The following packages will be installed")
    print(install_requires)

package_name = "flyai"

print(f"Building package {package_name}")

setuptools.setup(
    name=package_name,
    version="0.1",
    author="Abhijit Balaji",
    author_email="abhijitbalaji48@gmail.com",
    description="Make AI Models Go BRRRRR........",
    include_package_data=True,
    packages=setuptools.find_packages(exclude=["tests*"]),
    classifiers=classifiers,
    install_requires=install_requires,
    python_requires=">=3.10",
)
