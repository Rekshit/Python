import statistics

data= [24,65,13,28,10,39,47]

mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode(data)
sd_value = statistics.stdev(data)

print("The mean of data is: ", mean_value)
print("The median of data is: ", median_value)
print("The mode of data is: ", mode_value)
print("The standard deviation of data is: ", sd_value)