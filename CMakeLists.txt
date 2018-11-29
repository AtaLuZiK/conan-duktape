cmake_minimum_required (VERSION 2.8.12)
project (duktape C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(duktape
    ${CMAKE_CURRENT_SOURCE_DIR}/src/duk_config.h
    ${CMAKE_CURRENT_SOURCE_DIR}/src/duktape.h
    ${CMAKE_CURRENT_SOURCE_DIR}/src/duktape.c
)

add_executable(duk
    ${CMAKE_CURRENT_SOURCE_DIR}/src/duktape.c
    ${CMAKE_CURRENT_SOURCE_DIR}/examples/cmdline/duk_cmdline.c
    ${CMAKE_CURRENT_SOURCE_DIR}/extras/print-alert/duk_print_alert.c
    ${CMAKE_CURRENT_SOURCE_DIR}/extras/console/duk_console.c
    ${CMAKE_CURRENT_SOURCE_DIR}/extras/logging/duk_logging.c
    ${CMAKE_CURRENT_SOURCE_DIR}/extras/module-duktape/duk_module_duktape.c
)
target_compile_definitions(duk
    PRIVATE DUK_CMDLINE_PRINTALERT_SUPPORT
    PRIVATE DUK_CMDLINE_CONSOLE_SUPPORT
    PRIVATE DUK_CMDLINE_LOGGING_SUPPORT
    PRIVATE DUK_CMDLINE_MODULE_SUPPORT
)
target_include_directories(duk
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/extras/print-alert
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/extras/console
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/extras/logging
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/extras/module-duktape
)
