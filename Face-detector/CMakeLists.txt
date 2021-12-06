cmake_minimum_required(VERSION 3.16)
project(FaceDetector)

set(CMAKE_CXX_STANDARD 14)

file(GLOB SOURCES
        ${PROJECT_SOURCE_DIR}/source/*.cpp
        ${PROJECT_SOURCE_DIR}/include/*.h)

add_executable(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PRIVATE ${PROJECT_SOURCE_DIR}/include)

# OpenCV setup
find_package(OpenCV REQUIRED)
if (OpenCV_LIBS)
    target_include_directories(${PROJECT_NAME} PRIVATE ${OpenCV_INCLUDE_DIRS})
    target_link_libraries(${PROJECT_NAME} PRIVATE ${OpenCV_LIBS})
else()
    message(FATAL_ERROR "Cannot find OpenCV library on PC")
endif()

# DNN configuration files
set(FACE_DETECTION_CONFIGURATION "${PROJECT_SOURCE_DIR}/assets/deploy.prototxt")
set(FACE_DETECTION_WEIGHTS "${PROJECT_SOURCE_DIR}/assets/res10_300x300_ssd_iter_140000_fp16.caffemodel")
set(FACE_DETECTION_HAARCASCADE "${PROJECT_SOURCE_DIR}/assets/haarcascades/haarcascade_frontalface_alt2.xml")

if (EXISTS "${FACE_DETECTION_CONFIGURATION}")
    target_compile_definitions(${PROJECT_NAME} PRIVATE FACE_DETECTION_CONFIGURATION="${FACE_DETECTION_CONFIGURATION}")
else()
    message(FATAL_ERROR "Cannot find file ${FACE_DETECTION_CONFIGURATION} on PC")
endif()

if (EXISTS "${FACE_DETECTION_WEIGHTS}")
    target_compile_definitions(${PROJECT_NAME} PRIVATE FACE_DETECTION_WEIGHTS="${FACE_DETECTION_WEIGHTS}")
else()
    message(FATAL_ERROR "Cannot find file ${FACE_DETECTION_WEIGHTS} on PC")
endif()

if (EXISTS "${FACE_DETECTION_HAARCASCADE}")
    target_compile_definitions(${PROJECT_NAME} PRIVATE FACE_DETECTION_HAARCASCADE="${FACE_DETECTION_HAARCASCADE}")
else()
    message(FATAL_ERROR "Cannot find file ${FACE_DETECTION_HAARCASCADE} on PC")
endif()