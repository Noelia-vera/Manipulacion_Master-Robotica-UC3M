// Generated by gencpp from file graspit_interface/GetRobotsResponse.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_GETROBOTSRESPONSE_H
#define GRASPIT_INTERFACE_MESSAGE_GETROBOTSRESPONSE_H


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
struct GetRobotsResponse_
{
  typedef GetRobotsResponse_<ContainerAllocator> Type;

  GetRobotsResponse_()
    : ids()  {
    }
  GetRobotsResponse_(const ContainerAllocator& _alloc)
    : ids(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> _ids_type;
  _ids_type ids;





  typedef boost::shared_ptr< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetRobotsResponse_

typedef ::graspit_interface::GetRobotsResponse_<std::allocator<void> > GetRobotsResponse;

typedef boost::shared_ptr< ::graspit_interface::GetRobotsResponse > GetRobotsResponsePtr;
typedef boost::shared_ptr< ::graspit_interface::GetRobotsResponse const> GetRobotsResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::graspit_interface::GetRobotsResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::graspit_interface::GetRobotsResponse_<ContainerAllocator1> & lhs, const ::graspit_interface::GetRobotsResponse_<ContainerAllocator2> & rhs)
{
  return lhs.ids == rhs.ids;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::graspit_interface::GetRobotsResponse_<ContainerAllocator1> & lhs, const ::graspit_interface::GetRobotsResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace graspit_interface

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4f22efebf407aadba2ecc69df353d113";
  }

  static const char* value(const ::graspit_interface::GetRobotsResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4f22efebf407aadbULL;
  static const uint64_t static_value2 = 0xa2ecc69df353d113ULL;
};

template<class ContainerAllocator>
struct DataType< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "graspit_interface/GetRobotsResponse";
  }

  static const char* value(const ::graspit_interface::GetRobotsResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32[] ids\n"
"\n"
;
  }

  static const char* value(const ::graspit_interface::GetRobotsResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ids);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetRobotsResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::graspit_interface::GetRobotsResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::graspit_interface::GetRobotsResponse_<ContainerAllocator>& v)
  {
    s << indent << "ids[]" << std::endl;
    for (size_t i = 0; i < v.ids.size(); ++i)
    {
      s << indent << "  ids[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.ids[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_GETROBOTSRESPONSE_H