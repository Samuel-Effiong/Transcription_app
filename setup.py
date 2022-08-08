from cx_Freeze import setup, Executable
from setuptools import find_packages, find_namespace_packages


# ADD FILES
files = ['icon.ico', 'themes/', 'ffmpeg_engine/', 
	 'Split Audios/', 'models/', 'settings.json']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico",
    shortcut_name = "GLH Transcriber"
)

exclude_files = [
    "tkinter"
]

build_exe_options = {
    "include_files": files,
    "excludes": exclude_files,
    "optimize": 1
}

# SETUP CX FREEZE
setup(
    name="PyDracula",
    version="1.0",
    description="GLH Audio Transcriber",
    author="Samuel Nkopuruk E.",
    options={'build_exe': build_exe_options},
    packages=find_packages(),
    executables=[target]
)
