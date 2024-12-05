
    1. What controller type did you choose to use for path following with multiple waypoints (pid, pp, mpc)? Why did you choose this controller type?
    
    We used MPC because it accounts for both the dynamics (assumptions about the model and model path) as well as having a feedback loop to correctly address it's mistakes (best of both worlds from PID and PP). With testing we found it performed well.
    
    2. What roadmap parameters did you use for planning (num_vertices, connection_radius, curvature)? Why did you choose these parameters?
    
    num_vertices: 1000
    connection_radius: 20
    curvature: 1.07

    num_vertices and connection_radius were set to these values because they were able to find a path to each waypoint and didn't require much compute power. We tuned the curvature to the max curvature that we calculated in the previous project because we wanted our paths to be as straight as possible to maximize speed.

    3. What was the most difficult part of making your code work with multiple waypoints?

    Tuning the parameters was the hardest part because we needed to understand the relationship between our speed and the distance lookahead.