cmake_minimum_required(VERSION 3.1)
project(MinMax-Checker CXX)

set(CMAKE_CXX_STANDARD 17)

# Setup
set(CODE_DIR ${CMAKE_SOURCE_DIR}/code)
file(GLOB_RECURSE SOURCE LIST_DIRECTORY true ${CODE_DIR}/*.cpp)

add_executable(${PROJECT_NAME} ${SOURCE})

target_include_directories(${PROJECT_NAME} PRIVATE ${CODE_DIR})