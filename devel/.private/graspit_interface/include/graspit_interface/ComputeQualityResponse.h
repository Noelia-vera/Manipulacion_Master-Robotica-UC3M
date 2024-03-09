// Generated by gencpp from file graspit_interface/ComputeQualityResponse.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_COMPUTEQUALITYRESPONSE_H
#define GRASPIT_INTERFACE_MESSAGE_COMPUTEQUALITYRESPONSE_H


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
struct ComputeQualityResponse_
{
  typedef ComputeQualityResponse_<ContainerAllocator> Type;

  ComputeQualityResponse_()
    : result(0)
    , volume(0.0)
    , epsilon(0.0)  {
    }
  ComputeQualityResponse_(const ContainerAllocator& _alloc)
    : result(0)
    , volume(0.0)
    , epsilon(0.0)  {
  (void)_alloc;
    }



   typedef uint8_t _result_type;
  _result_type result;

   typedef double _volume_type;
  _volume_type volume;

   typedef double _epsilon_type;
  _epsilon_type epsilon;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(RESULT_SUCCESS)
  #undef RESULT_SUCCESS
#endif
#if defined(_WIN32) && defined(RESULT_INVALID_ID)
  #undef RESULT_INVALID_ID
#endif
#if defined(_WIN32) && defined(RESULT_COLLISION)
  #undef RESULT_COLLISION
#endif

  enum {
    RESULT_SUCCESS = 0u,
    RESULT_INVALID_ID = 1u,
    RESULT_COLLISION = 2u,
  };


  typedef boost::shared_ptr< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> const> ConstPtr;

}; // struct ComputeQualityResponse_

typedef ::graspit_interface::ComputeQualityResponse_<std::allocator<void> > ComputeQualityResponse;

typedef boost::shared_ptr< ::graspit_interface::ComputeQualityResponse > ComputeQualityResponsePtr;
typedef boost::shared_ptr< ::graspit_interface::ComputeQualityResponse const> ComputeQualityResponseConstPtr;

// constants requiring out of line definition

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::graspit_interface::ComputeQualityResponse_<ContainerAllocator1> & lhs, const ::graspit_interface::ComputeQualityResponse_<ContainerAllocator2> & rhs)
{
  return lhs.result == rhs.result &&
    lhs.volume == rhs.volume &&
    lhs.epsilon == rhs.epsilon;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::graspit_interface::ComputeQualityResponse_<ContainerAllocator1> & lhs, const ::graspit_interface::ComputeQualityResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace graspit_interface

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a174f632c6427274a6d20c7e1b08902f";
  }

  static const char* value(const ::graspit_interface::ComputeQualityResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa174f632c6427274ULL;
  static const uint64_t static_value2 = 0xa6d20c7e1b08902fULL;
};

template<class ContainerAllocator>
struct DataType< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "graspit_interface/ComputeQualityResponse";
  }

  static const char* value(const ::graspit_interface::ComputeQualityResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 RESULT_SUCCESS    = 0\n"
"uint8 RESULT_INVALID_ID = 1\n"
"uint8 RESULT_COLLISION  = 2\n"
"\n"
"uint8 result\n"
"\n"
"float64 volume\n"
"float64 epsilon\n"
"\n"
;
  }

  static const char* value(const ::graspit_interface::ComputeQualityResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
      stream.next(m.volume);
      stream.next(m.epsilon);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ComputeQualityResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::graspit_interface::ComputeQualityResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::graspit_interface::ComputeQualityResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.result);
    s << indent << "volume: ";
    Printer<double>::stream(s, indent + "  ", v.volume);
    s << indent << "epsilon: ";
    Printer<double>::stream(s, indent + "  ", v.epsilon);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_COMPUTEQUALITYRESPONSE_H
