from __future__ import division
import numpy as np

from control.controller import BaseController
from control.controller import compute_position_in_frame


class PurePursuitController(BaseController):
    def __init__(self, **kwargs):
        self.car_length = kwargs.pop("car_length")

        # Get the keyword args that we didn't consume with the above initialization
        super(PurePursuitController, self).__init__(**kwargs)


    def get_error(self, pose, reference_xytv):
        """Compute the Pure Pursuit error.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed

        Returns:
            error: Pure Pursuit error
        """
        return compute_position_in_frame(reference_xytv[:3], pose)

    def get_control(self, pose, reference_xytv, error):
        """Compute the Pure Pursuit control law.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed
            error: error vector from get_error

        Returns:
            control: np.array of velocity and steering angle
        """
        # BEGIN QUESTION 3.1
        "*** REPLACE THIS LINE ***"
        result = np.zeros(2)
        result[0] = reference_xytv[3]

        # x, y, theta = pose
        # x_F, y_F, theta_F, v = reference_xytv

        # first = np.zeros(shape=(2,2))
        # first[0, 0] = np.cos(theta)
        # first[0, 1] = np.sin(theta)
        # first[1, 0] = -np.sin(theta)
        # first[1, 1] = np.cos(theta)

        # second = np.array([x_F-x, y_F-y])


        ab = error



        rpp= np.sum(ab**2)/(2*ab[1])
        delt = np.arctan(self.car_length/rpp)
        result[1] = delt

        return result
        # END QUESTION 3.1
