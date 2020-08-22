#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_navigation_states.move_base_state import MoveBaseState
from mobile_manipulator_flexbe_states.detect_obj_srv_state import DetectObjState
from mobile_manipulator_flexbe_states.pick_srv_state import PickState
from mobile_manipulator_flexbe_states.detect_plane_srv_state import DetectPlaneState
from mobile_manipulator_flexbe_states.place_srv_state import PlaceState
from flexbe_manipulation_states.moveit_to_joints_state import MoveitToJointsState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]
from geometry_msgs.msg import Pose2D
# [/MANUAL_IMPORT]


'''
Created on Mon Jul 06 2020
@author: Yizheng Zhang
'''
class bring_something_from_a_to_bSM(Behavior):
	'''
	The states set of mobile manipulator.
	'''


	def __init__(self):
		super(bring_something_from_a_to_bSM, self).__init__()
		self.name = 'bring_something_from_a_to_b'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:26 y:401, x:564 y:234
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.pick_waypoint = Pose2D(-0.8, -3.65, -1.57)
		_state_machine.userdata.place_waypoint = Pose2D(-8.0, 4.13, 3.14)
		_state_machine.userdata.picking_state = [0.385, 0.476, 1.266, -0.722, 1.954, -1.708, 2.0197, -1.415]
		_state_machine.userdata.prepare_state = [0.337, 1.334, 1.328, -0.145, 1.811, 0.0, 1.639, 0.042]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:188 y:56
			OperatableStateMachine.add('nav_pick',
										MoveBaseState(),
										transitions={'arrived': 'prepare_state', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'waypoint': 'pick_waypoint'})

			# x:740 y:48
			OperatableStateMachine.add('detect_obj',
										DetectObjState(),
										transitions={'continue': 'pick_obj', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:850 y:397
			OperatableStateMachine.add('nav_place',
										MoveBaseState(),
										transitions={'arrived': 'detect_plane', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'waypoint': 'place_waypoint'})

			# x:1056 y:45
			OperatableStateMachine.add('pick_obj',
										PickState(),
										transitions={'continue': 'pick_moving_state', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:493 y:400
			OperatableStateMachine.add('detect_plane',
										DetectPlaneState(),
										transitions={'continue': 'place_obj', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1074 y:214
			OperatableStateMachine.add('pick_moving_state',
										MoveitToJointsState(move_group='arm_with_torso', joint_names=['torso_lift_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'upperarm_roll_joint', 'elbow_flex_joint', 'forearm_roll_joint', 'wrist_flex_joint', 'wrist_roll_joint'], action_topic='/move_group'),
										transitions={'reached': 'nav_place', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'picking_state'})

			# x:499 y:47
			OperatableStateMachine.add('prepare_state',
										MoveitToJointsState(move_group='arm_with_torso', joint_names=['torso_lift_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'upperarm_roll_joint', 'elbow_flex_joint', 'forearm_roll_joint', 'wrist_flex_joint', 'wrist_roll_joint'], action_topic='/move_group'),
										transitions={'reached': 'detect_obj', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'prepare_state'})

			# x:178 y:174
			OperatableStateMachine.add('nav_pick',
										MoveBaseState(),
										transitions={'arrived': 'prepare_state', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'waypoint': 'pick_waypoint'})

			# x:1053 y:513
			OperatableStateMachine.add('look_up',
										HeadActionState(),
										transitions={'head_arrived': 'nav_place', 'command_error': 'failed'},
										autonomy={'head_arrived': Autonomy.Off, 'command_error': Autonomy.Off},
										remapping={'point2see': 'look_up_point'})

			# x:598 y:600
			OperatableStateMachine.add('find_apriltag',
										HeadActionState(),
										transitions={'head_arrived': 'detect_plane', 'command_error': 'failed'},
										autonomy={'head_arrived': Autonomy.Off, 'command_error': Autonomy.Off},
										remapping={'point2see': 'see_apriltag'})

			# x:130 y:479
			OperatableStateMachine.add('place_obj',
										PlaceState(),
										transitions={'continue': 'finished_pose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1056 y:45
			OperatableStateMachine.add('pick_obj',
										PickState(),
										transitions={'continue': 'pick_moving_state', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:92 y:342
			OperatableStateMachine.add('finished_pose',
										MoveitToJointsState(move_group='arm_with_torso', joint_names=['torso_lift_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'upperarm_roll_joint', 'elbow_flex_joint', 'forearm_roll_joint', 'wrist_flex_joint', 'wrist_roll_joint'], action_topic='/move_group'),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'picking_state'})

		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
