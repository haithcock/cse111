water_density = 998.2
water_acceleration = 9.80665
dynamicviscosity =.0010016

def water_column_height(tower_height, tank_height):#the formula for calculating the water column height is h = t + (3w/4)
    height = tower_height + ((3 * tank_height)/4)
    return height
    ()


def pressure_gain_from_water_height(height, water_density, water_acceleration):     #the formula for calculating pressure cause by earth's gravity is p = pgh/1000  ---  P = (998.2 * 9.80665 * height of the water column in meters) / 1000
   pressure = ((water_density * water_acceleration * height)/1000)
   return pressure
   ()


def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity, water_density):        #P = (-fLpv^2)/2000d
   
    waterpressureloss = (-friction_factor *pipe_length*water_density*(fluid_velocity**2)/(2000*pipe_diameter))
    return waterpressureloss
    ()

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings, water_density):
    waterpressurelossfromfittings = (-.04 * water_density * (fluid_velocity**2) * quantity_fittings)/2000
    return waterpressurelossfromfittings
    ()

def reynolds_number(hydraulic_diameter, fluid_velocity, dynamicviscosity, water_density):
    reynolds_number = (water_density * hydraulic_diameter * fluid_velocity)/dynamicviscosity
    return reynolds_number
    ()
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, water_density):
   
    formulaone = (.1+(50/reynolds_number)) * (((larger_diameter/smaller_diameter)**4)-1)
    formulatwo = (-formulaone * water_density * (fluid_velocity**2))/2000
    return formulatwo
   
   #konstant =  
    ()




PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    water_density = 998.2
    water_acceleration = 9.80665
    dynamicviscosity =.0010016
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height, water_density, water_acceleration)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity, dynamicviscosity, water_density)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity, water_density)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles, water_density)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER, water_density)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity, water_density)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()



'''
    P is the lost pressure in kilopascals
    f is the pipe’s friction factor
    L is the length of the pipe in meters
    ρ is the density of water 998.2 (kilogram / meter3) *Just use # in your calculations
    v is the velocity of the water flowing through the pipe in meters / second
    d is the diameter of the pipe in meters
    '''