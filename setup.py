from setuptools import find_packages, setup

setup(name='grpc-framework',
      version='1.0.0',
      description='Django gRPC Framework',
      author='Comynli',
      author_email='comynli@magedu',
      url='https://github.com/magedu/grpc-framework/',
      packages=find_packages(),
      include_package_data=True,
      install_requires=["django>=3.1", "grpcio>=1.32", "grpcio-tools>=1.32"],
      python_requires=">=3.8",
      license='Apache-2.0'
      )
