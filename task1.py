#! python3
"""
Ask the user for their name and their email address.
(2 points)

Inputs:
 name
 email

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.

example:
What is your name:Dwayne Johnson
What ir your email:rock@aol.com

Your name is Dwayne Johnson, and your email is rock@aol.com

What is your name:Jackie Chan
What ir your email:crazyAsian@qq.com

Your name is Jackie Chan, and your email is crazyAsian@qq.com

"""
question1 = "What is your name?"
responce1 = input(question1)
question2 = "What is your email?"
responce2 = input(question2)
print(f"Your name is {responce1}, and your email is {responce2}")