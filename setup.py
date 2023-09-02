from setuptools import setup
import os
from glob import glob
package_name = 'kilobot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'scripts.publisher', 'scripts.subscriber'
        ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'meshes'),glob('meshes/*')),
        (os.path.join('share',package_name,'launch'),glob('launch/*')),
        (os.path.join('share',package_name,'urdf'),glob('urdf/*')),
        (os.path.join('share',package_name,'worlds'),glob('worlds/*')),
        (os.path.join('share',package_name,'data'),glob('data/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='claudiofreddi',
    maintainer_email='me@claudiofreddi.eu',
    description='kilobot',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'cmdVel_to_pwm_node = scripts.cmd_to_pwm_driver:main',
                'publisher_node = scripts.publisher:main'
                #'subscriber_node = vision_rpi_bot.subscriber:main',
                #'qr_maze_solve_node = vision_rpi_bot.qr_maze_drive:main',
                #'line_following_sim_node = vision_rpi_bot.line_following_sim:main',
                #'line_following_real_node = vision_rpi_bot.line_following_real:main',
                #'surveillance_node = vision_rpi_bot.surveillance_bot:main',
                           ],
                }
)
