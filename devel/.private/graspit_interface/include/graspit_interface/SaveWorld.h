// Generated by gencpp from file graspit_interface/SaveWorld.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_SAVEWORLD_H
#define GRASPIT_INTERFACE_MESSAGE_SAVEWORLD_H

#include <ros/service_traits.h>


#include <graspit_interface/SaveWorldRequest.h>
#include <graspit_interface/SaveWorldResponse.h>


namespace graspit_interface
{

struct SaveWorld
{

typedef SaveWorldRequest Request;
typedef SaveWorldResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SaveWorld
} // namespace graspit_interface


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::graspit_interface::SaveWorld > {
  static const char* value()
  {
    return "285e9fabd629899a63d0043517ce4bae";
  }

  static const char* value(const ::graspit_interface::SaveWorld&) { return value(); }
};

template<>
struct DataType< ::graspit_interface::SaveWorld > {
  static const char* value()
  {
    return "graspit_interface/SaveWorld";
  }

  static const char* value(const ::graspit_interface::SaveWorld&) { return value(); }
};


// service_traits::MD5Sum< ::graspit_interface::SaveWorldRequest> should match
// service_traits::MD5Sum< ::graspit_interface::SaveWorld >
template<>
struct MD5Sum< ::graspit_interface::SaveWorldRequest>
{
  static const char* value()
  {
    return MD5Sum< ::graspit_interface::SaveWorld >::value();
  }
  static const char* value(const ::graspit_interface::SaveWorldRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::graspit_interface::SaveWorldRequest> should match
// service_traits::DataType< ::graspit_interface::SaveWorld >
template<>
struct DataType< ::graspit_interface::SaveWorldRequest>
{
  static const char* value()
  {
    return DataType< ::graspit_interface::SaveWorld >::value();
  }
  static const char* value(const ::graspit_interface::SaveWorldRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::graspit_interface::SaveWorldResponse> should match
// service_traits::MD5Sum< ::graspit_interface::SaveWorld >
template<>
struct MD5Sum< ::graspit_interface::SaveWorldResponse>
{
  static const char* value()
  {
    return MD5Sum< ::graspit_interface::SaveWorld >::value();
  }
  static const char* value(const ::graspit_interface::SaveWorldResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::graspit_interface::SaveWorldResponse> should match
// service_traits::DataType< ::graspit_interface::SaveWorld >
template<>
struct DataType< ::graspit_interface::SaveWorldResponse>
{
  static const char* value()
  {
    return DataType< ::graspit_interface::SaveWorld >::value();
  }
  static const char* value(const ::graspit_interface::SaveWorldResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_SAVEWORLD_H
