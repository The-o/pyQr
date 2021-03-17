from setuptools import setup
setup(
    name='pyQr',
    version='0.1.0',
    description='QR-codes scanner and generator',
    url='https://github.com/The-o/pyQr',
    author='Pavel Yashchenko',
    author_email='pave.yashchenko@shtormtech.ru',
    license='MIT',
    packages=[],
    install_requires=[
        'wxPython', 'pyzbar', 'qrcode'
    ],
    scripts =['pyQr']
)