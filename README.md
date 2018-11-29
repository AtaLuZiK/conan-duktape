# conan-duktape

Conan package for [duktape](https://github.com/svaarala/duktape)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/conan-community).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/duktape%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/duktape%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-duktape.svg?branch=release%2F2.3.0)](https://travis-ci.org/AtaLuZiK/conan-duktape)|[![Build status](https://ci.appveyor.com/api/projects/status/j91vmmobhfvi97od/branch/release/2.3.0?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-duktape/branch/release/2.3.0)|

## Reuse the packages

### Basic setup

```
conan install duktape/2.3.0@zimmerk/stable
```

### Project setup

```
[requires]
duktape/2.3.0@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
