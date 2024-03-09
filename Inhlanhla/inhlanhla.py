import random
import datetime
from skyfield.api import load

# Get the current date
current_date = datetime.datetime.now()

# Get the age of the Earth in years
age_of_earth = 4.54e9  # Age of the Earth in years

# Get the lucky number of the whole country (you can replace this with any number)
lucky_number = 7

# Seed the random number generator with a combination of current date, age of the Earth, and lucky number
seed = current_date.year + current_date.month + current_date.day + int(age_of_earth) + lucky_number

# Load the ephemeris data
eph = load('de421.bsp')

# Get the positions of the Sun and Moon
sun, moon = eph['sun'], eph['moon']

# Compute the phase angle of the Moon
t = eph['moon'].at(eph.timescale.now())
_, phase_angle, _ = t.observe(sun).apparent().observe(moon).apparent().to_spherical()

# Convert phase angle to a value between 0 and 1 (where 0 is new moon and 1 is full moon)
moon_phase = (1 - phase_angle / (2 * 3.141592653589793)) % 1

# Include additional factors in the seed
seed += moon_phase

# Seed the random number generator
random.seed(seed)

# Generate 6 random lotto numbers
lotto_numbers = random.sample(range(1, 50), 6)

# Print the lotto numbers
print("Your lotto numbers are:", lotto_numbers)

