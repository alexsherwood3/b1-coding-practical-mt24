class Control:
    def __init__(self, Kp: float, Kd: float):
        #Initializes Proportional and Derivative gains for the controller
        self.Kp = Kp 
        self.Kd = Kd
        self.previous_error = 0  # For storing the error at the previous timestep

    def control(self, reference: float, observation: float) -> float:
        error = reference - observation #calculates error for computational efficiency
        # PD control formula: u[t] = Kp * e[t] + Kd * (e[t] - e[t-1])
        control_action = self.Kp * error + self.Kd * (error - self.previous_error) #implements control action
        # Store the current error as previous error for the next timestep
        self.previous_error = error
        return control_action