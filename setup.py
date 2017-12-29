import os
import shutil
import glob
import distutils.cmd
import distutils.log
import setuptools
import subprocess

class NuitkaClean(distutils.cmd.Command):
    user_options = []
    description = ""
    def initialize_options(self):
        return
    def finalize_options(self):
        return
    def run(self):
        self.announce("Removing recent build of the ops tool")
        for d in ['main.build', 'main.dist', 'bin']:
            shutil.rmtree(d)

class NuitkaBuild(distutils.cmd.Command):
    user_options = []
    description = ""
    def initialize_options(self):
        return
    def run(self):
        command = ['scons']
        self.announce("Building ops binary", level=distutils.log.INFO)
        subprocess.check_call(command)
        os.mkdir('bin')
        shutil.copy("main.dist/main.exe", "bin/bund")
        for file in glob.glob(r"main.dist/*.so"):
            shutil.copy(file, "bin")
    def finalize_options(self):
        return

        
setuptools.setup(
   cmdclass={
      'build': NuitkaBuild,
      'clean': NuitkaClean
   }
)
