// Generated by gencpp from file graspit_interface/ImportGraspableBodyRequest.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_IMPORTGRASPABLEBODYREQUEST_H
#define GRASPIT_INTERFACE_MESSAGE_IMPORTGRASPABLEBODYREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Pose.h>

namespace graspit_interface
{
template <class ContainerAllocator>
struct ImportGraspableBodyRequest_
{
  typedef ImportGraspableBodyRequest_<ContainerAllocator> Type;

  ImportGraspableBodyRequest_()
    : filename()
    , pose()  {
    }
  ImportGraspableBodyRequest_(const ContainerAllocator& _alloc)
    : filename(_alloc)
    , pose(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _filename_type;
  _filename_type filename;

   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _pose_type;
  _pose_type pose;





  typedef boost::shared_ptr< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ImportGraspableBodyRequest_

typedef ::graspit_interface::ImportGraspableBodyRequest_<std::allocator<void> > ImportGraspableBodyRequest;

typedef boost::shared_ptr< ::graspit_interface::ImportGraspableBodyRequest > ImportGraspableBodyRequestPtr;
typedef boost::shared_ptr< ::graspit_interface::ImportGraspableBodyRequest const> ImportGraspableBodyRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator1> & lhs, const ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator2> & rhs)
{
  return lhs.filename == rhs.filename &&
    lhs.pose == rhs.pose;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator1> & lhs, const ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace graspit_interface

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "67fcc86db491285e47664cb79b9f4221";
  }

  static const char* value(const ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x67fcc86db491285eULL;
  static const uint64_t static_value2 = 0x47664cb79b9f4221ULL;
};

template<class ContainerAllocator>
struct DataType< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "graspit_interface/ImportGraspableBodyRequest";
  }

  static const char* value(const ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string filename\n"
"geometry_msgs/Pose pose\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.filename);
      stream.next(m.pose);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ImportGraspableBodyRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::graspit_interface::ImportGraspableBodyRequest_<ContainerAllocator>& v)
  {
    s << indent << "filename: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.filename);
    s << indent << "pose: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_IMPORTGRASPABLEBODYREQUEST_H
