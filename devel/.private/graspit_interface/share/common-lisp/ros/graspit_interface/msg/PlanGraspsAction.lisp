; Auto-generated. Do not edit!


(cl:in-package graspit_interface-msg)


;//! \htmlinclude PlanGraspsAction.msg.html

(cl:defclass <PlanGraspsAction> (roslisp-msg-protocol:ros-message)
  ((action_goal
    :reader action_goal
    :initarg :action_goal
    :type graspit_interface-msg:PlanGraspsActionGoal
    :initform (cl:make-instance 'graspit_interface-msg:PlanGraspsActionGoal))
   (action_result
    :reader action_result
    :initarg :action_result
    :type graspit_interface-msg:PlanGraspsActionResult
    :initform (cl:make-instance 'graspit_interface-msg:PlanGraspsActionResult))
   (action_feedback
    :reader action_feedback
    :initarg :action_feedback
    :type graspit_interface-msg:PlanGraspsActionFeedback
    :initform (cl:make-instance 'graspit_interface-msg:PlanGraspsActionFeedback)))
)

(cl:defclass PlanGraspsAction (<PlanGraspsAction>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PlanGraspsAction>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PlanGraspsAction)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name graspit_interface-msg:<PlanGraspsAction> is deprecated: use graspit_interface-msg:PlanGraspsAction instead.")))

(cl:ensure-generic-function 'action_goal-val :lambda-list '(m))
(cl:defmethod action_goal-val ((m <PlanGraspsAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graspit_interface-msg:action_goal-val is deprecated.  Use graspit_interface-msg:action_goal instead.")
  (action_goal m))

(cl:ensure-generic-function 'action_result-val :lambda-list '(m))
(cl:defmethod action_result-val ((m <PlanGraspsAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graspit_interface-msg:action_result-val is deprecated.  Use graspit_interface-msg:action_result instead.")
  (action_result m))

(cl:ensure-generic-function 'action_feedback-val :lambda-list '(m))
(cl:defmethod action_feedback-val ((m <PlanGraspsAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graspit_interface-msg:action_feedback-val is deprecated.  Use graspit_interface-msg:action_feedback instead.")
  (action_feedback m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PlanGraspsAction>) ostream)
  "Serializes a message object of type '<PlanGraspsAction>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_goal) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_result) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_feedback) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PlanGraspsAction>) istream)
  "Deserializes a message object of type '<PlanGraspsAction>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_goal) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_result) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_feedback) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PlanGraspsAction>)))
  "Returns string type for a message object of type '<PlanGraspsAction>"
  "graspit_interface/PlanGraspsAction")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PlanGraspsAction)))
  "Returns string type for a message object of type 'PlanGraspsAction"
  "graspit_interface/PlanGraspsAction")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PlanGraspsAction>)))
  "Returns md5sum for a message object of type '<PlanGraspsAction>"
  "efcf545608ecd5605289fd94f4ae9759")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PlanGraspsAction)))
  "Returns md5sum for a message object of type 'PlanGraspsAction"
  "efcf545608ecd5605289fd94f4ae9759")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PlanGraspsAction>)))
  "Returns full string definition for message of type '<PlanGraspsAction>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%PlanGraspsActionGoal action_goal~%PlanGraspsActionResult action_result~%PlanGraspsActionFeedback action_feedback~%~%================================================================================~%MSG: graspit_interface/PlanGraspsActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%PlanGraspsGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: graspit_interface/PlanGraspsGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal~%int32 graspable_body_id~%~%Planner planner~%string search_energy~%SearchSpace search_space~%SearchContact search_contact~%SimAnnParams sim_ann_params~%~%int32 max_steps~%int32 feedback_num_steps~%~%================================================================================~%MSG: graspit_interface/Planner~%uint8 SIM_ANN                      = 0~%uint8 MULTI_THREADED               = 1~%~%uint8 type~%================================================================================~%MSG: graspit_interface/SearchSpace~%uint8 SPACE_AXIS_ANGLE    = 0~%uint8 SPACE_COMPLETE      = 1~%uint8 SPACE_ELLIPSOID     = 2~%uint8 SPACE_APPROACH      = 3~%~%uint8 type~%================================================================================~%MSG: graspit_interface/SearchContact~%uint8 CONTACT_PRESET    = 0~%uint8 CONTACT_LIVE      = 1~%~%uint8 type	~%================================================================================~%MSG: graspit_interface/SimAnnParams~%~%# flag to switch to custom params defined in this message. If not set, GraspIt's default settings are kept~%bool set_custom_params~%~%~%# //Annealing parameters~%# //! Annealing constant for neighbor generation schedule~%float64 YC	 	#	GraspIt! default: 7.0~%# //! Annealing constant for error acceptance schedule~%float64 HC	 	#	GraspIt! default: 7.0~%# //! Number of dimensions for neighbor generation schedule~%float64 YDIMS	#	GraspIt! default: 8.0~%# //! Number of dimensions for error acceptance schedule~%float64 HDIMS	#	GraspIt! default: 8.0~%# //! Adjust factor for neighbor generation schedule~%float64 NBR_ADJ	#	GraspIt! default: 1.0~%# //! Adjust raw errors reported by states to be in the relevant range of the annealing schedule~%float64 ERR_ADJ	#	GraspIt! default: 1.0e-6~%# //! Starting temperatue~%float64 DEF_T0	#	GraspIt! default: 1e6~%# //! Starting step~%float64 DEF_K0	#	GraspIt! default: 30000~%================================================================================~%MSG: graspit_interface/PlanGraspsActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%PlanGraspsResult result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: graspit_interface/PlanGraspsResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Result~%Grasp[] grasps~%float64[] energies~%string search_energy~%~%================================================================================~%MSG: graspit_interface/Grasp~%# id for the body the grasp was planned on.~%int32 graspable_body_id~%~%# pose of the hand with respect to the object ~%# the grasp was planned on~%geometry_msgs/Pose pose~%~%float64[] dofs~%~%float64 epsilon_quality~%float64 volume_quality~%~%~%# The approach direction to take before picking an object~%geometry_msgs/Vector3Stamped approach_direction~%~%~%~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Vector3Stamped~%# This represents a Vector3 with reference coordinate frame and timestamp~%Header header~%Vector3 vector~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: graspit_interface/PlanGraspsActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%PlanGraspsFeedback feedback~%~%================================================================================~%MSG: graspit_interface/PlanGraspsFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Feedback ~%int32 current_step~%Grasp[] grasps~%float64[] energies~%string search_energy~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PlanGraspsAction)))
  "Returns full string definition for message of type 'PlanGraspsAction"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%PlanGraspsActionGoal action_goal~%PlanGraspsActionResult action_result~%PlanGraspsActionFeedback action_feedback~%~%================================================================================~%MSG: graspit_interface/PlanGraspsActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%PlanGraspsGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: graspit_interface/PlanGraspsGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal~%int32 graspable_body_id~%~%Planner planner~%string search_energy~%SearchSpace search_space~%SearchContact search_contact~%SimAnnParams sim_ann_params~%~%int32 max_steps~%int32 feedback_num_steps~%~%================================================================================~%MSG: graspit_interface/Planner~%uint8 SIM_ANN                      = 0~%uint8 MULTI_THREADED               = 1~%~%uint8 type~%================================================================================~%MSG: graspit_interface/SearchSpace~%uint8 SPACE_AXIS_ANGLE    = 0~%uint8 SPACE_COMPLETE      = 1~%uint8 SPACE_ELLIPSOID     = 2~%uint8 SPACE_APPROACH      = 3~%~%uint8 type~%================================================================================~%MSG: graspit_interface/SearchContact~%uint8 CONTACT_PRESET    = 0~%uint8 CONTACT_LIVE      = 1~%~%uint8 type	~%================================================================================~%MSG: graspit_interface/SimAnnParams~%~%# flag to switch to custom params defined in this message. If not set, GraspIt's default settings are kept~%bool set_custom_params~%~%~%# //Annealing parameters~%# //! Annealing constant for neighbor generation schedule~%float64 YC	 	#	GraspIt! default: 7.0~%# //! Annealing constant for error acceptance schedule~%float64 HC	 	#	GraspIt! default: 7.0~%# //! Number of dimensions for neighbor generation schedule~%float64 YDIMS	#	GraspIt! default: 8.0~%# //! Number of dimensions for error acceptance schedule~%float64 HDIMS	#	GraspIt! default: 8.0~%# //! Adjust factor for neighbor generation schedule~%float64 NBR_ADJ	#	GraspIt! default: 1.0~%# //! Adjust raw errors reported by states to be in the relevant range of the annealing schedule~%float64 ERR_ADJ	#	GraspIt! default: 1.0e-6~%# //! Starting temperatue~%float64 DEF_T0	#	GraspIt! default: 1e6~%# //! Starting step~%float64 DEF_K0	#	GraspIt! default: 30000~%================================================================================~%MSG: graspit_interface/PlanGraspsActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%PlanGraspsResult result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: graspit_interface/PlanGraspsResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Result~%Grasp[] grasps~%float64[] energies~%string search_energy~%~%================================================================================~%MSG: graspit_interface/Grasp~%# id for the body the grasp was planned on.~%int32 graspable_body_id~%~%# pose of the hand with respect to the object ~%# the grasp was planned on~%geometry_msgs/Pose pose~%~%float64[] dofs~%~%float64 epsilon_quality~%float64 volume_quality~%~%~%# The approach direction to take before picking an object~%geometry_msgs/Vector3Stamped approach_direction~%~%~%~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Vector3Stamped~%# This represents a Vector3 with reference coordinate frame and timestamp~%Header header~%Vector3 vector~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: graspit_interface/PlanGraspsActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%PlanGraspsFeedback feedback~%~%================================================================================~%MSG: graspit_interface/PlanGraspsFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Feedback ~%int32 current_step~%Grasp[] grasps~%float64[] energies~%string search_energy~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PlanGraspsAction>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_goal))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_result))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_feedback))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PlanGraspsAction>))
  "Converts a ROS message object to a list"
  (cl:list 'PlanGraspsAction
    (cl:cons ':action_goal (action_goal msg))
    (cl:cons ':action_result (action_result msg))
    (cl:cons ':action_feedback (action_feedback msg))
))