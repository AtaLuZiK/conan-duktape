import os
import shutil

from conans import CMake, ConanFile, tools


class DuktapeConan(ConanFile):
    name = "duktape"
    version = "2.3.0"
    license = "MIT"
    author = "k000 zimmerk@live.com"
    url = "https://github.com/AtaLuZiK/conan-duktape"
    description = "embeddable Javascript engine with a focus on portability and compact footprint"
    topics = ("Javascript", "embeddable")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports_sources = "CMakeLists.txt", "duktape-config.cmake", "duk_config.h.shared", "duk_config.h.static"
    generators = "cmake"

    @property
    def zip_folder_name(self):
        return "duktape-" + self.version

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        zip_name = self.zip_folder_name + ".tar.xz"
        tools.download("https://duktape.org/%s" % zip_name, zip_name)
        tools.check_md5(zip_name, "352105b39979fc766bbd0b3721e8c2b5")
        tools.unzip(zip_name)
        os.unlink(zip_name)

        if self.options.shared:
            config_file = "duk_config.h.shared"
        else:
            config_file = "duk_config.h.static"
        shutil.move(config_file, "%s/src/duk_config.h" % self.zip_folder_name)
        shutil.move("CMakeLists.txt", "%s/CMakeLists.txt" % self.zip_folder_name)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.zip_folder_name)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="%s/src" % self.zip_folder_name)
        self.copy("duktape.lib", dst="lib", src="lib")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.exe", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", src="lib")
        self.copy("*.dylib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["duktape"]
