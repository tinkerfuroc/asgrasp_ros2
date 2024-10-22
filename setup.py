from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'asgrasp_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (os.path.join('share', package_name, 'checkpoints'), glob('asgrasp_ros2/contact_graspnet_pytorch/checkpoints/**/**/*.*', recursive=True)),
    ] + [
        (os.path.join('share', package_name, filename[47: filename.rfind('/')]), [filename])
        for filename in glob('asgrasp_ros2/contact_graspnet_pytorch/checkpoints/**/**/*.*', recursive=True)
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tinker',
    maintainer_email='queenxy2002@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'graspnet = asgrasp_ros2.contact_graspnet:main',
            'test = asgrasp_ros2.test:main',
            'demo = asgrasp_ros2.grasp_demo:main',
            'grasp_service = asgrasp_ros2.grasp_service:main',
        ],
    },
)
