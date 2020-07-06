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
		_state_machine.userdata.pick_waypoint = Pose2D(3, -1,0)
		_state_machine.userdata.place_waypoint = Pose2D(5, 1,0)

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:188 y:56
			OperatableStateMachine.add('nav_pick',
										MoveBaseState(),
										transitions={'arrived': 'detect_obj', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'waypoint': 'pick_waypoint'})

			# x:491 y:56
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

			# x:821 y:52
			OperatableStateMachine.add('pick_obj',
										PickState(),
										transitions={'continue': 'nav_place', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:503 y:396
			OperatableStateMachine.add('detect_plane',
										DetectPlaneState(),
										transitions={'continue': 'place_obj', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:193 y:392
			OperatableStateMachine.add('place_obj',
										PlaceState(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
