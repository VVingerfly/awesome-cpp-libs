# Awesome Cpp Libs

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> An awesome & curated list of cpp libraries for **CV/CGers**.

-----

## Table of Contents

- [Cpp](#cpp)
  - [Base Libraries](#base-libraries)
  - [Command Line Parser](#command-line-parser)
  - [Logging](#logging)
  - [Profiler](#profiler)
  - [Format String](#format-string)
  - [Testing](#testing)
  - [Serialization](#serialization)
  - [GUI](#gui)
  - [Visualization](#visualization)
  - [GPU](#gpu)
  - [Utility](#utility)
- [Math](#math)
  - [Linear Algebra](#linear-algebra)
  - [Optimization](#optimization)
  - [Automatic Differentiation](#automatic-differentiation)
  - [Statistics](#statistics)
- [CV](#cv)
  - [Image Processing](#image-processing)
  - [Structure from Motion](#structure-from-motion)
  - [Multi-View Reconstruction](#multi-view-reconstruction)
- [CG](#cg)
  - [Geometry Processing](#geometry-processing)
  - [PointCloud Processing](#pointcloud-processing)
  - [Visualization](#visualization)
  - [Triangulation](#triangulation)
  - [Texture&Atlas](#texture&atlas)
  - [Transformation](#transformation)
  - [Registration](#registration)
  - [Nearest Neighbors](#nearest-neighbors)
  - [Collision](#collision)
  - [Rendering](#rendering)
  - [Animation](#animation)
  - [Simulation](#simulation)
  - [Modeling](#modeling)
  - [Others](#others)

-----
## Cpp

### Base Libraries

#### [stb](https://github.com/nothings/stb)
[![Stars](https://img.shields.io/github/stars/nothings/stb)](Stars) [![Forks](https://img.shields.io/github/forks/nothings/stb)](Forks) [![Watchers](https://img.shields.io/github/watchers/nothings/stb)](Watchers) [![License](https://img.shields.io/github/license/nothings/stb)](LICENSE)

single-file public domain (or MIT licensed) libraries for C/C++

#### [abseil-cpp](https://github.com/abseil/abseil-cpp)
[![Stars](https://img.shields.io/github/stars/abseil/abseil-cpp)](Stars) [![Forks](https://img.shields.io/github/forks/abseil/abseil-cpp)](Forks) [![Watchers](https://img.shields.io/github/watchers/abseil/abseil-cpp)](Watchers) [![License](https://img.shields.io/github/license/abseil/abseil-cpp)](LICENSE)

Abseil is an open-source collection of C++ code (compliant to C++11) designed to augment the C++ standard library.

### Command Line Parser

#### [cxxopts](https://github.com/jarro2783/cxxopts)
[![Stars](https://img.shields.io/github/stars/jarro2783/cxxopts)](Stars) [![Forks](https://img.shields.io/github/forks/jarro2783/cxxopts)](Forks) [![Watchers](https://img.shields.io/github/watchers/jarro2783/cxxopts)](Watchers) [![License](https://img.shields.io/github/license/jarro2783/cxxopts)](LICENSE)

Lightweight C++ command line option parser.

### Logging

#### [spdlog](https://github.com/gabime/spdlog)
[![Stars](https://img.shields.io/github/stars/gabime/spdlog)](Stars) [![Forks](https://img.shields.io/github/forks/gabime/spdlog)](Forks) [![Watchers](https://img.shields.io/github/watchers/gabime/spdlog)](Watchers) [![License](https://img.shields.io/github/license/gabime/spdlog)](LICENSE)

spdlog is a very fast, header-only/compiled, C++ logging library.

#### [plog](https://github.com/SergiusTheBest/plog)
[![Stars](https://img.shields.io/github/stars/SergiusTheBest/plog)](Stars) [![Forks](https://img.shields.io/github/forks/SergiusTheBest/plog)](Forks) [![Watchers](https://img.shields.io/github/watchers/SergiusTheBest/plog)](Watchers) [![License](https://img.shields.io/github/license/SergiusTheBest/plog)](LICENSE)

plog is a portable, simple and extensible C++ logging library, pretty powerful logging library in about 1000 lines of code.

#### [loguru](https://github.com/emilk/loguru)
[![Stars](https://img.shields.io/github/stars/emilk/loguru)](Stars) [![Forks](https://img.shields.io/github/forks/emilk/loguru)](Forks) [![Watchers](https://img.shields.io/github/watchers/emilk/loguru)](Watchers) [![License](https://img.shields.io/github/license/emilk/loguru)](LICENSE)

loguru is a lightweight and flexible C++ logging library.

### Profiler

#### [easy_profiler](https://github.com/yse/easy_profiler)
[![Stars](https://img.shields.io/github/stars/yse/easy_profiler)](Stars) [![Forks](https://img.shields.io/github/forks/yse/easy_profiler)](Forks) [![Watchers](https://img.shields.io/github/watchers/yse/easy_profiler)](Watchers) [![License](https://img.shields.io/github/license/yse/easy_profiler)](LICENSE)

easy_profiler is lightweight cross-platform profiler library for C++.

#### [microprofile](https://github.com/jonasmr/microprofile)
[![Stars](https://img.shields.io/github/stars/jonasmr/microprofile)](Stars) [![Forks](https://img.shields.io/github/forks/jonasmr/microprofile)](Forks) [![Watchers](https://img.shields.io/github/watchers/jonasmr/microprofile)](Watchers) [![License](https://img.shields.io/github/license/jonasmr/microprofile)](LICENSE)

Microprofile is a embeddable profiler in a few files, written in C++

#### [Remotery](https://github.com/Celtoys/Remotery)
[![Stars](https://img.shields.io/github/stars/Celtoys/Remotery)](Stars) [![Forks](https://img.shields.io/github/forks/Celtoys/Remotery)](Forks) [![Watchers](https://img.shields.io/github/watchers/Celtoys/Remotery)](Watchers) [![License](https://img.shields.io/github/license/Celtoys/Remotery)](LICENSE)

Remotery is a realtime CPU/GPU profiler hosted in a single C file with a viewer that runs in a web browser.

### Format String

#### [fmt](https://github.com/fmtlib/fmt)
[![Stars](https://img.shields.io/github/stars/fmtlib/fmt)](Stars) [![Forks](https://img.shields.io/github/forks/fmtlib/fmt)](Forks) [![Watchers](https://img.shields.io/github/watchers/fmtlib/fmt)](Watchers) [![License](https://img.shields.io/github/license/fmtlib/fmt)](LICENSE)

{fmt} is an open-source formatting library for C++. It can be used as a safe and fast alternative to (s)printf and iostreams.

#### [tinyformat](https://github.com/c42f/tinyformat)
[![Stars](https://img.shields.io/github/stars/c42f/tinyformat)](Stars) [![Forks](https://img.shields.io/github/forks/c42f/tinyformat)](Forks) [![Watchers](https://img.shields.io/github/watchers/c42f/tinyformat)](Watchers) [![License](https://img.shields.io/github/license/c42f/tinyformat)](LICENSE)

tinyformat.h is a type safe printf replacement library in a single C++ header file.

### Testing

#### [Catch2](https://github.com/catchorg/Catch2)
[![Stars](https://img.shields.io/github/stars/catchorg/Catch2)](Stars) [![Forks](https://img.shields.io/github/forks/catchorg/Catch2)](Forks) [![Watchers](https://img.shields.io/github/watchers/catchorg/Catch2)](Watchers) [![License](https://img.shields.io/github/license/catchorg/Catch2)](LICENSE)

A modern, C++-native, header-only, test framework for unit-tests, TDD and BDD - using C++11, C++14, C++17 and later (or C++03 on the Catch1.x branch)

### Serialization

#### [cereal](https://github.com/USCiLab/cereal)
[![Stars](https://img.shields.io/github/stars/USCiLab/cereal)](Stars) [![Forks](https://img.shields.io/github/forks/USCiLab/cereal)](Forks) [![Watchers](https://img.shields.io/github/watchers/USCiLab/cereal)](Watchers) [![License](https://img.shields.io/github/license/USCiLab/cereal)](LICENSE)

cereal is a header-only C++11 serialization library. cereal takes arbitrary data types and reversibly turns them into different representations, such as compact binary encodings, XML, or JSON. cereal was designed to be fast, light-weight, and easy to extend - it has no external dependencies and can be easily bundled with other code or used standalone.

#### [json](https://github.com/nlohmann/json)
[![Stars](https://img.shields.io/github/stars/nlohmann/json)](Stars) [![Forks](https://img.shields.io/github/forks/nlohmann/json)](Forks) [![Watchers](https://img.shields.io/github/watchers/nlohmann/json)](Watchers) [![License](https://img.shields.io/github/license/nlohmann/json)](LICENSE)

JSON for Modern C++

#### [jsoncpp](https://github.com/open-source-parsers/jsoncpp)
[![Stars](https://img.shields.io/github/stars/open-source-parsers/jsoncpp)](Stars) [![Forks](https://img.shields.io/github/forks/open-source-parsers/jsoncpp)](Forks) [![Watchers](https://img.shields.io/github/watchers/open-source-parsers/jsoncpp)](Watchers) [![License](https://img.shields.io/github/license/open-source-parsers/jsoncpp)](LICENSE)

JsonCpp is a C++ library that allows manipulating JSON values, including serialization and deserialization to and from strings.

#### [rapidjson](https://github.com/Tencent/rapidjson)
[![Stars](https://img.shields.io/github/stars/Tencent/rapidjson)](Stars) [![Forks](https://img.shields.io/github/forks/Tencent/rapidjson)](Forks) [![Watchers](https://img.shields.io/github/watchers/Tencent/rapidjson)](Watchers) [![License](https://img.shields.io/github/license/Tencent/rapidjson)](LICENSE)

A fast JSON parser/generator for C++ with both SAX/DOM style API

### GUI

#### [imgui](https://github.com/ocornut/imgui)
[![Stars](https://img.shields.io/github/stars/ocornut/imgui)](Stars) [![Forks](https://img.shields.io/github/forks/ocornut/imgui)](Forks) [![Watchers](https://img.shields.io/github/watchers/ocornut/imgui)](Watchers) [![License](https://img.shields.io/github/license/ocornut/imgui)](LICENSE)

Dear ImGui is a bloat-free graphical user interface library for C++. It outputs optimized vertex buffers that you can render anytime in your 3D-pipeline enabled application. It is fast, portable, renderer agnostic and self-contained (no external dependencies).

#### [nanogui](https://github.com/wjakob/nanogui)
[![Stars](https://img.shields.io/github/stars/wjakob/nanogui)](Stars) [![Forks](https://img.shields.io/github/forks/wjakob/nanogui)](Forks) [![Watchers](https://img.shields.io/github/watchers/wjakob/nanogui)](Watchers) [![License](https://img.shields.io/github/license/wjakob/nanogui)](LICENSE)

NanoGUI is a minimalistic cross-platform widget library for OpenGL 3.x or higher. It supports automatic layout generation, stateful C++11 lambdas callbacks, a variety of useful widget types and Retina-capable rendering on Apple devices thanks to NanoVG by Mikko Mononen. Python bindings of all functionality are provided using pybind11.

### Visualization

#### [matplotplusplus](https://github.com/alandefreitas/matplotplusplus)
[![Stars](https://img.shields.io/github/stars/alandefreitas/matplotplusplus)](Stars) [![Forks](https://img.shields.io/github/forks/alandefreitas/matplotplusplus)](Forks) [![Watchers](https://img.shields.io/github/watchers/alandefreitas/matplotplusplus)](Watchers) [![License](https://img.shields.io/github/license/alandefreitas/matplotplusplus)](LICENSE)

Matplot++: A C++ Graphics Library for Data Visualization.

#### [implot](https://github.com/epezent/implot)
[![Stars](https://img.shields.io/github/stars/epezent/implot)](Stars) [![Forks](https://img.shields.io/github/forks/epezent/implot)](Forks) [![Watchers](https://img.shields.io/github/watchers/epezent/implot)](Watchers) [![License](https://img.shields.io/github/license/epezent/implot)](LICENSE)

ImPlot is an immediate mode, GPU accelerated plotting library for Dear ImGui.

### GPU

#### [compute](https://github.com/boostorg/compute)
[![Stars](https://img.shields.io/github/stars/boostorg/compute)](Stars) [![Forks](https://img.shields.io/github/forks/boostorg/compute)](Forks) [![Watchers](https://img.shields.io/github/watchers/boostorg/compute)](Watchers) [![License](https://img.shields.io/github/license/boostorg/compute)](LICENSE)

A C++ GPU Computing Library for OpenCL

#### [vexcl](https://github.com/ddemidov/vexcl)
[![Stars](https://img.shields.io/github/stars/ddemidov/vexcl)](Stars) [![Forks](https://img.shields.io/github/forks/ddemidov/vexcl)](Forks) [![Watchers](https://img.shields.io/github/watchers/ddemidov/vexcl)](Watchers) [![License](https://img.shields.io/github/license/ddemidov/vexcl)](LICENSE)

VexCL is a C++ vector expression template library for OpenCL/CUDA/OpenMP

### Utility

#### [magic_enum](https://github.com/Neargye/magic_enum)
[![Stars](https://img.shields.io/github/stars/Neargye/magic_enum)](Stars) [![Forks](https://img.shields.io/github/forks/Neargye/magic_enum)](Forks) [![Watchers](https://img.shields.io/github/watchers/Neargye/magic_enum)](Watchers) [![License](https://img.shields.io/github/license/Neargye/magic_enum)](LICENSE)

Magic Enum C++ is a header-only C++17 library provides static reflection for enums, work with any enum type without any macro or boilerplate code.

## Math

### Linear Algebra

#### [Eigen](http://eigen.tuxfamily.org)

Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

#### [linalg](https://github.com/sgorsten/linalg)
[![Stars](https://img.shields.io/github/stars/sgorsten/linalg)](Stars) [![Forks](https://img.shields.io/github/forks/sgorsten/linalg)](Forks) [![Watchers](https://img.shields.io/github/watchers/sgorsten/linalg)](Watchers) [![License](https://img.shields.io/github/license/sgorsten/linalg)](LICENSE)

`linalg.h` is a single header, public domain, short vector math library for C++.

#### [NumCpp](https://github.com/dpilger26/NumCpp)
[![Stars](https://img.shields.io/github/stars/dpilger26/NumCpp)](Stars) [![Forks](https://img.shields.io/github/forks/dpilger26/NumCpp)](Forks) [![Watchers](https://img.shields.io/github/watchers/dpilger26/NumCpp)](Watchers) [![License](https://img.shields.io/github/license/dpilger26/NumCpp)](LICENSE)

NumCpp is a C++ implementation of the Python Numpy library.

### Optimization

#### [ceres-solver](https://github.com/ceres-solver/ceres-solver)
[![Stars](https://img.shields.io/github/stars/ceres-solver/ceres-solver)](Stars) [![Forks](https://img.shields.io/github/forks/ceres-solver/ceres-solver)](Forks) [![Watchers](https://img.shields.io/github/watchers/ceres-solver/ceres-solver)](Watchers) [![License](https://img.shields.io/github/license/ceres-solver/ceres-solver)](LICENSE)

Ceres Solver is an open source C++ library for modeling and solving large, complicated optimization problems. Ceres Solver can solve two kinds of problems.
- Non-linear Least Squares problems with bounds constraints.
- General unconstrained optimization problems.


#### [Ipopt](https://github.com/coin-or/Ipopt)
[![Stars](https://img.shields.io/github/stars/coin-or/Ipopt)](Stars) [![Forks](https://img.shields.io/github/forks/coin-or/Ipopt)](Forks) [![Watchers](https://img.shields.io/github/watchers/coin-or/Ipopt)](Watchers) [![License](https://img.shields.io/github/license/coin-or/Ipopt)](LICENSE)

Ipopt (Interior Point OPTimizer) is a software package for large-scale nonlinear optimization.

#### [NLopt](https://github.com/stevengj/nlopt)
[![Stars](https://img.shields.io/github/stars/stevengj/nlopt)](Stars) [![Forks](https://img.shields.io/github/forks/stevengj/nlopt)](Forks) [![Watchers](https://img.shields.io/github/watchers/stevengj/nlopt)](Watchers) [![License](https://img.shields.io/github/license/stevengj/nlopt)](LICENSE)

NLopt is a library for nonlinear local and global optimization, for functions with and without gradient information. It is designed as a simple, unified interface and packaging of several free/open-source nonlinear optimization libraries.

#### [AMGCL](https://github.com/ddemidov/amgcl)
[![Stars](https://img.shields.io/github/stars/ddemidov/amgcl)](Stars) [![Forks](https://img.shields.io/github/forks/ddemidov/amgcl)](Forks) [![Watchers](https://img.shields.io/github/watchers/ddemidov/amgcl)](Watchers) [![License](https://img.shields.io/github/license/ddemidov/amgcl)](LICENSE)

AMGCL is a header-only C++ library for solving large sparse linear systems with algebraic multigrid (AMG) method.

#### [optim](https://github.com/kthohr/optim)
[![Stars](https://img.shields.io/github/stars/kthohr/optim)](Stars) [![Forks](https://img.shields.io/github/forks/kthohr/optim)](Forks) [![Watchers](https://img.shields.io/github/watchers/kthohr/optim)](Watchers) [![License](https://img.shields.io/github/license/kthohr/optim)](LICENSE)

OptimLib is a lightweight C++ library of numerical optimization methods for nonlinear functions.

### Automatic Differentiation

#### [optim](https://github.com/autodiff/autodiff)
[![Stars](https://img.shields.io/github/stars/autodiff/autodiff)](Stars) [![Forks](https://img.shields.io/github/forks/autodiff/autodiff)](Forks) [![Watchers](https://img.shields.io/github/watchers/autodiff/autodiff)](Watchers) [![License](https://img.shields.io/github/license/autodiff/autodiff)](LICENSE)

autodiff is a C++17 library that uses modern and advanced programming techniques to enable automatic computation of derivatives in an efficient, easy, and intuitive way.

#### [FastAD](https://github.com/JamesYang007/FastAD)
[![Stars](https://img.shields.io/github/stars/JamesYang007/FastAD)](Stars) [![Forks](https://img.shields.io/github/forks/JamesYang007/FastAD)](Forks) [![Watchers](https://img.shields.io/github/watchers/JamesYang007/FastAD)](Watchers) [![License](https://img.shields.io/github/license/JamesYang007/FastAD)](LICENSE)

FastAD is a header-only C++ template library for automatic differentiation supporting both forward and reverse mode.

#### [clad](https://github.com/vgvassilev/clad)
[![Stars](https://img.shields.io/github/stars/vgvassilev/clad)](Stars) [![Forks](https://img.shields.io/github/forks/vgvassilev/clad)](Forks) [![Watchers](https://img.shields.io/github/watchers/vgvassilev/clad)](Watchers) [![License](https://img.shields.io/github/license/vgvassilev/clad)](LICENSE)

Clad is a source-transformation automatic differentiation (AD) library for C++, implemented as a plugin for the Clang compiler.

#### [Adept-2](https://github.com/rjhogan/Adept-2)
[![Stars](https://img.shields.io/github/stars/rjhogan/Adept-2)](Stars) [![Forks](https://img.shields.io/github/forks/rjhogan/Adept-2)](Forks) [![Watchers](https://img.shields.io/github/watchers/rjhogan/Adept-2)](Watchers) [![License](https://img.shields.io/github/license/rjhogan/Adept-2)](LICENSE)

Adept-2 is combined array and automatic differentiation library in C++.

### Statistics

#### [stats](https://github.com/kthohr/stats)
[![Stars](https://img.shields.io/github/stars/kthohr/stats)](Stars) [![Forks](https://img.shields.io/github/forks/kthohr/stats)](Forks) [![Watchers](https://img.shields.io/github/watchers/kthohr/stats)](Watchers) [![License](https://img.shields.io/github/license/kthohr/stats)](LICENSE)

StatsLib is a templated C++ library of statistical distribution functions, featuring unique compile-time computing capabilities and seamless integration with several popular linear algebra libraries.

## CV

### Image Processing

#### [OpenCV](https://github.com/opencv/opencv)
[![Stars](https://img.shields.io/github/stars/opencv/opencv)](Stars) [![Forks](https://img.shields.io/github/forks/opencv/opencv)](Forks) [![Watchers](https://img.shields.io/github/watchers/opencv/opencv)](Watchers) [![License](https://img.shields.io/github/license/opencv/opencv)](LICENSE)

Open Source Computer Vision Library.

#### [ccv](https://github.com/liuliu/ccv)
[![Stars](https://img.shields.io/github/stars/liuliu/ccv)](Stars) [![Forks](https://img.shields.io/github/forks/liuliu/ccv)](Forks) [![Watchers](https://img.shields.io/github/watchers/liuliu/ccv)](Watchers) [![License](https://img.shields.io/github/license/liuliu/ccv)](LICENSE)

C-based/Cached/Core Computer Vision Library, A Modern Computer Vision Library.

#### [CImg](https://github.com/dtschump/CImg)
[![Stars](https://img.shields.io/github/stars/dtschump/CImg)](Stars) [![Forks](https://img.shields.io/github/forks/dtschump/CImg)](Forks) [![Watchers](https://img.shields.io/github/watchers/dtschump/CImg)](Watchers) [![License](https://img.shields.io/github/license/dtschump/CImg)](LICENSE)

CImg Library is a small and open-source C++ toolkit for image processing.

#### [VLFeat](https://github.com/vlfeat/vlfeat)
[![Stars](https://img.shields.io/github/stars/vlfeat/vlfeat)](Stars) [![Forks](https://img.shields.io/github/forks/vlfeat/vlfeat)](Forks) [![Watchers](https://img.shields.io/github/watchers/vlfeat/vlfeat)](Watchers) [![License](https://img.shields.io/github/license/vlfeat/vlfeat)](LICENSE)

The VLFeat open source library implements popular computer vision algorithms specialising in image understanding and local featurexs extraction and matching.

### Structure from Motion

#### [TheiaSfM](https://github.com/sweeneychris/TheiaSfM)
[![Stars](https://img.shields.io/github/stars/sweeneychris/TheiaSfM)](Stars) [![Forks](https://img.shields.io/github/forks/sweeneychris/TheiaSfM)](Forks) [![Watchers](https://img.shields.io/github/watchers/sweeneychris/TheiaSfM)](Watchers) [![License](https://img.shields.io/github/license/sweeneychris/TheiaSfM)](LICENSE)

Theia is an open source library for multiview geometry and structure from motion. It is designed to be very efficient, scalable, and accurate. All steps of the pipeline are designed to be modular so that code is easy to read and easy to extend.

#### [COLMAP](https://github.com/colmap/colmap)
[![Stars](https://img.shields.io/github/stars/colmap/colmap)](Stars) [![Forks](https://img.shields.io/github/forks/colmap/colmap)](Forks) [![Watchers](https://img.shields.io/github/watchers/colmap/colmap)](Watchers) [![License](https://img.shields.io/github/license/colmap/colmap)](LICENSE)

COLMAP is a general-purpose Structure-from-Motion (SfM) and Multi-View Stereo (MVS) pipeline with a graphical and command-line interface. It offers a wide range of features for reconstruction of ordered and unordered image collections. The software is licensed under the new BSD license.

#### [bundler_sfm](https://github.com/snavely/bundler_sfm)
[![Stars](https://img.shields.io/github/stars/snavely/bundler_sfm)](Stars) [![Forks](https://img.shields.io/github/forks/snavely/bundler_sfm)](Forks) [![Watchers](https://img.shields.io/github/watchers/snavely/bundler_sfm)](Watchers) [![License](https://img.shields.io/github/license/snavely/bundler_sfm)](LICENSE)

Bundler Structure from Motion Toolkit

### Multi-View Reconstruction

#### [OpenMVG](https://github.com/openMVG/openMVG)
[![Stars](https://img.shields.io/github/stars/openMVG/openMVG)](Stars) [![Forks](https://img.shields.io/github/forks/openMVG/openMVG)](Forks) [![Watchers](https://img.shields.io/github/watchers/openMVG/openMVG)](Watchers) [![License](https://img.shields.io/github/license/openMVG/openMVG)](LICENSE)

OpenMVG (Multiple View Geometry) is a library for computer-vision scientists and especially targeted to the Multiple View Geometry community. It is designed to provide an easy access to the classical problem solvers in Multiple View Geometry and solve them accurately.

#### [openMVS](https://github.com/cdcseacave/openMVS)
[![Stars](https://img.shields.io/github/stars/cdcseacave/openMVS)](Stars) [![Forks](https://img.shields.io/github/forks/cdcseacave/openMVS)](Forks) [![Watchers](https://img.shields.io/github/watchers/cdcseacave/openMVS)](Watchers) [![License](https://img.shields.io/github/license/cdcseacave/openMVS)](LICENSE)

OpenMVS (Multi-View Stereo) is a library for computer-vision scientists and especially targeted to the Multi-View Stereo reconstruction community. The input is a set of camera poses plus the sparse point-cloud and the output is a textured mesh.

#### [AliceVision](https://github.com/alicevision/AliceVision)
[![Stars](https://img.shields.io/github/stars/alicevision/AliceVision)](Stars) [![Forks](https://img.shields.io/github/forks/alicevision/AliceVision)](Forks) [![Watchers](https://img.shields.io/github/watchers/alicevision/AliceVision)](Watchers) [![License](https://img.shields.io/github/license/alicevision/AliceVision)](LICENSE)

AliceVision is a Photogrammetric Computer Vision Framework which provides a 3D Reconstruction and Camera Tracking algorithms.

## CG

### Geometry Processing

#### [libigl](https://github.com/libigl/libigl)
[![Stars](https://img.shields.io/github/stars/libigl/libigl)](Stars) [![Forks](https://img.shields.io/github/forks/libigl/libigl)](Forks) [![Watchers](https://img.shields.io/github/watchers/libigl/libigl)](Watchers) [![License](https://img.shields.io/github/license/libigl/libigl)](LICENSE)

A simple C++ geometry processing library.

#### [meshlab](https://github.com/cnr-isti-vclab/meshlab)
[![Stars](https://img.shields.io/github/stars/cnr-isti-vclab/meshlab)](Stars) [![Forks](https://img.shields.io/github/forks/cnr-isti-vclab/meshlab)](Forks) [![Watchers](https://img.shields.io/github/watchers/cnr-isti-vclab/meshlab)](Watchers) [![License](https://img.shields.io/github/license/cnr-isti-vclab/meshlab)](LICENSE)

MeshLab is an open source, portable, and extensible system for the processing and editing of unstructured large 3D triangular meshes.

#### [CGAL](https://github.com/CGAL/cgal)
[![Stars](https://img.shields.io/github/stars/CGAL/cgal)](Stars) [![Forks](https://img.shields.io/github/forks/CGAL/cgal)](Forks) [![Watchers](https://img.shields.io/github/watchers/CGAL/cgal)](Watchers) [![License](https://img.shields.io/github/license/CGAL/cgal)](LICENSE)

The Computational Geometry Algorithms Library (CGAL), a C++ library that aims to provide easy access to efficient and reliable algorithms in computational geometry.

#### [Geogram](https://github.com/BrunoLevy/geogram)
[![Stars](https://img.shields.io/github/stars/BrunoLevy/geogram)](Stars) [![Forks](https://img.shields.io/github/forks/BrunoLevy/geogram)](Forks) [![Watchers](https://img.shields.io/github/watchers/BrunoLevy/geogram)](Watchers) [![License](https://img.shields.io/github/license/BrunoLevy/geogram)](LICENSE)

Geogram is a programming library with geometric algorithms. And [Graphite](https://github.com/BrunoLevy/GraphiteThree) is an experimental 3D modeler built around geogram.

#### [Open3D](https://github.com/intel-isl/Open3D)
[![Stars](https://img.shields.io/github/stars/intel-isl/Open3D)](Stars) [![Forks](https://img.shields.io/github/forks/intel-isl/Open3D)](Forks) [![Watchers](https://img.shields.io/github/watchers/intel-isl/Open3D)](Watchers) [![License](https://img.shields.io/github/license/intel-isl/Open3D)](LICENSE)

A modern library for 3D data processing.

#### [vcglib](https://github.com/cnr-isti-vclab/vcglib)
[![Stars](https://img.shields.io/github/stars/cnr-isti-vclab/vcglib)](Stars) [![Forks](https://img.shields.io/github/forks/cnr-isti-vclab/vcglib)](Forks) [![Watchers](https://img.shields.io/github/watchers/cnr-isti-vclab/vcglib)](Watchers) [![License](https://img.shields.io/github/license/cnr-isti-vclab/vcglib)](LICENSE)

The Visualization and Computer Graphics Library (VCGlib for short), a open source, portable, C++, templated, no dependency, library for manipulation, processing, cleaning, simplifying triangle meshes. And it is the base of [Meshlab](http://www.meshlab.net).

#### [OpenFlipper](http://www.openflipper.org/)

A flexible geometry modeling and processing framework.

#### [geometry-central](https://github.com/nmwsharp/geometry-central)
[![Stars](https://img.shields.io/github/stars/nmwsharp/geometry-central)](Stars) [![Forks](https://img.shields.io/github/forks/nmwsharp/geometry-central)](Forks) [![Watchers](https://img.shields.io/github/watchers/nmwsharp/geometry-central)](Watchers) [![License](https://img.shields.io/github/license/nmwsharp/geometry-central)](LICENSE)

Geometry-central is a modern C++ library of data structures and algorithms for geometry processing, with a particular focus on surface meshes.

#### [Polygon Mesh Processing Library](https://github.com/pmp-library/pmp-library)
[![Stars](https://img.shields.io/github/stars/pmp-library/pmp-library)](Stars) [![Forks](https://img.shields.io/github/forks/pmp-library/pmp-library)](Forks) [![Watchers](https://img.shields.io/github/watchers/pmp-library/pmp-library)](Watchers) [![License](https://img.shields.io/github/license/pmp-library/pmp-library)](LICENSE)

The Polygon Mesh Processing Library is a modern C++ open-source library for processing and visualizing polygon surface meshes.

#### [cinolib](https://github.com/mlivesu/cinolib)
[![Stars](https://img.shields.io/github/stars/mlivesu/cinolib)](Stars) [![Forks](https://img.shields.io/github/forks/mlivesu/cinolib)](Forks) [![Watchers](https://img.shields.io/github/watchers/mlivesu/cinolib)](Watchers) [![License](https://img.shields.io/github/license/mlivesu/cinolib)](LICENSE)

A generic programming header only C++ library for processing polygonal and polyhedral meshes.

#### [Easy3D](https://github.com/LiangliangNan/Easy3D)
[![Stars](https://img.shields.io/github/stars/LiangliangNan/Easy3D)](Stars) [![Forks](https://img.shields.io/github/forks/LiangliangNan/Easy3D)](Forks) [![Watchers](https://img.shields.io/github/watchers/LiangliangNan/Easy3D)](Watchers) [![License](https://img.shields.io/github/license/LiangliangNan/Easy3D)](LICENSE)

Easy3D is an open-source library for 3D modeling, geometry processing, and rendering. It is implemented in C++ and designed with an emphasis on simplicity and efficiency.

#### [starlab](https://github.com/OpenGP/starlab)
[![Stars](https://img.shields.io/github/stars/OpenGP/starlab)](Stars) [![Forks](https://img.shields.io/github/forks/OpenGP/starlab)](Forks) [![Watchers](https://img.shields.io/github/watchers/OpenGP/starlab)](Watchers) [![License](https://img.shields.io/github/license/OpenGP/starlab)](LICENSE)

A lightweight, modular, and cross-platform (Windows, OSX, Linux) 3D geometry processing environment.

### PointCloud Processing

#### [Point Cloud Library (PCL)](https://github.com/PointCloudLibrary/pcl)
[![Stars](https://img.shields.io/github/stars/PointCloudLibrary/pcl)](Stars) [![Forks](https://img.shields.io/github/forks/PointCloudLibrary/pcl)](Forks) [![Watchers](https://img.shields.io/github/watchers/PointCloudLibrary/pcl)](Watchers) [![License](https://img.shields.io/github/license/PointCloudLibrary/pcl)](LICENSE)

The Point Cloud Library (PCL) is a standalone, large scale, open project for 2D/3D image and point cloud processing.

#### [cilantro](https://github.com/kzampog/cilantro)
[![Stars](https://img.shields.io/github/stars/kzampog/cilantro)](Stars) [![Forks](https://img.shields.io/github/forks/kzampog/cilantro)](Forks) [![Watchers](https://img.shields.io/github/watchers/kzampog/cilantro)](Watchers) [![License](https://img.shields.io/github/license/kzampog/cilantro)](LICENSE)

cilantro is a lean and fast C++ library for working with point cloud data.

#### [Draco](https://github.com/google/draco)
[![Stars](https://img.shields.io/github/stars/google/draco)](Stars) [![Forks](https://img.shields.io/github/forks/google/draco)](Forks) [![Watchers](https://img.shields.io/github/watchers/google/draco)](Watchers) [![License](https://img.shields.io/github/license/google/draco)](LICENSE)

Draco is a library for compressing and decompressing 3D geometric meshes and point clouds. It is intended to improve the storage and transmission of 3D graphics.

#### [CloudCompare](https://github.com/CloudCompare/CloudCompare)
[![Stars](https://img.shields.io/github/stars/CloudCompare/CloudCompare)](Stars) [![Forks](https://img.shields.io/github/forks/CloudCompare/CloudCompare)](Forks) [![Watchers](https://img.shields.io/github/watchers/CloudCompare/CloudCompare)](Watchers) [![License](https://img.shields.io/github/license/CloudCompare/CloudCompare)](LICENSE)

CloudCompare is a 3D point cloud (and triangular mesh) processing software. It was originally designed to perform comparison between two 3D points clouds (such as the ones obtained with a laser scanner) or between a point cloud and a triangular mesh. It relies on an octree structure that is highly optimized for this particular use-case. It was also meant to deal with huge point clouds (typically more than 10 million points, and up to 120 million with 2 GB of memory).

### Visualization

#### [polyscope](https://github.com/nmwsharp/polyscope)
[![Stars](https://img.shields.io/github/stars/nmwsharp/polyscope)](Stars) [![Forks](https://img.shields.io/github/forks/nmwsharp/polyscope)](Forks) [![Watchers](https://img.shields.io/github/watchers/nmwsharp/polyscope)](Watchers) [![License](https://img.shields.io/github/license/nmwsharp/polyscope)](LICENSE)

polyscope is a C++/Python viewer and user interface for 3D data, like meshes and point clouds.

### Triangulation

#### [Triangle](http://www.cs.cmu.edu/~quake/triangle.html)

A two-dimensional quality mesh generator and delaunay triangulator.

#### [CDT](https://github.com/artem-ogre/CDT)
[![Stars](https://img.shields.io/github/stars/artem-ogre/CDT)](Stars) [![Forks](https://img.shields.io/github/forks/artem-ogre/CDT)](Forks) [![Watchers](https://img.shields.io/github/watchers/artem-ogre/CDT)](Watchers) [![License](https://img.shields.io/github/license/artem-ogre/CDT)](LICENSE)

CDT is a C++ library for generating constraint or conforming Delaunay triangulations.

### Texture&Atlas

#### [mvs-texturing](https://github.com/nmoehrle/mvs-texturing)
[![Stars](https://img.shields.io/github/stars/nmoehrle/mvs-texturing)](Stars) [![Forks](https://img.shields.io/github/forks/nmoehrle/mvs-texturing)](Forks) [![Watchers](https://img.shields.io/github/watchers/nmoehrle/mvs-texturing)](Watchers) [![License](https://img.shields.io/github/license/nmoehrle/mvs-texturing)](LICENSE)

MVS-Texturing is a project that focuses on texturing 3D reconstructions from multi-view stereo images.

#### [xatlas](https://github.com/jpcy/xatlas)
[![Stars](https://img.shields.io/github/stars/jpcy/xatlas)](Stars) [![Forks](https://img.shields.io/github/forks/jpcy/xatlas)](Forks) [![Watchers](https://img.shields.io/github/watchers/jpcy/xatlas)](Watchers) [![License](https://img.shields.io/github/license/jpcy/xatlas)](LICENSE)

xatlas is a small C++11 library with no external dependencies that generates unique texture coordinates suitable for baking lightmaps or texture painting.

#### [UVAtlas](https://github.com/Microsoft/UVAtlas)
[![Stars](https://img.shields.io/github/stars/Microsoft/UVAtlas)](Stars) [![Forks](https://img.shields.io/github/forks/Microsoft/UVAtlas)](Forks) [![Watchers](https://img.shields.io/github/watchers/Microsoft/UVAtlas)](Watchers) [![License](https://img.shields.io/github/license/Microsoft/UVAtlas)](LICENSE)

UVAtlas is a shared source library for creating and packing an isochart texture atlas.

#### [ptex](https://github.com/wdas/ptex)
[![Stars](https://img.shields.io/github/stars/wdas/ptex)](Stars) [![Forks](https://img.shields.io/github/forks/wdas/ptex)](Forks) [![Watchers](https://img.shields.io/github/watchers/wdas/ptex)](Watchers) [![License](https://img.shields.io/github/license/wdas/ptex)](LICENSE)

Ptex is a texture mapping system developed by Walt Disney Animation Studios for production-quality rendering.

### Transformation

#### [manif](https://github.com/artivis/manif)
[![Stars](https://img.shields.io/github/stars/artivis/manif)](Stars) [![Forks](https://img.shields.io/github/forks/artivis/manif)](Forks) [![Watchers](https://img.shields.io/github/watchers/artivis/manif)](Watchers) [![License](https://img.shields.io/github/license/artivis/manif)](LICENSE)

manif is a header-only C++11 Lie theory library for state-estimation targeted at robotics applications.

#### [Sophus](https://github.com/strasdat/Sophus)
[![Stars](https://img.shields.io/github/stars/strasdat/Sophus)](Stars) [![Forks](https://img.shields.io/github/forks/strasdat/Sophus)](Forks) [![Watchers](https://img.shields.io/github/watchers/strasdat/Sophus)](Watchers) [![License](https://img.shields.io/github/license/strasdat/Sophus)](LICENSE)

Sophus is a c++ implementation of Lie groups commonly used for 2d and 3d geometric problems (i.e. for Computer Vision or Robotics applications). Among others, this package includes the special orthogonal groups SO(2) and SO(3) to present rotations in 2d and 3d as well as the special Euclidean group SE(2) and SE(3) to represent rigid body transformations (i.e. rotations and translations) in 2d and 3d. It is released under a MIT license.

### Registration

#### [libpointmatcher](https://github.com/ethz-asl/libpointmatcher)
[![Stars](https://img.shields.io/github/stars/ethz-asl/libpointmatcher)](Stars) [![Forks](https://img.shields.io/github/forks/ethz-asl/libpointmatcher)](Forks) [![Watchers](https://img.shields.io/github/watchers/ethz-asl/libpointmatcher)](Watchers) [![License](https://img.shields.io/github/license/ethz-asl/libpointmatcher)](LICENSE)

libpointmatcher is a modular library implementing the Iterative Closest Point (ICP) algorithm for aligning point clouds. It has applications in robotics and computer vision. \nIt is released under a permissive BSD license.

#### [OpenGR](https://github.com/STORM-IRIT/OpenGR)
[![Stars](https://img.shields.io/github/stars/STORM-IRIT/OpenGR)](Stars) [![Forks](https://img.shields.io/github/forks/STORM-IRIT/OpenGR)](Forks) [![Watchers](https://img.shields.io/github/watchers/STORM-IRIT/OpenGR)](Watchers) [![License](https://img.shields.io/github/license/STORM-IRIT/OpenGR)](LICENSE)

OpenGR is a set C++ libraries for 3D Global Registration. And it aims at providing several state of the art global registration algorithms for 3D data.

#### [FastGlobalRegistration](https://github.com/intel-isl/FastGlobalRegistration)
[![Stars](https://img.shields.io/github/stars/intel-isl/FastGlobalRegistration)](Stars) [![Forks](https://img.shields.io/github/forks/intel-isl/FastGlobalRegistration)](Forks) [![Watchers](https://img.shields.io/github/watchers/intel-isl/FastGlobalRegistration)](Watchers) [![License](https://img.shields.io/github/license/intel-isl/FastGlobalRegistration)](LICENSE)

FastGlobalRegistration is an open source C++ implementation based on the technique presented in the paper "Fast Global Registration, ECCV 2016."

#### [ICPCUDA](https://github.com/mp3guy/ICPCUDA)
[![Stars](https://img.shields.io/github/stars/mp3guy/ICPCUDA)](Stars) [![Forks](https://img.shields.io/github/forks/mp3guy/ICPCUDA)](Forks) [![Watchers](https://img.shields.io/github/watchers/mp3guy/ICPCUDA)](Watchers) [![License](https://img.shields.io/github/license/mp3guy/ICPCUDA)](LICENSE)

Super fast implementation of ICP in CUDA for compute capable devices 3.5 or higher. Requires CUDA, includes Pangolin, Eigen and Sophus third party submodules

### Nearest Neighbors

#### [ANN](https://www.cs.umd.edu/~mount/ANN)

ANN is a library written in C++, which supports data structures and algorithms for both exact and approximate nearest neighbor searching in arbitrarily high dimensions.

#### [nanoflann](https://github.com/jlblancoc/nanoflann)
[![Stars](https://img.shields.io/github/stars/jlblancoc/nanoflann)](Stars) [![Forks](https://img.shields.io/github/forks/jlblancoc/nanoflann)](Forks) [![Watchers](https://img.shields.io/github/watchers/jlblancoc/nanoflann)](Watchers) [![License](https://img.shields.io/github/license/jlblancoc/nanoflann)](LICENSE)

A C++11 header-only library for Nearest Neighbor (NN) search with KD-trees.

### Collision

#### [fcl-Flexible Collision Library](https://github.com/flexible-collision-library/fcl)
[![Stars](https://img.shields.io/github/stars/flexible-collision-library/fcl)](Stars) [![Forks](https://img.shields.io/github/forks/flexible-collision-library/fcl)](Forks) [![Watchers](https://img.shields.io/github/watchers/flexible-collision-library/fcl)](Watchers) [![License](https://img.shields.io/github/license/flexible-collision-library/fcl)](LICENSE)

FCL is a library for performing three types of proximity queries on a pair of geometric models composed of triangles.

### Rendering

#### [bgfx](https://github.com/bkaradzic/bgfx)
[![Stars](https://img.shields.io/github/stars/bkaradzic/bgfx)](Stars) [![Forks](https://img.shields.io/github/forks/bkaradzic/bgfx)](Forks) [![Watchers](https://img.shields.io/github/watchers/bkaradzic/bgfx)](Watchers) [![License](https://img.shields.io/github/license/bkaradzic/bgfx)](LICENSE)

bgfx is a cross-platform, graphics API agnostic, "Bring Your Own Engine/Framework" style rendering library.

#### [tinyrenderer](https://github.com/ssloy/tinyrenderer)
[![Stars](https://img.shields.io/github/stars/ssloy/tinyrenderer)](Stars) [![Forks](https://img.shields.io/github/forks/ssloy/tinyrenderer)](Forks) [![Watchers](https://img.shields.io/github/watchers/ssloy/tinyrenderer)](Watchers) [![License](https://img.shields.io/github/license/ssloy/tinyrenderer)](LICENSE)

A tiny yet powerful rendering library.

#### [yocto-gl](https://github.com/xelatihy/yocto-gl)
[![Stars](https://img.shields.io/github/stars/xelatihy/yocto-gl)](Stars) [![Forks](https://img.shields.io/github/forks/xelatihy/yocto-gl)](Forks) [![Watchers](https://img.shields.io/github/watchers/xelatihy/yocto-gl)](Watchers) [![License](https://img.shields.io/github/license/xelatihy/yocto-gl)](LICENSE)

Yocto/GL is a collection of small C++17 libraries for building physically-based graphics algorithms released under the MIT license.

#### [Filament](https://github.com/google/filament)
[![Stars](https://img.shields.io/github/stars/google/filament)](Stars) [![Forks](https://img.shields.io/github/forks/google/filament)](Forks) [![Watchers](https://img.shields.io/github/watchers/google/filament)](Watchers) [![License](https://img.shields.io/github/license/google/filament)](LICENSE)

Filament is a real-time physically based rendering engine for Android, iOS, Linux, macOS, Windows, and WebGL. It is designed to be as small as possible and as efficient as possible on Android.

### Animation

#### [ozz-animation](https://github.com/guillaumeblanc/ozz-animation)
[![Stars](https://img.shields.io/github/stars/guillaumeblanc/ozz-animation)](Stars) [![Forks](https://img.shields.io/github/forks/guillaumeblanc/ozz-animation)](Forks) [![Watchers](https://img.shields.io/github/watchers/guillaumeblanc/ozz-animation)](Watchers) [![License](https://img.shields.io/github/license/guillaumeblanc/ozz-animation)](LICENSE)

ozz-animation is an open source c++ 3d skeletal animation library. It provides runtime character animation functionalities (sampling, blending...), with the toolset to import major DCC formats (Collada, Fbx, glTF...). It proposes a low-level renderer and game-engine agnostic implementation, focusing on performance and memory constraints with a data-oriented design.

### Simulation

#### [bullet3](https://github.com/bulletphysics/bullet3)
[![Stars](https://img.shields.io/github/stars/bulletphysics/bullet3)](Stars) [![Forks](https://img.shields.io/github/forks/bulletphysics/bullet3)](Forks) [![Watchers](https://img.shields.io/github/watchers/bulletphysics/bullet3)](Watchers) [![License](https://img.shields.io/github/license/bulletphysics/bullet3)](LICENSE)

Bullet Physics SDK: real-time collision detection and multi-physics simulation for VR, games, visual effects, robotics, machine learning etc.

#### [pinocchio](https://github.com/stack-of-tasks/pinocchio)
[![Stars](https://img.shields.io/github/stars/stack-of-tasks/pinocchio)](Stars) [![Forks](https://img.shields.io/github/forks/stack-of-tasks/pinocchio)](Forks) [![Watchers](https://img.shields.io/github/watchers/stack-of-tasks/pinocchio)](Watchers) [![License](https://img.shields.io/github/license/stack-of-tasks/pinocchio)](LICENSE)

Pinocchio is a fast and flexible implementation of Rigid Body Dynamics algorithms and their analytical derivatives.

### Modeling

#### [OpenSCAD](https://github.com/openscad/openscad)
[![Stars](https://img.shields.io/github/stars/openscad/openscad)](Stars) [![Forks](https://img.shields.io/github/forks/openscad/openscad)](Forks) [![Watchers](https://img.shields.io/github/watchers/openscad/openscad)](Watchers) [![License](https://img.shields.io/github/license/openscad/openscad)](LICENSE)

OpenSCAD is a software for creating solid 3D CAD objects.

#### [Dust3D](https://github.com/huxingyi/dust3d)
[![Stars](https://img.shields.io/github/stars/huxingyi/dust3d)](Stars) [![Forks](https://img.shields.io/github/forks/huxingyi/dust3d)](Forks) [![Watchers](https://img.shields.io/github/watchers/huxingyi/dust3d)](Watchers) [![License](https://img.shields.io/github/license/huxingyi/dust3d)](LICENSE)

Dust3D is a cross-platform open-source 3D modeling software. Auto UV unwrapping, auto rigging with PBR Material support, pose and motion authoring all in one.

### Others

#### [quickhull](https://github.com/akuukka/quickhull)
[![Stars](https://img.shields.io/github/stars/akuukka/quickhull)](Stars) [![Forks](https://img.shields.io/github/forks/akuukka/quickhull)](Forks) [![Watchers](https://img.shields.io/github/watchers/akuukka/quickhull)](Watchers) [![License](https://img.shields.io/github/license/akuukka/quickhull)](LICENSE)

C++ implementation of the 3D QuickHull algorithm.

#### [QHull](https://github.com/qhull/qhull)
[![Stars](https://img.shields.io/github/stars/qhull/qhull)](Stars) [![Forks](https://img.shields.io/github/forks/qhull/qhull)](Forks) [![Watchers](https://img.shields.io/github/watchers/qhull/qhull)](Watchers) [![License](https://img.shields.io/github/license/qhull/qhull)](LICENSE)

Qhull is a general dimension convex hull program. It also generates Delaunay triangulations, Voronoi diagrams, furthest-site Voronoi diagrams, and halfspace intersections about a point.

#### [Cork Boolean Library](https://github.com/gilbo/cork)
[![Stars](https://img.shields.io/github/stars/gilbo/cork)](Stars) [![Forks](https://img.shields.io/github/forks/gilbo/cork)](Forks) [![Watchers](https://img.shields.io/github/watchers/gilbo/cork)](Watchers) [![License](https://img.shields.io/github/license/gilbo/cork)](LICENSE)

Cork is designed to support Boolean operations between triangle meshes.


## [Back to Top](#table-of-contents)
