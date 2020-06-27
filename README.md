# Awesome Cpp Libs

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> An awesome & curated list of cpp libraries for **CV/CGers**.

-----

## Table of Contents

- [Cpp](#cpp)
  - [Command Line Parser](#command-line-parser)
  - [Logging](#logging)
  - [Format String](#format-string)
  - [Testing](#testing)
  - [Serialization](#serialization)
  - [GUI](#gui)
- [Math](#math)
  - [Linear Algebra](#linear-algebra)
  - [Optimization](#optimization)
- [CV](#cv)
  - [Image Processing](#image-processing)
  - [Multi-View Reconstruction](#multi-view-reconstruction)
- [CG](#cg)
  - [Geometry Processing](#geometry-processing)
  - [PointCloud Processing](#pointcloud-processing)
  - [Visualization](#visualization)
  - [Triangulation](#triangulation)
  - [Transformation](#transformation)
  - [Registration](#registration)
  - [Nearest Neighbors](#nearest-neighbors)
  - [Collision](#collision)
  - [Others](#others)

-----
## Cpp

### Command Line Parser

#### [cxxopts](https://github.com/jarro2783/cxxopts)
[![Watchers](https://img.shields.io/github/watchers/jarro2783/cxxopts)](Watchers) [![Stars](https://img.shields.io/github/stars/jarro2783/cxxopts)](Stars) [![Forks](https://img.shields.io/github/forks/jarro2783/cxxopts)](Forks) [![License](https://img.shields.io/github/license/jarro2783/cxxopts)](LICENSE)

Lightweight C++ command line option parser.

### Logging

#### [spdlog](https://github.com/gabime/spdlog)
[![Watchers](https://img.shields.io/github/watchers/gabime/spdlog)](Watchers) [![Stars](https://img.shields.io/github/stars/gabime/spdlog)](Stars) [![Forks](https://img.shields.io/github/forks/gabime/spdlog)](Forks) [![License](https://img.shields.io/github/license/gabime/spdlog)](LICENSE)

Very fast, header-only/compiled, C++ logging library.

#### [plog](https://github.com/SergiusTheBest/plog)
[![Watchers](https://img.shields.io/github/watchers/SergiusTheBest/plog)](Watchers) [![Stars](https://img.shields.io/github/stars/SergiusTheBest/plog)](Stars) [![Forks](https://img.shields.io/github/forks/SergiusTheBest/plog)](Forks) [![License](https://img.shields.io/github/license/SergiusTheBest/plog)](LICENSE)

Portable, simple and extensible C++ logging library, pretty powerful logging library in about 1000 lines of code.

### Format String

#### [fmt](https://github.com/fmtlib/fmt)
[![Watchers](https://img.shields.io/github/watchers/fmtlib/fmt)](Watchers) [![Stars](https://img.shields.io/github/stars/fmtlib/fmt)](Stars) [![Forks](https://img.shields.io/github/forks/fmtlib/fmt)](Forks) [![License](https://img.shields.io/github/license/fmtlib/fmt)](LICENSE)

{fmt} is an open-source formatting library for C++. It can be used as a safe and fast alternative to (s)printf and iostreams.

#### [tinyformat](https://github.com/c42f/tinyformat)
[![Watchers](https://img.shields.io/github/watchers/c42f/tinyformat)](Watchers) [![Stars](https://img.shields.io/github/stars/c42f/tinyformat)](Stars) [![Forks](https://img.shields.io/github/forks/c42f/tinyformat)](Forks) [![License](https://img.shields.io/github/license/c42f/tinyformat)](LICENSE)

tinyformat.h is a type safe printf replacement library in a single C++ header file.

### Testing

#### [Catch2](https://github.com/catchorg/Catch2)
[![Watchers](https://img.shields.io/github/watchers/catchorg/Catch2)](Watchers) [![Stars](https://img.shields.io/github/stars/catchorg/Catch2)](Stars) [![Forks](https://img.shields.io/github/forks/catchorg/Catch2)](Forks) [![License](https://img.shields.io/github/license/catchorg/Catch2)](LICENSE)

A modern, C++-native, header-only, test framework for unit-tests, TDD and BDD - using C++11, C++14, C++17 and later (or C++03 on the Catch1.x branch)

### Serialization

#### [cereal](https://github.com/USCiLab/cereal)
[![Watchers](https://img.shields.io/github/watchers/USCiLab/cereal)](Watchers) [![Stars](https://img.shields.io/github/stars/USCiLab/cereal)](Stars) [![Forks](https://img.shields.io/github/forks/USCiLab/cereal)](Forks) [![License](https://img.shields.io/github/license/USCiLab/cereal)](LICENSE)

cereal is a header-only C++11 serialization library. cereal takes arbitrary data types and reversibly turns them into different representations, such as compact binary encodings, XML, or JSON. cereal was designed to be fast, light-weight, and easy to extend - it has no external dependencies and can be easily bundled with other code or used standalone.

#### [json](https://github.com/nlohmann/json)
[![Watchers](https://img.shields.io/github/watchers/nlohmann/json)](Watchers) [![Stars](https://img.shields.io/github/stars/nlohmann/json)](Stars) [![Forks](https://img.shields.io/github/forks/nlohmann/json)](Forks) [![License](https://img.shields.io/github/license/nlohmann/json)](LICENSE)

JSON for Modern C++ 

### GUI

#### [imgui](https://github.com/ocornut/imgui)
[![Watchers](https://img.shields.io/github/watchers/ocornut/imgui)](Watchers) [![Stars](https://img.shields.io/github/stars/ocornut/imgui)](Stars) [![Forks](https://img.shields.io/github/forks/ocornut/imgui)](Forks) [![License](https://img.shields.io/github/license/ocornut/imgui)](LICENSE)

Dear ImGui is a bloat-free graphical user interface library for C++. It outputs optimized vertex buffers that you can render anytime in your 3D-pipeline enabled application. It is fast, portable, renderer agnostic and self-contained (no external dependencies).

#### [nanogui](https://github.com/wjakob/nanogui)
[![Watchers](https://img.shields.io/github/watchers/wjakob/nanogui)](Watchers) [![Stars](https://img.shields.io/github/stars/wjakob/nanogui)](Stars) [![Forks](https://img.shields.io/github/forks/wjakob/nanogui)](Forks) [![License](https://img.shields.io/github/license/wjakob/nanogui)](LICENSE)

NanoGUI is a minimalistic cross-platform widget library for OpenGL 3.x or higher. It supports automatic layout generation, stateful C++11 lambdas callbacks, a variety of useful widget types and Retina-capable rendering on Apple devices thanks to NanoVG by Mikko Mononen. Python bindings of all functionality are provided using pybind11.

## Math

### Linear Algebra

#### [Eigen](http://eigen.tuxfamily.org)

Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

#### [linalg](https://github.com/sgorsten/linalg)
[![Watchers](https://img.shields.io/github/watchers/sgorsten/linalg)](Watchers) [![Stars](https://img.shields.io/github/stars/sgorsten/linalg)](Stars) [![Forks](https://img.shields.io/github/forks/sgorsten/linalg)](Forks) [![License](https://img.shields.io/github/license/sgorsten/linalg)](LICENSE)

`linalg.h` is a single header, public domain, short vector math library for C++.

### Optimization

#### [ceres-solver](https://github.com/ceres-solver/ceres-solver)
[![Watchers](https://img.shields.io/github/watchers/ceres-solver/ceres-solver)](Watchers) [![Stars](https://img.shields.io/github/stars/ceres-solver/ceres-solver)](Stars) [![Forks](https://img.shields.io/github/forks/ceres-solver/ceres-solver)](Forks) [![License](https://img.shields.io/github/license/ceres-solver/ceres-solver)](LICENSE)

Ceres Solver is an open source C++ library for modeling and solving large, complicated optimization problems. Ceres Solver can solve two kinds of problems.
- Non-linear Least Squares problems with bounds constraints.
- General unconstrained optimization problems.


#### [Ipopt](https://github.com/coin-or/Ipopt)
[![Watchers](https://img.shields.io/github/watchers/coin-or/Ipopt)](Watchers) [![Stars](https://img.shields.io/github/stars/coin-or/Ipopt)](Stars) [![Forks](https://img.shields.io/github/forks/coin-or/Ipopt)](Forks) [![License](https://img.shields.io/github/license/coin-or/Ipopt)](LICENSE)

Ipopt (Interior Point OPTimizer) is a software package for large-scale nonlinear optimization.

#### [NLopt](https://github.com/stevengj/nlopt)
[![Watchers](https://img.shields.io/github/watchers/stevengj/nlopt)](Watchers) [![Stars](https://img.shields.io/github/stars/stevengj/nlopt)](Stars) [![Forks](https://img.shields.io/github/forks/stevengj/nlopt)](Forks) [![License](https://img.shields.io/github/license/stevengj/nlopt)](LICENSE)

NLopt is a library for nonlinear local and global optimization, for functions with and without gradient information. It is designed as a simple, unified interface and packaging of several free/open-source nonlinear optimization libraries.

## CV

### Image Processing

#### [OpenCV](https://github.com/opencv/opencv)
[![Watchers](https://img.shields.io/github/watchers/opencv/opencv)](Watchers) [![Stars](https://img.shields.io/github/stars/opencv/opencv)](Stars) [![Forks](https://img.shields.io/github/forks/opencv/opencv)](Forks) [![License](https://img.shields.io/github/license/opencv/opencv)](LICENSE)

Open Source Computer Vision Library.

#### [stb](https://github.com/nothings/stb)
[![Watchers](https://img.shields.io/github/watchers/nothings/stb)](Watchers) [![Stars](https://img.shields.io/github/stars/nothings/stb)](Stars) [![Forks](https://img.shields.io/github/forks/nothings/stb)](Forks) [![License](https://img.shields.io/github/license/nothings/stb)](LICENSE)

single-file public domain (or MIT licensed) libraries for C/C++

### Multi-View Reconstruction

#### [OpenMVG](https://github.com/openMVG/openMVG)
[![Watchers](https://img.shields.io/github/watchers/openMVG/openMVG)](Watchers) [![Stars](https://img.shields.io/github/stars/openMVG/openMVG)](Stars) [![Forks](https://img.shields.io/github/forks/openMVG/openMVG)](Forks) [![License](https://img.shields.io/github/license/openMVG/openMVG)](LICENSE)

OpenMVG (Multiple View Geometry) is a library for computer-vision scientists and especially targeted to the Multiple View Geometry community. It is designed to provide an easy access to the classical problem solvers in Multiple View Geometry and solve them accurately.

#### [openMVS](https://github.com/cdcseacave/openMVS)
[![Watchers](https://img.shields.io/github/watchers/cdcseacave/openMVS)](Watchers) [![Stars](https://img.shields.io/github/stars/cdcseacave/openMVS)](Stars) [![Forks](https://img.shields.io/github/forks/cdcseacave/openMVS)](Forks) [![License](https://img.shields.io/github/license/cdcseacave/openMVS)](LICENSE)

OpenMVS (Multi-View Stereo) is a library for computer-vision scientists and especially targeted to the Multi-View Stereo reconstruction community. The input is a set of camera poses plus the sparse point-cloud and the output is a textured mesh.

#### [COLMAP](https://github.com/colmap/colmap)
[![Watchers](https://img.shields.io/github/watchers/colmap/colmap)](Watchers) [![Stars](https://img.shields.io/github/stars/colmap/colmap)](Stars) [![Forks](https://img.shields.io/github/forks/colmap/colmap)](Forks) [![License](https://img.shields.io/github/license/colmap/colmap)](LICENSE)

COLMAP is a general-purpose Structure-from-Motion (SfM) and Multi-View Stereo (MVS) pipeline with a graphical and command-line interface. It offers a wide range of features for reconstruction of ordered and unordered image collections. The software is licensed under the new BSD license.

## CG

### Geometry Processing

#### [libigl](https://github.com/libigl/libigl)
[![Watchers](https://img.shields.io/github/watchers/libigl/libigl)](Watchers) [![Stars](https://img.shields.io/github/stars/libigl/libigl)](Stars) [![Forks](https://img.shields.io/github/forks/libigl/libigl)](Forks) [![License](https://img.shields.io/github/license/libigl/libigl)](LICENSE)

A simple C++ geometry processing library.

#### [CGAL](https://github.com/CGAL/cgal)
[![Watchers](https://img.shields.io/github/watchers/CGAL/cgal)](Watchers) [![Stars](https://img.shields.io/github/stars/CGAL/cgal)](Stars) [![Forks](https://img.shields.io/github/forks/CGAL/cgal)](Forks) [![License](https://img.shields.io/github/license/CGAL/cgal)](LICENSE)

The Computational Geometry Algorithms Library (CGAL), a C++ library that aims to provide easy access to efficient and reliable algorithms in computational geometry.

#### [Open3D](https://github.com/intel-isl/Open3D)
[![Watchers](https://img.shields.io/github/watchers/intel-isl/Open3D)](Watchers) [![Stars](https://img.shields.io/github/stars/intel-isl/Open3D)](Stars) [![Forks](https://img.shields.io/github/forks/intel-isl/Open3D)](Forks) [![License](https://img.shields.io/github/license/intel-isl/Open3D)](LICENSE)

A modern library for 3D data processing.

#### [vcglib](https://github.com/cnr-isti-vclab/vcglib)
[![Watchers](https://img.shields.io/github/watchers/cnr-isti-vclab/vcglib)](Watchers) [![Stars](https://img.shields.io/github/stars/cnr-isti-vclab/vcglib)](Stars) [![Forks](https://img.shields.io/github/forks/cnr-isti-vclab/vcglib)](Forks) [![License](https://img.shields.io/github/license/cnr-isti-vclab/vcglib)](LICENSE)

The Visualization and Computer Graphics Library (VCGlib for short), a open source, portable, C++, templated, no dependency, library for manipulation, processing, cleaning, simplifying triangle meshes.

#### [OpenFlipper](http://www.openflipper.org/)

A flexible geometry modeling and processing framework.

#### [geometry-central](https://github.com/nmwsharp/geometry-central)
[![Watchers](https://img.shields.io/github/watchers/nmwsharp/geometry-central)](Watchers) [![Stars](https://img.shields.io/github/stars/nmwsharp/geometry-central)](Stars) [![Forks](https://img.shields.io/github/forks/nmwsharp/geometry-central)](Forks) [![License](https://img.shields.io/github/license/nmwsharp/geometry-central)](LICENSE)

Geometry-central is a modern C++ library of data structures and algorithms for geometry processing, with a particular focus on surface meshes.

#### [Polygon Mesh Processing Library](https://github.com/pmp-library/pmp-library)
[![Watchers](https://img.shields.io/github/watchers/pmp-library/pmp-library)](Watchers) [![Stars](https://img.shields.io/github/stars/pmp-library/pmp-library)](Stars) [![Forks](https://img.shields.io/github/forks/pmp-library/pmp-library)](Forks) [![License](https://img.shields.io/github/license/pmp-library/pmp-library)](LICENSE)

The Polygon Mesh Processing Library is a modern C++ open-source library for processing and visualizing polygon surface meshes.

#### [cinolib](https://github.com/mlivesu/cinolib)
[![Watchers](https://img.shields.io/github/watchers/mlivesu/cinolib)](Watchers) [![Stars](https://img.shields.io/github/stars/mlivesu/cinolib)](Stars) [![Forks](https://img.shields.io/github/forks/mlivesu/cinolib)](Forks) [![License](https://img.shields.io/github/license/mlivesu/cinolib)](LICENSE)

A generic programming header only C++ library for processing polygonal and polyhedral meshes.

#### [Easy3D](https://github.com/LiangliangNan/Easy3D)
[![Watchers](https://img.shields.io/github/watchers/LiangliangNan/Easy3D)](Watchers) [![Stars](https://img.shields.io/github/stars/LiangliangNan/Easy3D)](Stars) [![Forks](https://img.shields.io/github/forks/LiangliangNan/Easy3D)](Forks) [![License](https://img.shields.io/github/license/LiangliangNan/Easy3D)](LICENSE)

Easy3D is an open-source library for 3D modeling, geometry processing, and rendering. It is implemented in C++ and designed with an emphasis on simplicity and efficiency.

### PointCloud Processing

#### [Point Cloud Library (PCL)](https://github.com/PointCloudLibrary/pcl)
[![Watchers](https://img.shields.io/github/watchers/PointCloudLibrary/pcl)](Watchers) [![Stars](https://img.shields.io/github/stars/PointCloudLibrary/pcl)](Stars) [![Forks](https://img.shields.io/github/forks/PointCloudLibrary/pcl)](Forks) [![License](https://img.shields.io/github/license/PointCloudLibrary/pcl)](LICENSE)

The Point Cloud Library (PCL) is a standalone, large scale, open project for 2D/3D image and point cloud processing.

#### [cilantro](https://github.com/kzampog/cilantro)
[![Watchers](https://img.shields.io/github/watchers/kzampog/cilantro)](Watchers) [![Stars](https://img.shields.io/github/stars/kzampog/cilantro)](Stars) [![Forks](https://img.shields.io/github/forks/kzampog/cilantro)](Forks) [![License](https://img.shields.io/github/license/kzampog/cilantro)](LICENSE)

cilantro is a lean and fast C++ library for working with point cloud data.

#### [Draco](https://github.com/google/draco)
[![Watchers](https://img.shields.io/github/watchers/google/draco)](Watchers) [![Stars](https://img.shields.io/github/stars/google/draco)](Stars) [![Forks](https://img.shields.io/github/forks/google/draco)](Forks) [![License](https://img.shields.io/github/license/google/draco)](LICENSE)

Draco is a library for compressing and decompressing 3D geometric meshes and point clouds. It is intended to improve the storage and transmission of 3D graphics.

#### [CloudCompare](https://github.com/CloudCompare/CloudCompare)
[![Watchers](https://img.shields.io/github/watchers/CloudCompare/CloudCompare)](Watchers) [![Stars](https://img.shields.io/github/stars/CloudCompare/CloudCompare)](Stars) [![Forks](https://img.shields.io/github/forks/CloudCompare/CloudCompare)](Forks) [![License](https://img.shields.io/github/license/CloudCompare/CloudCompare)](LICENSE)

CloudCompare is a 3D point cloud (and triangular mesh) processing software. It was originally designed to perform comparison between two 3D points clouds (such as the ones obtained with a laser scanner) or between a point cloud and a triangular mesh. It relies on an octree structure that is highly optimized for this particular use-case. It was also meant to deal with huge point clouds (typically more than 10 million points, and up to 120 million with 2 GB of memory).

### Visualization

#### [polyscope](https://github.com/nmwsharp/polyscope)
[![Watchers](https://img.shields.io/github/watchers/nmwsharp/polyscope)](Watchers) [![Stars](https://img.shields.io/github/stars/nmwsharp/polyscope)](Stars) [![Forks](https://img.shields.io/github/forks/nmwsharp/polyscope)](Forks) [![License](https://img.shields.io/github/license/nmwsharp/polyscope)](LICENSE)

olyscope is a C++/Python viewer and user interface for 3D data, like meshes and point clouds.

### Triangulation

#### [Triangle](http://www.cs.cmu.edu/~quake/triangle.html)

A two-dimensional quality mesh generator and delaunay triangulator.

### Transformation

#### [manif](https://github.com/artivis/manif)
[![Watchers](https://img.shields.io/github/watchers/artivis/manif)](Watchers) [![Stars](https://img.shields.io/github/stars/artivis/manif)](Stars) [![Forks](https://img.shields.io/github/forks/artivis/manif)](Forks) [![License](https://img.shields.io/github/license/artivis/manif)](LICENSE)

manif is a header-only C++11 Lie theory library for state-estimation targeted at robotics applications.

#### [Sophus](https://github.com/strasdat/Sophus)
[![Watchers](https://img.shields.io/github/watchers/strasdat/Sophus)](Watchers) [![Stars](https://img.shields.io/github/stars/strasdat/Sophus)](Stars) [![Forks](https://img.shields.io/github/forks/strasdat/Sophus)](Forks) [![License](https://img.shields.io/github/license/strasdat/Sophus)](LICENSE)

Sophus is a c++ implementation of Lie groups commonly used for 2d and 3d geometric problems (i.e. for Computer Vision or Robotics applications). Among others, this package includes the special orthogonal groups SO(2) and SO(3) to present rotations in 2d and 3d as well as the special Euclidean group SE(2) and SE(3) to represent rigid body transformations (i.e. rotations and translations) in 2d and 3d. It is released under a MIT license.

### Registration

#### [libpointmatcher](https://github.com/ethz-asl/libpointmatcher)
[![Watchers](https://img.shields.io/github/watchers/ethz-asl/libpointmatcher)](Watchers) [![Stars](https://img.shields.io/github/stars/ethz-asl/libpointmatcher)](Stars) [![Forks](https://img.shields.io/github/forks/ethz-asl/libpointmatcher)](Forks) [![License](https://img.shields.io/github/license/ethz-asl/libpointmatcher)](LICENSE)

libpointmatcher is a modular library implementing the Iterative Closest Point (ICP) algorithm for aligning point clouds. It has applications in robotics and computer vision. \nIt is released under a permissive BSD license.

#### [OpenGR](https://github.com/STORM-IRIT/OpenGR)
[![Watchers](https://img.shields.io/github/watchers/STORM-IRIT/OpenGR)](Watchers) [![Stars](https://img.shields.io/github/stars/STORM-IRIT/OpenGR)](Stars) [![Forks](https://img.shields.io/github/forks/STORM-IRIT/OpenGR)](Forks) [![License](https://img.shields.io/github/license/STORM-IRIT/OpenGR)](LICENSE)

OpenGR is a set C++ libraries for 3D Global Registration. And it aims at providing several state of the art global registration algorithms for 3D data.

#### [ICPCUDA](https://github.com/mp3guy/ICPCUDA)
[![Watchers](https://img.shields.io/github/watchers/mp3guy/ICPCUDA)](Watchers) [![Stars](https://img.shields.io/github/stars/mp3guy/ICPCUDA)](Stars) [![Forks](https://img.shields.io/github/forks/mp3guy/ICPCUDA)](Forks) [![License](https://img.shields.io/github/license/mp3guy/ICPCUDA)](LICENSE)

Super fast implementation of ICP in CUDA for compute capable devices 3.5 or higher. Requires CUDA, includes Pangolin, Eigen and Sophus third party submodules

### Nearest Neighbors

#### [ANN](https://www.cs.umd.edu/~mount/ANN)

ANN is a library written in C++, which supports data structures and algorithms for both exact and approximate nearest neighbor searching in arbitrarily high dimensions.

#### [nanoflann](https://github.com/jlblancoc/nanoflann)
[![Watchers](https://img.shields.io/github/watchers/jlblancoc/nanoflann)](Watchers) [![Stars](https://img.shields.io/github/stars/jlblancoc/nanoflann)](Stars) [![Forks](https://img.shields.io/github/forks/jlblancoc/nanoflann)](Forks) [![License](https://img.shields.io/github/license/jlblancoc/nanoflann)](LICENSE)

A C++11 header-only library for Nearest Neighbor (NN) search with KD-trees.

### Collision

#### [fcl-Flexible Collision Library](https://github.com/flexible-collision-library/fcl)
[![Watchers](https://img.shields.io/github/watchers/flexible-collision-library/fcl)](Watchers) [![Stars](https://img.shields.io/github/stars/flexible-collision-library/fcl)](Stars) [![Forks](https://img.shields.io/github/forks/flexible-collision-library/fcl)](Forks) [![License](https://img.shields.io/github/license/flexible-collision-library/fcl)](LICENSE)

FCL is a library for performing three types of proximity queries on a pair of geometric models composed of triangles.

### Others

#### [quickhull](https://github.com/akuukka/quickhull)
[![Watchers](https://img.shields.io/github/watchers/akuukka/quickhull)](Watchers) [![Stars](https://img.shields.io/github/stars/akuukka/quickhull)](Stars) [![Forks](https://img.shields.io/github/forks/akuukka/quickhull)](Forks) [![License](https://img.shields.io/github/license/akuukka/quickhull)](LICENSE)

C++ implementation of the 3D QuickHull algorithm.

#### [Cork Boolean Library](https://github.com/gilbo/cork)
[![Watchers](https://img.shields.io/github/watchers/gilbo/cork)](Watchers) [![Stars](https://img.shields.io/github/stars/gilbo/cork)](Stars) [![Forks](https://img.shields.io/github/forks/gilbo/cork)](Forks) [![License](https://img.shields.io/github/license/gilbo/cork)](LICENSE)

Cork is designed to support Boolean operations between triangle meshes.


## [Back to Top](#table-of-contents)
