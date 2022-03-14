cmake_minimum_required(VERSION "3.23.0-rc1")

project("HelloWorld")
# Set the output folder where your program will be created
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_executable("${PROJECT_NAME}" "hello_world.cpp")
install(TARGETS ${PROJECT_NAME} RUNTIME DESTINATION bin)

set(CPACK_PACKAGE_NAME "HelloWorld")
set(CPACK_PACKAGE_VERSION_MAJOR 1)
set(CPACK_PACKAGE_VERSION_MINOR 0)
set(CPACK_PACKAGE_VERSION_PATCH 0)
set(CPACK_INSTALL_SCRIPT ${CMAKE_SOURCE_DIR}/DoSomething.cmake)
include(CPack)


