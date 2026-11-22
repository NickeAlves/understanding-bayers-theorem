![bayes-theorem-wikipedia-image](https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ed/Bayes_icon.svg/1920px-Bayes_icon.svg.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail)

# Summary

My goal is understanding how the Bayes' Theorem work and how I can apply this.

# Bayes' Theorem

## History

In probability theory, Bayes' theorem (alternatively Bayes' law or Bayes' rule), gives a mathematical rule for inverting conditional probabilities, allowing the probability of a cause to be found given its effect. For example, with Bayes' theorem, the probability that a patient has a disease given that they tested positive for that disease can be found using the probability that the test yields a positive result when the disease is present. The theorem was developed in the 18th century by Bayes and independently by Pierre-Simon Laplace.

One of Bayes' theorem's many applications is Bayesian inference, an approach to statistical inference, where it is used to invert the probability of observations given a model configuration (i.e., the likelihood function) to obtain the probability of the model configuration given the observations (i.e., the posterior probability).

This theorem is widely used in various fields, including machine learning, data science, and decision-making processes.

---

## Formula

<p align="center">
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/20251206130704617861/p_a_b_.webp">
</p>

<p align="center">
    <code> P(A∣B)=P(B∣A)×P(A)​/P(B) </code>
</p>

Where:

- P(A∣B) is the probability of A given B (posterior probability).
- P(B∣A) is the probability of B given A (likelihood).
- P(A) is the probability of A (prior probability).
- P(B) is the probability of B (evidence).

### Problem

Suppose a disease affects 1% of the population. A test for this disease is 99% accurate: it correctly identifies the disease in 99% of cases (true positive) and correctly identifies non-disease in 99% of cases (true negative). What is the probability that a person has the disease given they tested positive?

### Breakdown of the Problem

- P(Disease)=0.01 (prior probability of having the disease)
- P(No Disease)=0.99 (prior probability of not having the disease)
- P(Positive∣Disease)=0.99 (probability of testing positive given the disease)
- P(Positive∣No Disease)=0.01 (probability of testing positive given no disease)

We want to find P(Disease∣Positive), the probability of having the disease given a positive test result.

---

## References based

Wikipedia: [Bayes' theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem)

allglenn's Medium article: [Understanding Bayes’ Theorem](https://medium.com/@glennlenormand/understanding-bayes-theorem-4e283fefe4ec)

GeeksforGeeks: [Bayes' Theorem - GeeksforGeeks](https://www.geeksforgeeks.org/maths/bayes-theorem/)

---
