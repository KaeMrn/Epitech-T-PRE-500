def calculate_series_sum(n):
    series_sum = 0
    current_term = 1
    series = []  # To store the series terms

    for _ in range(n):
        series.append(current_term)  # Append the current term to the series
        series_sum += current_term
        current_term = current_term * 10 + 1

    return series, series_sum

# Specify the number of terms in the series you want to add
n = int(input("enter the number of terms in the series: "))  # You can change this to the desired number of terms

series, result = calculate_series_sum(n)

print("The series is:", end=" ")
for term in series:
    print(term, end=" + ")
print("\b\b")  # To remove the extra '+ ' at the end

print(f"The sum of the series is: {result}")

for power in range (2,8):
    power_result = result ** power
    print (f"the sum raised to the power {power} is: {power_result}")
