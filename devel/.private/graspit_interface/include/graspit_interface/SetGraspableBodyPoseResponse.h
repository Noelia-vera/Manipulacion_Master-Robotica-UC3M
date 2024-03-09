// Generated by gencpp from file graspit_interface/SetGraspableBodyPoseResponse.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_SETGRASPABLEBODYPOSERESPONSE_H
#define GRASPIT_INTERFACE_MESSAGE_SETGRASPABLEBODYPOSERESPONSE_H


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
struct SetGraspableBodyPoseResponse_
{
  typedef SetGraspableBodyPoseResponse_<ContainerAllocator> Type;

  SetGraspableBodyPoseResponse_()
    : result(0)  {
    }
  SetGraspableBodyPoseResponse_(const ContainerAllocator& _alloc)
    : result(0)  {
  (void)_alloc;
    }



   typedef uint8_t _result_type;
  _result_type result;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(RESULT_SUCCESS)
  #undef RESULT_SUCCESS
#endif
#if defined(_WIN32) && defined(RESULT_INVALID_ID)
  #undef RESULT_INVALID_ID
#endif
#if defined(_WIN32) && defined(RESULT_INVALID_POSE)
  #undef RESULT_INVALID_POSE
#endif
#if defined(_WIN32) && defined(RESULT_BODY_IN_COLLISION)
  #undef RESULT_BODY_IN_COLLISION
#endif

  enum {
    RESULT_SUCCESS = 0u,
    RESULT_INVALID_ID = 1u,
    RESULT_INVALID_POSE = 2u,
    RESULT_BODY_IN_COLLISION = 3u,
  };


  typedef boost::shared_ptr< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> const> ConstPtr;

}; // struct SetGraspableBodyPoseResponse_

typedef ::graspit_interface::SetGraspableBodyPoseResponse_<std::allocator<void> > SetGraspableBodyPoseResponse;

typedef boost::shared_ptr< ::graspit_interface::SetGraspableBodyPoseResponse > SetGraspableBodyPoseResponsePtr;
typedef boost::shared_ptr< ::graspit_interface::SetGraspableBodyPoseResponse const> SetGraspableBodyPoseResponseConstPtr;

// constants requiring out of line definition

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator1> & lhs, const ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator2> & rhs)
{
  return lhs.result == rhs.result;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator1> & lhs, const ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace graspit_interface

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "de5a8e8b8fd4f59325ce002a311c962f";
  }

  static const char* value(const ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xde5a8e8b8fd4f593ULL;
  static const uint64_t static_value2 = 0x25ce002a311c962fULL;
};

template<class ContainerAllocator>
struct DataType< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "graspit_interface/SetGraspableBodyPoseResponse";
  }

  static const char* value(const ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 RESULT_SUCCESS           = 0\n"
"uint8 RESULT_INVALID_ID        = 1\n"
"uint8 RESULT_INVALID_POSE      = 2\n"
"uint8 RESULT_BODY_IN_COLLISION = 3\n"
"\n"
"uint8 result\n"
"\n"
;
  }

  static const char* value(const ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetGraspableBodyPoseResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::graspit_interface::SetGraspableBodyPoseResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_SETGRASPABLEBODYPOSERESPONSE_H
