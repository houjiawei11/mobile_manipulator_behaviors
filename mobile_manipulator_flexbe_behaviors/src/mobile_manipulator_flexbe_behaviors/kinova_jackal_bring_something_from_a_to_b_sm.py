#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_manipulation_states.moveit_to_joints_state import MoveitToJointsState
from flexbe_navigation_states.move_base_state import MoveBaseState
from mobile_manipulator_flexbe_states.detect_plane_srv_state import DetectPlaneState
from mobile_manipulator_flexbe_states.place_srv_state import PlaceState
from mobile_manipulator_flexbe_states.pick_srv_state import PickState
from mobile_manipulator_flexbe_states.detect_obj_srv_state import DetectObjState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]
from geometry_msgs.msg import Pose2D, Point
# [/MANUAL_IMPORT]


'''
Created on Mon Aug 23 2020
@author: Yizheng Zhang
'''
class kinova_jackal_bring_something_from_a_to_bSM(Behavior):
	'''
	kinova_jackal_robot. the states set of mobile manipulator.
	'''


	def __init__(self):
		super(kinova_jackal_bring_something_from_a_to_bSM, self).__init__()
		self.name = 'kinova_jackal_bring_something_from_a_to_b'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:26 y:401, x:564 y:234
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.pick_waypoint = Pose2D(-0.3, -3.8, 0)
		_state_machine.userdata.place_waypoint = Pose2D(-8.0, 4.13, 3.14)
		_state_machine.userdata.picking_state = [0.385, 0.476, 1.266, -0.722, 1.954, -1.708, 2.0197, -1.415]
		_state_machine.userdata.prepare_state = [3.141, 2.75, 1.0, -1.57, 0, 1.483]
		_state_machine.userdata.start_point = Point(0.48, 0.0, 0.5)
		_state_machine.userdata.look_up_point = Point(2.0, 0.0, 1.1)
		_state_machine.userdata.see_apriltag = Point(0.8, 0.3, 0.7)

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:123 y:37
			OperatableStateMachine.add('prepare_state',
										MoveitToJointsState(move_group='arm', joint_names=['j2n6s300_joint_1', 'j2n6s300_joint_2', 'j2n6s300_joint_3', 'j2n6s300_joint_4', 'j2n6s300_joint_5', 'j2n6s300_joint_6'], action_topic='/move_group'),
										transitions={'reached': 'nav_pick', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'prepare_state'})

			# x:1137 y:421
			OperatableStateMachine.add('nav_place',
										MoveBaseState(),
										transitions={'arrived': 'detect_plane', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'waypoint': 'place_waypoint'})

			# x:706 y:544
			OperatableStateMachine.add('detect_plane',
										DetectPlaneState(),
										transitions={'continue': 'place_obj', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1096 y:252
			OperatableStateMachine.add('pick_moving_state',
										MoveitToJointsState(move_group='arm', joint_names=['j2n6s300_joint_1', 'j2n6s300_joint_2', 'j2n6s300_joint_3', 'j2n6s300_joint_4', 'j2n6s300_joint_5', 'j2n6s300_joint_6'], action_topic='/move_group'),
										transitions={'reached': 'nav_place', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'prepare_state'})

			# x:576 y:44
			OperatableStateMachine.add('nav_pick',
										MoveBaseState(),
										transitions={'arrived': 'detect_obj', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'waypoint': 'pick_waypoint'})

			# x:372 y:536
			OperatableStateMachine.add('place_obj',
										PlaceState(),
										transitions={'continue': 'finished_pose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1094 y:67
			OperatableStateMachine.add('pick_obj',
										PickState(),
										transitions={'continue': 'pick_moving_state', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:119 y:540
			OperatableStateMachine.add('finished_pose',
										MoveitToJointsState(move_group='arm', joint_names=['j2n6s300_joint_1', 'j2n6s300_joint_2', 'j2n6s300_joint_3', 'j2n6s300_joint_4', 'j2n6s300_joint_5', 'j2n6s300_joint_6'], action_topic='/move_group'),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'prepare_state'})

			# x:822 y:30
			OperatableStateMachine.add('detect_obj',
										DetectObjState(),
										transitions={'continue': 'pick_obj', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
