// Generated by gencpp from file graspit_interface/GetGraspableBody.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_GETGRASPABLEBODY_H
#define GRASPIT_INTERFACE_MESSAGE_GETGRASPABLEBODY_H

#include <ros/service_traits.h>


#include <graspit_interface/GetGraspableBodyRequest.h>
#include <graspit_interface/GetGraspableBodyResponse.h>


namespace graspit_interface
{

struct GetGraspableBody
{

typedef GetGraspableBodyRequest Request;
typedef GetGraspableBodyResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetGraspableBody
} // namespace graspit_interface


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::graspit_interface::GetGraspableBody > {
  static const char* value()
  {
    return "218c3a98036ba7fa42afdff3e6384346";
  }

  static const char* value(const ::graspit_interface::GetGraspableBody&) { return value(); }
};

template<>
struct DataType< ::graspit_interface::GetGraspableBody > {
  static const char* value()
  {
    return "graspit_interface/GetGraspableBody";
  }

  static const char* value(const ::graspit_interface::GetGraspableBody&) { return value(); }
};


// service_traits::MD5Sum< ::graspit_interface::GetGraspableBodyRequest> should match
// service_traits::MD5Sum< ::graspit_interface::GetGraspableBody >
template<>
struct MD5Sum< ::graspit_interface::GetGraspableBodyRequest>
{
  static const char* value()
  {
    return MD5Sum< ::graspit_interface::GetGraspableBody >::value();
  }
  static const char* value(const ::graspit_interface::GetGraspableBodyRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::graspit_interface::GetGraspableBodyRequest> should match
// service_traits::DataType< ::graspit_interface::GetGraspableBody >
template<>
struct DataType< ::graspit_interface::GetGraspableBodyRequest>
{
  static const char* value()
  {
    return DataType< ::graspit_interface::GetGraspableBody >::value();
  }
  static const char* value(const ::graspit_interface::GetGraspableBodyRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::graspit_interface::GetGraspableBodyResponse> should match
// service_traits::MD5Sum< ::graspit_interface::GetGraspableBody >
template<>
struct MD5Sum< ::graspit_interface::GetGraspableBodyResponse>
{
  static const char* value()
  {
    return MD5Sum< ::graspit_interface::GetGraspableBody >::value();
  }
  static const char* value(const ::graspit_interface::GetGraspableBodyResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::graspit_interface::GetGraspableBodyResponse> should match
// service_traits::DataType< ::graspit_interface::GetGraspableBody >
template<>
struct DataType< ::graspit_interface::GetGraspableBodyResponse>
{
  static const char* value()
  {
    return DataType< ::graspit_interface::GetGraspableBody >::value();
  }
  static const char* value(const ::graspit_interface::GetGraspableBodyResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_GETGRASPABLEBODY_H
