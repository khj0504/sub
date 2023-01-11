from setuptools import setup

package_name = 'test123'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hakjun',
    maintainer_email='khj@robotis.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_publisher = test123.hello_publisher:main',
            'hello_subscriber = test123.hello_subscriber:main',
        ],
    },
)
