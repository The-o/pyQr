from setuptools import setup
setup(
    name='pyQr',
    version='0.2.0',
    description='QR-codes scanner and generator',
    url='https://github.com/The-o/pyQr',
    author='Pavel Yashchenko',
    author_email='pavel.yashchenko@shtormtech.ru',
    license='MIT',
    packages=[],
    install_requires=[
        'wxPython', 'pyzbar', 'qrcode', 'pyperclip'
    ],
    scripts = ['pyQr']
)