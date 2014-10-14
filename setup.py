from glob import glob
from distutils.core import setup
import py2exe
import sys

data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

setup(console=['main.py'], data_files=data_files)
