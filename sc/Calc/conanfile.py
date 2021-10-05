from conans import ConanFile, CMake
   
class Calc(ConanFile):
    name = "Calc"
    #version = "0.1"
    license="MIT"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/memsharded/conan-hello.git"

    def source(self):
        self.run("git clone https://github.com/memsharded/hello.git")

    def build(self):
        cmake = CMake(self)
        self.run('cd Calc && cmake . %s' % cmake.command_line)
        self.run("cd Calc && cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="Calc")
        self.copy("*.lib", dst="lib", src="Calc/lib")
        self.copy("*.a", dst="lib", src="Calc/lib")

    def package_info(self):
        self.cpp_info.libs = ["Calc"]
