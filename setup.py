from setuptools import find_packages, setup

package_name = 'health_check_pkg'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools',
        'rclpy',
        'std_msgs',
        'diagnostic_msgs'
    ],
    zip_safe=True,
    maintainer='robot',
    maintainer_email='axba0001@ce.pucmm.edu.do',
    description='Paquete para gestionar y revisar la salud de las multiples Raspberry Pi',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'heartbeat_listener_node = health_check_pkg.heartbeat_listener:main',
            'heartbeat_publisher_node = health_check_pkg.heartbeat_publisher:main',
            'diagnostics_publisher_node = health_check_pkg.diagnostics_publisher:main',
        ],
    },
)
