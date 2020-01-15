import sys
from cx_Freeze import setup, Executable
build_exe_options = {"packages": ["os", "numpy"], "excludes": ["tkinter"], "include_files":["images"]}
base = None
setup( name = "MacGyver",
    version = "0.1",
    description = "Mac Gyver game",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py")])