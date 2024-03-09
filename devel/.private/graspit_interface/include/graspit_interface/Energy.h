// Generated by gencpp from file graspit_interface/Energy.msg
// DO NOT EDIT!


#ifndef GRASPIT_INTERFACE_MESSAGE_ENERGY_H
#define GRASPIT_INTERFACE_MESSAGE_ENERGY_H


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
struct Energy_
{
  typedef Energy_<ContainerAllocator> Type;

  Energy_()
    : energy(0.0)
    , energy_type(0)  {
    }
  Energy_(const ContainerAllocator& _alloc)
    : energy(0.0)
    , energy_type(0)  {
  (void)_alloc;
    }



   typedef double _energy_type;
  _energy_type energy;

   typedef uint8_t _energy_type_type;
  _energy_type_type energy_type;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(ENERGY_VOLUME)
  #undef ENERGY_VOLUME
#endif
#if defined(_WIN32) && defined(ENERGY_EPSILON)
  #undef ENERGY_EPSILON
#endif

  enum {
    ENERGY_VOLUME = 0u,
    ENERGY_EPSILON = 1u,
  };


  typedef boost::shared_ptr< ::graspit_interface::Energy_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::graspit_interface::Energy_<ContainerAllocator> const> ConstPtr;

}; // struct Energy_

typedef ::graspit_interface::Energy_<std::allocator<void> > Energy;

typedef boost::shared_ptr< ::graspit_interface::Energy > EnergyPtr;
typedef boost::shared_ptr< ::graspit_interface::Energy const> EnergyConstPtr;

// constants requiring out of line definition

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::graspit_interface::Energy_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::graspit_interface::Energy_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::graspit_interface::Energy_<ContainerAllocator1> & lhs, const ::graspit_interface::Energy_<ContainerAllocator2> & rhs)
{
  return lhs.energy == rhs.energy &&
    lhs.energy_type == rhs.energy_type;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::graspit_interface::Energy_<ContainerAllocator1> & lhs, const ::graspit_interface::Energy_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace graspit_interface

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::Energy_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::graspit_interface::Energy_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::Energy_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graspit_interface::Energy_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::Energy_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graspit_interface::Energy_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::graspit_interface::Energy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b02fc5d9e41e0b8406a4fd73ca0a93db";
  }

  static const char* value(const ::graspit_interface::Energy_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb02fc5d9e41e0b84ULL;
  static const uint64_t static_value2 = 0x06a4fd73ca0a93dbULL;
};

template<class ContainerAllocator>
struct DataType< ::graspit_interface::Energy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "graspit_interface/Energy";
  }

  static const char* value(const ::graspit_interface::Energy_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::graspit_interface::Energy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 energy\n"
"uint8 energy_type\n"
"\n"
"uint8 ENERGY_VOLUME = 0\n"
"uint8 ENERGY_EPSILON = 1\n"
;
  }

  static const char* value(const ::graspit_interface::Energy_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::graspit_interface::Energy_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.energy);
      stream.next(m.energy_type);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Energy_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::graspit_interface::Energy_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::graspit_interface::Energy_<ContainerAllocator>& v)
  {
    s << indent << "energy: ";
    Printer<double>::stream(s, indent + "  ", v.energy);
    s << indent << "energy_type: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.energy_type);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRASPIT_INTERFACE_MESSAGE_ENERGY_H
