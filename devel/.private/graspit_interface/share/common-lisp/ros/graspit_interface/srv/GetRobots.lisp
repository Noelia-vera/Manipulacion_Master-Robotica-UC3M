; Auto-generated. Do not edit!


(cl:in-package graspit_interface-srv)


;//! \htmlinclude GetRobots-request.msg.html

(cl:defclass <GetRobots-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass GetRobots-request (<GetRobots-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetRobots-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetRobots-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name graspit_interface-srv:<GetRobots-request> is deprecated: use graspit_interface-srv:GetRobots-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetRobots-request>) ostream)
  "Serializes a message object of type '<GetRobots-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetRobots-request>) istream)
  "Deserializes a message object of type '<GetRobots-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetRobots-request>)))
  "Returns string type for a service object of type '<GetRobots-request>"
  "graspit_interface/GetRobotsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetRobots-request)))
  "Returns string type for a service object of type 'GetRobots-request"
  "graspit_interface/GetRobotsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetRobots-request>)))
  "Returns md5sum for a message object of type '<GetRobots-request>"
  "4f22efebf407aadba2ecc69df353d113")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetRobots-request)))
  "Returns md5sum for a message object of type 'GetRobots-request"
  "4f22efebf407aadba2ecc69df353d113")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetRobots-request>)))
  "Returns full string definition for message of type '<GetRobots-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetRobots-request)))
  "Returns full string definition for message of type 'GetRobots-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetRobots-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetRobots-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GetRobots-request
))
;//! \htmlinclude GetRobots-response.msg.html

(cl:defclass <GetRobots-response> (roslisp-msg-protocol:ros-message)
  ((ids
    :reader ids
    :initarg :ids
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass GetRobots-response (<GetRobots-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetRobots-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetRobots-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name graspit_interface-srv:<GetRobots-response> is deprecated: use graspit_interface-srv:GetRobots-response instead.")))

(cl:ensure-generic-function 'ids-val :lambda-list '(m))
(cl:defmethod ids-val ((m <GetRobots-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graspit_interface-srv:ids-val is deprecated.  Use graspit_interface-srv:ids instead.")
  (ids m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetRobots-response>) ostream)
  "Serializes a message object of type '<GetRobots-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'ids))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'ids))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetRobots-response>) istream)
  "Deserializes a message object of type '<GetRobots-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'ids) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'ids)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetRobots-response>)))
  "Returns string type for a service object of type '<GetRobots-response>"
  "graspit_interface/GetRobotsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetRobots-response)))
  "Returns string type for a service object of type 'GetRobots-response"
  "graspit_interface/GetRobotsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetRobots-response>)))
  "Returns md5sum for a message object of type '<GetRobots-response>"
  "4f22efebf407aadba2ecc69df353d113")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetRobots-response)))
  "Returns md5sum for a message object of type 'GetRobots-response"
  "4f22efebf407aadba2ecc69df353d113")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetRobots-response>)))
  "Returns full string definition for message of type '<GetRobots-response>"
  (cl:format cl:nil "int32[] ids~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetRobots-response)))
  "Returns full string definition for message of type 'GetRobots-response"
  (cl:format cl:nil "int32[] ids~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetRobots-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'ids) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetRobots-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GetRobots-response
    (cl:cons ':ids (ids msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GetRobots)))
  'GetRobots-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GetRobots)))
  'GetRobots-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetRobots)))
  "Returns string type for a service object of type '<GetRobots>"
  "graspit_interface/GetRobots")