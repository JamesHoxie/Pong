import cx_Freeze

executables = [cx_Freeze.Executable("pong.py")]

cx_Freeze.setup(
	name="Python Pong",
	options={"build.exe": {"packages": ["pygame"]}},
	executables = executables
	)