// Generated by gencpp from file graspit_interface/AutoGraspRequest.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_AUTOGRASPREQUEST_H
#define GRASPIT_INTERFACE_MESSAGE_AUTOGRASPREQUEST_H


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
struct AutoGraspRequest_
{
  typedef AutoGraspRequest_<ContainerAllocator> Type;

  AutoGraspRequest_()
    : id(0)  {
    }
  AutoGraspRequest_(const ContainerAllocator& _alloc)
    : id(0)  {
  (void)_alloc;
    }



   typedef uint32_t _id_type;
  _id_type id;





  typedef boost::shared_ptr< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> const> ConstPtr;

}; // struct AutoGraspRequest_

typedef ::graspit_interface::AutoGraspRequest_<std::allocator<void> > AutoGraspRequest;

typedef boost::shared_ptr< ::graspit_interface::AutoGraspRequest > AutoGraspRequestPtr;
typedef boost::shared_ptr< ::graspit_interface::AutoGraspRequest const> AutoGraspRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::graspit_interface::AutoGraspRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::graspit_interface::AutoGraspRequest_<ContainerAllocator1> & lhs, const ::graspit_interface::AutoGraspRequest_<ContainerAllocator2> & rhs)
{
  return lhs.id == rhs.id;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::graspit_interface::AutoGraspRequest_<ContainerAllocator1> & lhs, const ::graspit_interface::AutoGraspRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace graspit_interface

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "309d4b30834b338cced19e5622a97a03";
  }

  static const char* value(const ::graspit_interface::AutoGraspRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x309d4b30834b338cULL;
  static const uint64_t static_value2 = 0xced19e5622a97a03ULL;
};

template<class ContainerAllocator>
struct DataType< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "graspit_interface/AutoGraspRequest";
  }

  static const char* value(const ::graspit_interface::AutoGraspRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint32 id\n"
;
  }

  static const char* value(const ::graspit_interface::AutoGraspRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct AutoGraspRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::graspit_interface::AutoGraspRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::graspit_interface::AutoGraspRequest_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.id);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_AUTOGRASPREQUEST_H
