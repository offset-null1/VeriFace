# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/daksh/VeriFace/backend/model

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/daksh/VeriFace/backend/model/build

# Include any dependencies generated for this target.
include CMakeFiles/loss.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/loss.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/loss.dir/flags.make

CMakeFiles/loss.dir/loss.cpp.o: CMakeFiles/loss.dir/flags.make
CMakeFiles/loss.dir/loss.cpp.o: ../loss.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/daksh/VeriFace/backend/model/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/loss.dir/loss.cpp.o"
	/usr/bin/g++-7  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/loss.dir/loss.cpp.o -c /home/daksh/VeriFace/backend/model/loss.cpp

CMakeFiles/loss.dir/loss.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/loss.dir/loss.cpp.i"
	/usr/bin/g++-7 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/daksh/VeriFace/backend/model/loss.cpp > CMakeFiles/loss.dir/loss.cpp.i

CMakeFiles/loss.dir/loss.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/loss.dir/loss.cpp.s"
	/usr/bin/g++-7 $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/daksh/VeriFace/backend/model/loss.cpp -o CMakeFiles/loss.dir/loss.cpp.s

CMakeFiles/loss.dir/loss.cpp.o.requires:

.PHONY : CMakeFiles/loss.dir/loss.cpp.o.requires

CMakeFiles/loss.dir/loss.cpp.o.provides: CMakeFiles/loss.dir/loss.cpp.o.requires
	$(MAKE) -f CMakeFiles/loss.dir/build.make CMakeFiles/loss.dir/loss.cpp.o.provides.build
.PHONY : CMakeFiles/loss.dir/loss.cpp.o.provides

CMakeFiles/loss.dir/loss.cpp.o.provides.build: CMakeFiles/loss.dir/loss.cpp.o


# Object files for target loss
loss_OBJECTS = \
"CMakeFiles/loss.dir/loss.cpp.o"

# External object files for target loss
loss_EXTERNAL_OBJECTS =

loss: CMakeFiles/loss.dir/loss.cpp.o
loss: CMakeFiles/loss.dir/build.make
loss: /home/daksh/libtorch/lib/libtorch.so
loss: /home/daksh/libtorch/lib/libc10.so
loss: /usr/lib/x86_64-linux-gnu/libcuda.so
loss: /usr/lib/x86_64-linux-gnu/libnvrtc.so
loss: /usr/lib/x86_64-linux-gnu/libnvToolsExt.so
loss: /usr/local/cuda-11.0/lib64/libcudart.so
loss: /home/daksh/libtorch/lib/libc10_cuda.so
loss: /home/daksh/libtorch/lib/libc10_cuda.so
loss: /home/daksh/libtorch/lib/libc10.so
loss: /usr/local/cuda/lib64/libnvToolsExt.so
loss: /usr/local/cuda/lib64/libcudart.so
loss: /usr/local/cuda-11.0/lib64/libcufft.so
loss: /usr/local/cuda-11.0/lib64/libcurand.so
loss: /usr/local/cuda-11.0/lib64/libcudnn.so
loss: /usr/local/cuda/lib64/libculibos.a
loss: /usr/local/cuda/lib64/libculibos.a
loss: /usr/local/cuda-11.0/lib64/libcublas.so
loss: /usr/local/cuda-11.0/lib64/libcudart.so
loss: CMakeFiles/loss.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/daksh/VeriFace/backend/model/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable loss"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/loss.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/loss.dir/build: loss

.PHONY : CMakeFiles/loss.dir/build

CMakeFiles/loss.dir/requires: CMakeFiles/loss.dir/loss.cpp.o.requires

.PHONY : CMakeFiles/loss.dir/requires

CMakeFiles/loss.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/loss.dir/cmake_clean.cmake
.PHONY : CMakeFiles/loss.dir/clean

CMakeFiles/loss.dir/depend:
	cd /home/daksh/VeriFace/backend/model/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/daksh/VeriFace/backend/model /home/daksh/VeriFace/backend/model /home/daksh/VeriFace/backend/model/build /home/daksh/VeriFace/backend/model/build /home/daksh/VeriFace/backend/model/build/CMakeFiles/loss.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/loss.dir/depend

