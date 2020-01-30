#!/usr/bin/python3

from setuptools import setup, find_packages, Extension

setup(name="aurauas_navigation",
      version="1.4",
      description="Navigation Tools",
      author="Curtis L. Olson",
      author_email="curtolson@flightgear.org",
      url="https://github.com/AuraUAS",
      #py_modules=["props", "props_json", "props_xml"],
      #package_dir = {"": "lib"},
      packages = find_packages(),
      ext_modules=[
          Extension("aurauas_navigation.structs",
                    define_macros=[("HAVE_PYBIND11", "1")],
                    sources=["src/nav_common/structs.cxx"],
                    depends=["src/nav_common/structs.hxx"]),
          Extension("aurauas_navigation.ekf15",
                    sources=["src/nav_ekf15/pybind11.cxx",
                             "src/nav_ekf15/EKF_15state.cxx",
                             "src/nav_common/nav_functions_float.cxx"],
                    depends=["src/nav_ekf15/EKF_15state.hxx",
                             "src/nav_common/constants.hxx",
                             "src/nav_common/nav_functions_float.hxx"]),
          Extension("aurauas_navigation.ekf15_mag",
                    sources=["src/nav_ekf15_mag/pybind11.cxx",
                             "src/nav_ekf15_mag/EKF_15state.cxx",
                             "src/nav_common/nav_functions_float.cxx",
                             "src/nav_common/coremag.c"],
                    depends=["src/nav_ekf15_mag/EKF_15state.hxx",
                             "src/nav_common/constants.hxx",
                             "src/nav_common/nav_functions_float.hxx",
                             "src/nav_common/coremag.h"]),
          Extension("aurauas_navigation.openloop",
                    sources=["src/nav_openloop/pybind11.cxx",
                             "src/nav_openloop/openloop.cxx",
                             "src/nav_openloop/glocal.cxx",
                             "src/nav_common/nav_functions_float.cxx",
                             "src/nav_common/coremag.c"],
                    depends=["src/nav_openloop/openloop.hxx",
                             "src/nav_openloop/glocal.hxx",
                             "src/nav_common/constants.hxx",
                             "src/nav_common/nav_functions_float.hxx",
                             "src/nav_common/coremag.h"]),
          Extension("aurauas_navigation.uNavINS",
                    include_dirs=["/usr/include/eigen3"],
                    sources=["src/UASLab_RAPTRS/pybind11.cxx",
                             "src/UASLab_RAPTRS/nav-functions.cpp",
                             "src/UASLab_RAPTRS/uNavINS.cpp"],
                    depends=["src/UASLab_RAPTRS/nav-functions.h",
                             "src/UASLab_RAPTRS/uNavINS.h"]),
          Extension("aurauas_navigation.uNavINS_BFS",
                    include_dirs=["/usr/include/eigen3"],
                    sources=["src/BFS_raptrs/pybind11.cxx",
                             "src/BFS_raptrs/uNavINS.cpp"],
                    depends=["src/BFS_raptrs/uNavINS.h"])
      ],
     )
