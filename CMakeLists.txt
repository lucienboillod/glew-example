cmake_minimum_required(VERSION 2.8.11)
project(glew_example)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(conanbuildinfo.cmake)
conan_basic_setup()

find_package(Glew REQUIRED)

add_executable(${PROJECT_NAME} example.cc)
target_link_libraries(${PROJECT_NAME} ${GLEW_LIBRARY})

install(TARGETS ${PROJECT_NAME}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
