def leibniz(n):
    t_sum = 0
    for i in range(n):
        term = (-1) ** i /(2*i+1)
        t_sum = t_sum + term
    
    return t_sum * 4

terms= int(input("enter number of terms:"))
pi = leibniz(terms)
formatted_pi= f"{pi: .6f}"
print("approximation of pi=", formatted_pi)
