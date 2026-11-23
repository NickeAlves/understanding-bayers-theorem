def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    p_not_a = 1 - p_a
    p_b = (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)
    return (p_b_given_a * p_a) / p_b

# assigning the values based on our problem
p_disease = 0.01
p_positive_given_disease = 0.99
p_negative_given_no_disease = 0.01

# calculating the probability of having the disease given a positive test result

p_disease_given_positive = bayes_theorem(p_disease, p_positive_given_disease, p_negative_given_no_disease)

print(f"The probability of having the disease given a positive test result is: {p_disease_given_positive:.2%}")