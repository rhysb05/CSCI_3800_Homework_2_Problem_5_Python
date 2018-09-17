print("Welcome!! This program calculates and displays world population growth\n")
print("The program assumes that world population will continue")
print("to grow at a rate of 1.09% annually\n")
print("Estimates are based on information from the United Nations Population")
print("Division")

# Set current growth rate
growth_rate = 1.0109
annual_increase = 0

# Current world population
starting_population = 7632819325
current_population = 7632819325

# Variable to hold the variables in my loop
current_year = 2018
double_population_year = 0
# Print the column headers
print("Year:\tPopulation:\tPopulation Increase:")

for i in range(75):
	if i == 0:
		print(f"{current_year}\t{current_population}\t{annual_increase}")
	# end if
	if i != 0:
		annual_increase = ((current_population * growth_rate) - current_population)
		current_population *= growth_rate
		current_year += 1
		
		print(f"{current_year}\t" "%.0f" % current_population, "\t%.0f" % annual_increase)
		
		# Store the year when the population will double
		if double_population_year == 0 and current_population >= starting_population * 2:
			double_population_year = current_year
	# end if
# end for
	
print(f"\n\n The population will double in", {double_population_year})
print("Thanks for running our program!!!")
