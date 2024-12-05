#!/usr/bin/env python
from __future__ import division

from threading import Lock

import numpy as np


class LowVarianceSampler:
    """Low-variance particle sampler."""

    def __init__(self, particles, weights, state_lock=None):
        """Initialize the particle sampler.

        Args:
            particles: the particles to update
            weights: the weights to update
            state_lock: guarding access to the particles and weights during update,
                since both are shared variables with other processes
        """
        self.particles = particles
        self.weights = weights
        self.state_lock = state_lock or Lock()
        self.n_particles = particles.shape[0]

        # You may want to cache some intermediate variables here for efficiency

        # the number of particles (should cache this?)
        # self.M = len(self.weights)

    def resample(self):
        """Resample particles using the low-variance sampling scheme.

        Both self.particles and self.weights should be modified in-place.
        """
        # Acquire the lock that synchronizes access to the particles. This is
        # necessary because self.particles is shared by the other particle
        # filter classes.
        #
        # The with statement automatically acquires and releases the lock.
        # See the Python documentation for more information:
        # https://docs.python.org/3/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement
        with self.state_lock:
            # BEGIN QUESTION 3.2
            "*** REPLACE THIS LINE ***"

            # slide 37 in particle filters lecture, Probabilistic Robotics
            M = len(self.weights)
            
            # the indices that correspond to the number r, r + 1/M ...
            corr_indices = np.zeros(M)

            # generate a random number r in [0, 1/M]
            r = np.random.uniform(0, 1/M)

            cumulative = np.cumsum(self.weights)
            # check the particles the numbers r, r + 1/M... correspond to
            # i = 1

            # for m in range(1, M):
            #     U = r + (m - 1) * (1/M)
            #     while U > cumulative[i]:
            #         i += 1
            #         # cumulative += self.weights[i]
            #     corr_indices[m] = i
            #     r += 1 / M

            

            # Vectorize the lookup
            # use np.searchsorted 
            U = r + np.arange(M) * 1/M
            corr_indices = np.searchsorted(cumulative, U)

            # update self.particles and self.weights
            self.particles[:] = self.particles[corr_indices]
            self.weights[:] = 1/M






            # END QUESTION 3.2
