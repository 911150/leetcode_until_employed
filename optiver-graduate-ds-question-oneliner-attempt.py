import numpy as np
import random # can save a line here by using numpy random
import matplotlib.pyplot as plt

def find_food_q1():
    t, found, loc, food, steps = 0, False, [0,0], [2, -2], [(1,0), (-1,0), (0,1), (0,-1)]
    while (s := random.choice(steps)) and not found:
        loc[0], loc[1], t = loc[0] + s[0], loc[1] + s[1], t + 1
        if (loc[0] in food) or (loc[1] in food): return t 

def find_food_q2():
    t, found, loc, steps = 0, False, [0,0], [(1,0), (-1,0), (0,1), (0,-1)]
    while (s := random.choice(steps)) and not found:
        loc[0], loc[1], t = loc[0] + s[0], loc[1] + s[1], t + 1
        if loc[1] == -loc[0] + 1: return t

def find_food_q3():
    t, found, loc, steps = 0, False, [0,0], [(1,0), (-1,0), (0,1), (0,-1)]
    while (s := random.choice(steps)) and not found:
        loc[0], loc[1], t = loc[0] + s[0], loc[1] + s[1], t + 1
        cond = ((loc[0]-0.25) / 3) ** 2 + ((loc[1] - 0.25) / 40) ** 2 > 1
        if cond: return t


if __name__ == '__main__': 
    # question 1
    print(np.mean([find_food_q1() for x in range(0,10000)])) # 4.5 steps, i wonder why

    # question 2 # food located on diagonal line
    print(np.mean([find_food_q2() for x in range(0,1000)]))

    # question 3 # food located inside a circle ting
    print(np.mean([find_food_q3() for x in range(0,10000)])) 

    
    # # plotting visuals
    # # Q1
    # x1 = np.linspace(-100, 100, 100) # q1
    # y1 = -x1 + 1
    # plt.plot(x1,y1)
    # plt.axhline(0, color='black', linewidth=0.5)  # Horizontal line at y = 0
    # plt.axvline(0, color='black', linewidth=0.5)  # Vertical line at x = 0

    # # Q3
    # # Define the center and radius of the circle
    # center_x, center_y, radius_x, radius_y = 2.5, 2.5, 30, 40  # in cm
    # # Generate theta values from 0 to 2pi
    # theta = np.linspace(0, 2*np.pi, 100)
    # # Calculate x and y coordinates of the circle
    # x = center_x + radius_x * np.cos(theta)
    # y = center_y + radius_y * np.sin(theta)
    # # Create the plot
    # plt.plot(x, y)
    # plt.xlabel('x (cm)')
    # plt.ylabel('y (cm)')
    # plt.savefig('temp.png')



    



