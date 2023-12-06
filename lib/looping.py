#!/usr/bin/env python3

def happy_new_year():
    num=10
    while (num>0):
        print(num)
        num=num-1
        if (num==0):
            print("Happy New Year!")

    

def square_integers(int_list):
    new_list = [int * int for int in int_list]
    return new_list

def fizzbuzz():
    for x in range(1,101):
        if (x%3)==0 and (x%5)==0:
            print("FizzBuzz")
        elif (x%3)==0:
            print("Fizz")
        elif (x%5)==0:
            print("Buzz")
        else:
            print(x)
