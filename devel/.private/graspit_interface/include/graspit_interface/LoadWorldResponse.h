// Generated by gencpp from file graspit_interface/LoadWorldResponse.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_LOADWORLDRESPONSE_H
#define GRASPIT_INTERFACE_MESSAGE_LOADWORLDRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace graspit_interface
{
template <class ContainerAllocator>
struct LoadWorldResponse_
{
  typedef LoadWorldResponse_<ContainerAllocator> Type;

  LoadWorldResponse_()
    : result(0)  {
    }
  LoadWorldResponse_(const ContainerAllocator& _alloc)
    : result(0)  {
  (void)_alloc;
    }



   typedef uint8_t _result_type;
  _result_type result;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(RESULT_SUCCESS)
  #undef RESULT_SUCCESS
#endif
#if defined(_WIN32) && defined(RESULT_FAILURE)
  #undef RESULT_FAILURE
#endif

  enum {
    RESULT_SUCCESS = 0u,
    RESULT_FAILURE = 1u,
  };


  typedef boost::shared_ptr< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> const> ConstPtr;

}; // struct LoadWorldResponse_

typedef ::graspit_interface::LoadWorldResponse_<std::allocator<void> > LoadWorldResponse;

typedef boost::shared_ptr< ::graspit_interface::LoadWorldResponse > LoadWorldResponsePtr;
typedef boost::shared_ptr< ::graspit_interface::LoadWorldResponse const> LoadWorldResponseConstPtr;

// constants requiring out of line definition

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::graspit_interface::LoadWorldResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::graspit_interface::LoadWorldResponse_<ContainerAllocator1> & lhs, const ::graspit_interface::LoadWorldResponse_<ContainerAllocator2> & rhs)
{
  return lhs.result == rhs.result;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::graspit_interface::LoadWorldResponse_<ContainerAllocator1> & lhs, const ::graspit_interface::LoadWorldResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace graspit_interface

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "97cab54dd6dbe9e837f2d3a5a24e81f8";
  }

  static const char* value(const ::graspit_interface::LoadWorldResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x97cab54dd6dbe9e8ULL;
  static const uint64_t static_value2 = 0x37f2d3a5a24e81f8ULL;
};

template<class ContainerAllocator>
struct DataType< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "graspit_interface/LoadWorldResponse";
  }

  static const char* value(const ::graspit_interface::LoadWorldResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 RESULT_SUCCESS    = 0\n"
"uint8 RESULT_FAILURE    = 1\n"
"\n"
"uint8 result\n"
;
  }

  static const char* value(const ::graspit_interface::LoadWorldResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct LoadWorldResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::graspit_interface::LoadWorldResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::graspit_interface::LoadWorldResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_LOADWORLDRESPONSE_H
