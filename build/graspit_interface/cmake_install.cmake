# Install script for directory: /home/noelia/manipulacion_ws/src/graspit_interface

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/noelia/manipulacion_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/noelia/manipulacion_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/noelia/manipulacion_ws/install" TYPE PROGRAM FILES "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/noelia/manipulacion_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/noelia/manipulacion_ws/install" TYPE PROGRAM FILES "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/noelia/manipulacion_ws/install/setup.bash;/home/noelia/manipulacion_ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/noelia/manipulacion_ws/install" TYPE FILE FILES
    "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/setup.bash"
    "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/noelia/manipulacion_ws/install/setup.sh;/home/noelia/manipulacion_ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/noelia/manipulacion_ws/install" TYPE FILE FILES
    "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/setup.sh"
    "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/noelia/manipulacion_ws/install/setup.zsh;/home/noelia/manipulacion_ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/noelia/manipulacion_ws/install" TYPE FILE FILES
    "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/setup.zsh"
    "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/noelia/manipulacion_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/noelia/manipulacion_ws/install" TYPE FILE FILES "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/.rosinstall")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graspit_interface/msg" TYPE FILE FILES
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/Body.msg"
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/GraspableBody.msg"
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/Robot.msg"
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/TactileSensorData.msg"
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/Grasp.msg"
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/Planner.msg"
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/SearchSpace.msg"
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/SearchContact.msg"
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/Energy.msg"
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/Contact.msg"
    "/home/noelia/manipulacion_ws/src/graspit_interface/msg/SimAnnParams.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graspit_interface/srv" TYPE FILE FILES
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/GetRobot.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/GetGraspableBody.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/GetBody.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/GetBodies.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/GetRobots.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/GetGraspableBodies.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/SetGraspableBodyPose.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/SetRobotPose.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/SetBodyPose.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/GetDynamics.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/SetDynamics.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/SetRobotDesiredDOF.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/ForceRobotDOF.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/MoveDOFToContacts.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/AutoGrasp.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/AutoOpen.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/ImportRobot.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/ImportObstacle.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/ImportGraspableBody.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/LoadWorld.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/SaveWorld.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/ClearWorld.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/SaveImage.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/ToggleAllCollisions.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/ComputeQuality.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/ComputeEnergy.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/ApproachToContact.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/FindInitialContact.srv"
    "/home/noelia/manipulacion_ws/src/graspit_interface/srv/DynamicAutoGraspComplete.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graspit_interface/action" TYPE FILE FILES "/home/noelia/manipulacion_ws/src/graspit_interface/action/PlanGrasps.action")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graspit_interface/msg" TYPE FILE FILES
    "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/share/graspit_interface/msg/PlanGraspsAction.msg"
    "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/share/graspit_interface/msg/PlanGraspsActionGoal.msg"
    "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/share/graspit_interface/msg/PlanGraspsActionResult.msg"
    "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/share/graspit_interface/msg/PlanGraspsActionFeedback.msg"
    "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/share/graspit_interface/msg/PlanGraspsGoal.msg"
    "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/share/graspit_interface/msg/PlanGraspsResult.msg"
    "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/share/graspit_interface/msg/PlanGraspsFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graspit_interface/cmake" TYPE FILE FILES "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/graspit_interface-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/include/graspit_interface")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/share/roseus/ros/graspit_interface")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/share/common-lisp/ros/graspit_interface")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/share/gennodejs/ros/graspit_interface")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/lib/python3/dist-packages/graspit_interface")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/noelia/manipulacion_ws/devel/.private/graspit_interface/lib/python3/dist-packages/graspit_interface")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/graspit_interface.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graspit_interface/cmake" TYPE FILE FILES "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/graspit_interface-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graspit_interface/cmake" TYPE FILE FILES
    "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/graspit_interfaceConfig.cmake"
    "/home/noelia/manipulacion_ws/build/graspit_interface/catkin_generated/installspace/graspit_interfaceConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/graspit_interface" TYPE FILE FILES "/home/noelia/manipulacion_ws/src/graspit_interface/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/noelia/manipulacion_ws/build/graspit_interface/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
