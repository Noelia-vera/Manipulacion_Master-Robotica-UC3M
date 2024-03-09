// Generated by gencpp from file graspit_interface/GetBody.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_GETBODY_H
#define GRASPIT_INTERFACE_MESSAGE_GETBODY_H

#include <ros/service_traits.h>


#include <graspit_interface/GetBodyRequest.h>
#include <graspit_interface/GetBodyResponse.h>


namespace graspit_interface
{

struct GetBody
{

typedef GetBodyRequest Request;
typedef GetBodyResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetBody
} // namespace graspit_interface


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::graspit_interface::GetBody > {
  static const char* value()
  {
    return "b5f0921777cf671340b9c6535008ff4e";
  }

  static const char* value(const ::graspit_interface::GetBody&) { return value(); }
};

template<>
struct DataType< ::graspit_interface::GetBody > {
  static const char* value()
  {
    return "graspit_interface/GetBody";
  }

  static const char* value(const ::graspit_interface::GetBody&) { return value(); }
};


// service_traits::MD5Sum< ::graspit_interface::GetBodyRequest> should match
// service_traits::MD5Sum< ::graspit_interface::GetBody >
template<>
struct MD5Sum< ::graspit_interface::GetBodyRequest>
{
  static const char* value()
  {
    return MD5Sum< ::graspit_interface::GetBody >::value();
  }
  static const char* value(const ::graspit_interface::GetBodyRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::graspit_interface::GetBodyRequest> should match
// service_traits::DataType< ::graspit_interface::GetBody >
template<>
struct DataType< ::graspit_interface::GetBodyRequest>
{
  static const char* value()
  {
    return DataType< ::graspit_interface::GetBody >::value();
  }
  static const char* value(const ::graspit_interface::GetBodyRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::graspit_interface::GetBodyResponse> should match
// service_traits::MD5Sum< ::graspit_interface::GetBody >
template<>
struct MD5Sum< ::graspit_interface::GetBodyResponse>
{
  static const char* value()
  {
    return MD5Sum< ::graspit_interface::GetBody >::value();
  }
  static const char* value(const ::graspit_interface::GetBodyResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::graspit_interface::GetBodyResponse> should match
// service_traits::DataType< ::graspit_interface::GetBody >
template<>
struct DataType< ::graspit_interface::GetBodyResponse>
{
  static const char* value()
  {
    return DataType< ::graspit_interface::GetBody >::value();
  }
  static const char* value(const ::graspit_interface::GetBodyResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_GETBODY_H