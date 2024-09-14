import math
country = input("")
life_expectancy = float(input())
expected_schooling = float(input())
mean_schooling = float(input())
gni = float(input())

MIN_LIFE_EXP = 20
MAX_LIFE_EXP = 85
MIN_EXP_SCHOOLING = 0
MAX_EXP_SCHOOLING = 18
MIN_MEAN_EXP_SCHOOLING = 0
MAX_MEAN_EXP_SCHOOLING = 15
MIN_GNI = 100
MAX_GNI = 75000

health = (life_expectancy-MIN_LIFE_EXP)/(MAX_LIFE_EXP-MIN_LIFE_EXP)
schooling_index = (expected_schooling-MIN_EXP_SCHOOLING)/(MAX_EXP_SCHOOLING-MIN_EXP_SCHOOLING)
mean_schooling_index = (mean_schooling-MIN_MEAN_EXP_SCHOOLING)/(MAX_MEAN_EXP_SCHOOLING-MIN_MEAN_EXP_SCHOOLING)

educational_index = (schooling_index+mean_schooling_index)/2

gni_index = (math.log10(gni)-math.log10(MIN_GNI))/(math.log10(MAX_GNI)-math.log10(MIN_GNI))

hdi = math.cbrt(health*educational_index*gni_index)

worst_index = [health, educational_index, gni_index]
min_worst_index = min(worst_index)


print(f"Life expectancy index for {country} is {health:.4f}." )
print(f"Education index for {country} is {educational_index:.4f}.")
print(f"GNI index for {country} is {gni_index:.4f}.")
print(f"HDI for {country} is {hdi:.3f}.")
print(f"HDI for {country} is high: {gni_index>0.7}.")
print(f"The worst index for {country} is {min_worst_index:.4f}.")
