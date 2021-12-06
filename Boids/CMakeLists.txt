cmake_minimum_required(VERSION 3.16)
project(Boids)

set(EXECUTABLE_NAME ${PROJECT_NAME}_run)

set(CMAKE_CXX_STANDARD 14)

add_executable(${EXECUTABLE_NAME} main.cpp Boids.h Boid.h)

message(${CMAKE_SOURCE_DIR})

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake_modules" ${CMAKE_MODULE_PATH})
find_package(SFML 2 REQUIRED system window graphics)

if (SFML_FOUND)
    include_directories(${SFML_INCLUDE_DIR})
    target_link_libraries(${EXECUTABLE_NAME} ${SFML_LIBRARIES} ${SFML_DEPENDENCIES})
endif()