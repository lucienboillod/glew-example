#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake
import os


class ExampleConan(ConanFile):
    name = "glew-example"
    version = "0.1.0"
    license = "MIT"
    exports_sources = ["CMakeLists.txt", "example.cc"]
    generators = 'cmake'
    settings = "os", "arch", "compiler", "build_type"
    requires = "glew/2.1.0@bincrafters/stable"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.env_info.PATH = os.path.join(self.package_folder, "bin")
