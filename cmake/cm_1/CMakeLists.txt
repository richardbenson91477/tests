cmake_minimum_required (VERSION 2.6)
project (cm_1)
# The version number.
set (cm_1_VERSION_MAJOR 1)
set (cm_1_VERSION_MINOR 0)
set (emoji_man "\"ᕕ( ᐛ )ᕗ\"")

# configure a header file to pass some of the CMake settings
configure_file (
  "${PROJECT_SOURCE_DIR}/cm_1_conf.h.in"
  "${PROJECT_BINARY_DIR}/cm_1_conf.h"
)

# add the binary tree to the search path for include files
include_directories("${PROJECT_BINARY_DIR}")

# add the executable
add_executable(cm_1 cm_1.cxx)

