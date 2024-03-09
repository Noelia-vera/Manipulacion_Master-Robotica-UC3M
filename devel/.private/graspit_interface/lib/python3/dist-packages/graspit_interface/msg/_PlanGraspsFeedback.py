# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from graspit_interface/PlanGraspsFeedback.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import graspit_interface.msg
import std_msgs.msg

class PlanGraspsFeedback(genpy.Message):
  _md5sum = "d54c8e6346726a2e719e94003c616ef2"
  _type = "graspit_interface/PlanGraspsFeedback"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Feedback 
int32 current_step
Grasp[] grasps
float64[] energies
string search_energy


================================================================================
MSG: graspit_interface/Grasp
# id for the body the grasp was planned on.
int32 graspable_body_id

# pose of the hand with respect to the object 
# the grasp was planned on
geometry_msgs/Pose pose

float64[] dofs

float64 epsilon_quality
float64 volume_quality


# The approach direction to take before picking an object
geometry_msgs/Vector3Stamped approach_direction





================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Vector3Stamped
# This represents a Vector3 with reference coordinate frame and timestamp
Header header
Vector3 vector

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['current_step','grasps','energies','search_energy']
  _slot_types = ['int32','graspit_interface/Grasp[]','float64[]','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       current_step,grasps,energies,search_energy

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PlanGraspsFeedback, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.current_step is None:
        self.current_step = 0
      if self.grasps is None:
        self.grasps = []
      if self.energies is None:
        self.energies = []
      if self.search_energy is None:
        self.search_energy = ''
    else:
      self.current_step = 0
      self.grasps = []
      self.energies = []
      self.search_energy = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.current_step
      buff.write(_get_struct_i().pack(_x))
      length = len(self.grasps)
      buff.write(_struct_I.pack(length))
      for val1 in self.grasps:
        _x = val1.graspable_body_id
        buff.write(_get_struct_i().pack(_x))
        _v1 = val1.pose
        _v2 = _v1.position
        _x = _v2
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v3 = _v1.orientation
        _x = _v3
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        length = len(val1.dofs)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*val1.dofs))
        _x = val1
        buff.write(_get_struct_2d().pack(_x.epsilon_quality, _x.volume_quality))
        _v4 = val1.approach_direction
        _v5 = _v4.header
        _x = _v5.seq
        buff.write(_get_struct_I().pack(_x))
        _v6 = _v5.stamp
        _x = _v6
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v5.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v7 = _v4.vector
        _x = _v7
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.energies)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.energies))
      _x = self.search_energy
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.grasps is None:
        self.grasps = None
      end = 0
      start = end
      end += 4
      (self.current_step,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grasps = []
      for i in range(0, length):
        val1 = graspit_interface.msg.Grasp()
        start = end
        end += 4
        (val1.graspable_body_id,) = _get_struct_i().unpack(str[start:end])
        _v8 = val1.pose
        _v9 = _v8.position
        _x = _v9
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v10 = _v8.orientation
        _x = _v10
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.dofs = s.unpack(str[start:end])
        _x = val1
        start = end
        end += 16
        (_x.epsilon_quality, _x.volume_quality,) = _get_struct_2d().unpack(str[start:end])
        _v11 = val1.approach_direction
        _v12 = _v11.header
        start = end
        end += 4
        (_v12.seq,) = _get_struct_I().unpack(str[start:end])
        _v13 = _v12.stamp
        _x = _v13
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v12.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v12.frame_id = str[start:end]
        _v14 = _v11.vector
        _x = _v14
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.grasps.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.energies = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.search_energy = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.search_energy = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.current_step
      buff.write(_get_struct_i().pack(_x))
      length = len(self.grasps)
      buff.write(_struct_I.pack(length))
      for val1 in self.grasps:
        _x = val1.graspable_body_id
        buff.write(_get_struct_i().pack(_x))
        _v15 = val1.pose
        _v16 = _v15.position
        _x = _v16
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v17 = _v15.orientation
        _x = _v17
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        length = len(val1.dofs)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.dofs.tostring())
        _x = val1
        buff.write(_get_struct_2d().pack(_x.epsilon_quality, _x.volume_quality))
        _v18 = val1.approach_direction
        _v19 = _v18.header
        _x = _v19.seq
        buff.write(_get_struct_I().pack(_x))
        _v20 = _v19.stamp
        _x = _v20
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v19.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v21 = _v18.vector
        _x = _v21
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.energies)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.energies.tostring())
      _x = self.search_energy
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.grasps is None:
        self.grasps = None
      end = 0
      start = end
      end += 4
      (self.current_step,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grasps = []
      for i in range(0, length):
        val1 = graspit_interface.msg.Grasp()
        start = end
        end += 4
        (val1.graspable_body_id,) = _get_struct_i().unpack(str[start:end])
        _v22 = val1.pose
        _v23 = _v22.position
        _x = _v23
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v24 = _v22.orientation
        _x = _v24
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.dofs = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        _x = val1
        start = end
        end += 16
        (_x.epsilon_quality, _x.volume_quality,) = _get_struct_2d().unpack(str[start:end])
        _v25 = val1.approach_direction
        _v26 = _v25.header
        start = end
        end += 4
        (_v26.seq,) = _get_struct_I().unpack(str[start:end])
        _v27 = _v26.stamp
        _x = _v27
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v26.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v26.frame_id = str[start:end]
        _v28 = _v25.vector
        _x = _v28
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.grasps.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.energies = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.search_energy = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.search_energy = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_2d = None
def _get_struct_2d():
    global _struct_2d
    if _struct_2d is None:
        _struct_2d = struct.Struct("<2d")
    return _struct_2d
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
