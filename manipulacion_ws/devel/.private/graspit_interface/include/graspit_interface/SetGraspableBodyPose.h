// Generated by gencpp from file graspit_interface/SetGraspableBodyPose.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_SETGRASPABLEBODYPOSE_H
#define GRASPIT_INTERFACE_MESSAGE_SETGRASPABLEBODYPOSE_H

#include <ros/service_traits.h>


#include <graspit_interface/SetGraspableBodyPoseRequest.h>
#include <graspit_interface/SetGraspableBodyPoseResponse.h>


namespace graspit_interface
{

struct SetGraspableBodyPose
{

typedef SetGraspableBodyPoseRequest Request;
typedef SetGraspableBodyPoseResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetGraspableBodyPose
} // namespace graspit_interface


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::graspit_interface::SetGraspableBodyPose > {
  static const char* value()
  {
    return "6f869681a43e0646852b48a974e19787";
  }

  static const char* value(const ::graspit_interface::SetGraspableBodyPose&) { return value(); }
};

template<>
struct DataType< ::graspit_interface::SetGraspableBodyPose > {
  static const char* value()
  {
    return "graspit_interface/SetGraspableBodyPose";
  }

  static const char* value(const ::graspit_interface::SetGraspableBodyPose&) { return value(); }
};


// service_traits::MD5Sum< ::graspit_interface::SetGraspableBodyPoseRequest> should match
// service_traits::MD5Sum< ::graspit_interface::SetGraspableBodyPose >
template<>
struct MD5Sum< ::graspit_interface::SetGraspableBodyPoseRequest>
{
  static const char* value()
  {
    return MD5Sum< ::graspit_interface::SetGraspableBodyPose >::value();
  }
  static const char* value(const ::graspit_interface::SetGraspableBodyPoseRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::graspit_interface::SetGraspableBodyPoseRequest> should match
// service_traits::DataType< ::graspit_interface::SetGraspableBodyPose >
template<>
struct DataType< ::graspit_interface::SetGraspableBodyPoseRequest>
{
  static const char* value()
  {
    return DataType< ::graspit_interface::SetGraspableBodyPose >::value();
  }
  static const char* value(const ::graspit_interface::SetGraspableBodyPoseRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::graspit_interface::SetGraspableBodyPoseResponse> should match
// service_traits::MD5Sum< ::graspit_interface::SetGraspableBodyPose >
template<>
struct MD5Sum< ::graspit_interface::SetGraspableBodyPoseResponse>
{
  static const char* value()
  {
    return MD5Sum< ::graspit_interface::SetGraspableBodyPose >::value();
  }
  static const char* value(const ::graspit_interface::SetGraspableBodyPoseResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::graspit_interface::SetGraspableBodyPoseResponse> should match
// service_traits::DataType< ::graspit_interface::SetGraspableBodyPose >
template<>
struct DataType< ::graspit_interface::SetGraspableBodyPoseResponse>
{
  static const char* value()
  {
    return DataType< ::graspit_interface::SetGraspableBodyPose >::value();
  }
  static const char* value(const ::graspit_interface::SetGraspableBodyPoseResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_SETGRASPABLEBODYPOSE_H
