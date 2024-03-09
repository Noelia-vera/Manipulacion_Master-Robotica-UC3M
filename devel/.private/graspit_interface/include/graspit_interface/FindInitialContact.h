// Generated by gencpp from file graspit_interface/FindInitialContact.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_FINDINITIALCONTACT_H
#define GRASPIT_INTERFACE_MESSAGE_FINDINITIALCONTACT_H

#include <ros/service_traits.h>


#include <graspit_interface/FindInitialContactRequest.h>
#include <graspit_interface/FindInitialContactResponse.h>


namespace graspit_interface
{

struct FindInitialContact
{

typedef FindInitialContactRequest Request;
typedef FindInitialContactResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct FindInitialContact
} // namespace graspit_interface


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::graspit_interface::FindInitialContact > {
  static const char* value()
  {
    return "fdb119775186f8935d45786efba6c6a8";
  }

  static const char* value(const ::graspit_interface::FindInitialContact&) { return value(); }
};

template<>
struct DataType< ::graspit_interface::FindInitialContact > {
  static const char* value()
  {
    return "graspit_interface/FindInitialContact";
  }

  static const char* value(const ::graspit_interface::FindInitialContact&) { return value(); }
};


// service_traits::MD5Sum< ::graspit_interface::FindInitialContactRequest> should match
// service_traits::MD5Sum< ::graspit_interface::FindInitialContact >
template<>
struct MD5Sum< ::graspit_interface::FindInitialContactRequest>
{
  static const char* value()
  {
    return MD5Sum< ::graspit_interface::FindInitialContact >::value();
  }
  static const char* value(const ::graspit_interface::FindInitialContactRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::graspit_interface::FindInitialContactRequest> should match
// service_traits::DataType< ::graspit_interface::FindInitialContact >
template<>
struct DataType< ::graspit_interface::FindInitialContactRequest>
{
  static const char* value()
  {
    return DataType< ::graspit_interface::FindInitialContact >::value();
  }
  static const char* value(const ::graspit_interface::FindInitialContactRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::graspit_interface::FindInitialContactResponse> should match
// service_traits::MD5Sum< ::graspit_interface::FindInitialContact >
template<>
struct MD5Sum< ::graspit_interface::FindInitialContactResponse>
{
  static const char* value()
  {
    return MD5Sum< ::graspit_interface::FindInitialContact >::value();
  }
  static const char* value(const ::graspit_interface::FindInitialContactResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::graspit_interface::FindInitialContactResponse> should match
// service_traits::DataType< ::graspit_interface::FindInitialContact >
template<>
struct DataType< ::graspit_interface::FindInitialContactResponse>
{
  static const char* value()
  {
    return DataType< ::graspit_interface::FindInitialContact >::value();
  }
  static const char* value(const ::graspit_interface::FindInitialContactResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_FINDINITIALCONTACT_H
