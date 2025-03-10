from setuptools import find_packages, setup
import glob
import os

package_name = 'tcebot_sim'

data_files = [
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/configs', glob.glob('configs/*')),
        ('share/' + package_name + '/launch', glob.glob('launch/*')),
        ('share/' + package_name + '/worlds', glob.glob('worlds/*')),
]

# Recursively add all files inside the models directory
for root, dirs, files in os.walk('models'):
    for file in files:
        file_path = os.path.join(root, file)
        install_path = os.path.join('share', package_name, file_path)
        data_files.append((os.path.dirname(install_path), [file_path]))

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Dhanush M',
    maintainer_email='dhanushshettigar90@gmail.com',
    description='A ROS 2 package for simulating the tcebot robot in Gazebo, providing launch files, configurations, and predefined worlds.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
