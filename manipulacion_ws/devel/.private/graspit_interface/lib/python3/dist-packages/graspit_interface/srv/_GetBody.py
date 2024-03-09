# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from graspit_interface/GetBodyRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetBodyRequest(genpy.Message):
  _md5sum = "c5e4a7d59c68f74eabcec876a00216aa"
  _type = "graspit_interface/GetBodyRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 id
"""
  __slots__ = ['id']
  _slot_types = ['int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetBodyRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
    else:
      self.id = 0

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
      _x = self.id
      buff.write(_get_struct_i().pack(_x))
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
      end = 0
      start = end
      end += 4
      (self.id,) = _get_struct_i().unpack(str[start:end])
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
      _x = self.id
      buff.write(_get_struct_i().pack(_x))
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
      end = 0
      start = end
      end += 4
      (self.id,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from graspit_interface/GetBodyResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import graspit_interface.msg
import std_msgs.msg

class GetBodyResponse(genpy.Message):
  _md5sum = "722dad3e6f58748e50f775608844db35"
  _type = "graspit_interface/GetBodyResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """Body body

uint8 RESULT_SUCCESS    = 0
uint8 RESULT_INVALID_ID = 1
 
uint8 result


================================================================================
MSG: graspit_interface/Body
std_msgs/Header header

geometry_msgs/Pose pose
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
"""
  # Pseudo-constants
  RESULT_SUCCESS = 0
  RESULT_INVALID_ID = 1

  __slots__ = ['body','result']
  _slot_types = ['graspit_interface/Body','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       body,result

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetBodyResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.body is None:
        self.body = graspit_interface.msg.Body()
      if self.result is None:
        self.result = 0
    else:
      self.body = graspit_interface.msg.Body()
      self.result = 0

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
      _x = self
      buff.write(_get_struct_3I().pack(_x.body.header.seq, _x.body.header.stamp.secs, _x.body.header.stamp.nsecs))
      _x = self.body.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7dB().pack(_x.body.pose.position.x, _x.body.pose.position.y, _x.body.pose.position.z, _x.body.pose.orientation.x, _x.body.pose.orientation.y, _x.body.pose.orientation.z, _x.body.pose.orientation.w, _x.result))
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
      if self.body is None:
        self.body = graspit_interface.msg.Body()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.body.header.seq, _x.body.header.stamp.secs, _x.body.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.body.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.body.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 57
      (_x.body.pose.position.x, _x.body.pose.position.y, _x.body.pose.position.z, _x.body.pose.orientation.x, _x.body.pose.orientation.y, _x.body.pose.orientation.z, _x.body.pose.orientation.w, _x.result,) = _get_struct_7dB().unpack(str[start:end])
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
      _x = self
      buff.write(_get_struct_3I().pack(_x.body.header.seq, _x.body.header.stamp.secs, _x.body.header.stamp.nsecs))
      _x = self.body.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7dB().pack(_x.body.pose.position.x, _x.body.pose.position.y, _x.body.pose.position.z, _x.body.pose.orientation.x, _x.body.pose.orientation.y, _x.body.pose.orientation.z, _x.body.pose.orientation.w, _x.result))
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
      if self.body is None:
        self.body = graspit_interface.msg.Body()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.body.header.seq, _x.body.header.stamp.secs, _x.body.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.body.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.body.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 57
      (_x.body.pose.position.x, _x.body.pose.position.y, _x.body.pose.position.z, _x.body.pose.orientation.x, _x.body.pose.orientation.y, _x.body.pose.orientation.z, _x.body.pose.orientation.w, _x.result,) = _get_struct_7dB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_7dB = None
def _get_struct_7dB():
    global _struct_7dB
    if _struct_7dB is None:
        _struct_7dB = struct.Struct("<7dB")
    return _struct_7dB
class GetBody(object):
  _type          = 'graspit_interface/GetBody'
  _md5sum = 'b5f0921777cf671340b9c6535008ff4e'
  _request_class  = GetBodyRequest
  _response_class = GetBodyResponse