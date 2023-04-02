#!/usr/bin/env python
# coding: utf-8

# ### Find the Correlation using python code

# There are three methods to find the correlation between two data samples
# 1. Scatter Diagram 
# 2. Karl pearson method
# 3. Spearman's rank Correlation method

# ### Creating a python function to find correlation using anyone of the above methods

# In[7]:


def find_correlation():
    
    # importing the required libraries
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    from scipy.stats import rankdata
    
    """
    This function will find the correlation between two samples of data.
    User has to give sample1 and sample2 as integers
    user has to choose any of the three methods to find the correlation.
    There are three methods to find the correlation between two data samples
    1. Scatter Plot method
    2. Karl pearson method
    3. Spearman's rank correlation method
    
    """
    # Taking the value of number of data in each sample(same for sample-1 and sample-2)
    N = int(input('What is the number of data in each sample: '))
    print(" ")
    
    # Enter the values in sample-1(a list)
    sample1 = [int(input(f'enter the value-{i} in sample1:')) for i in range(1,N+1)]
    print(" ")
    
    # Enter the values in sample-1(a list)
    sample2 = [int(input(f'enter the value-{i} in sample2:')) for i in range(1,N+1)]
    print(" ")
    
    # asking the method to find the correlation
    print("Selecting the method to find the correlation between the two samples")
    print(" ")
    method = int(input("Enter 1 for scatter plot, 2 for karl pearson, 3 for spearman's rank method: "))
    print(" ")
    
    print("sample1: ", sample1)
    print(" ")
    print("sample2: ", sample2)
    print(" ")
    # converting list to numpy array
    sample1, sample2 = np.array(sample1), np.array(sample2)
    
    if method == 1:
        print("Finding the coorelation using scatter diagram method...")
        print(" ")
        
        # find the coefficient of concurrent deviation(CCD)
        # r**2 = (2*c-N)/N, if r**2>0 => +vely correlated
        # elif r**2<0 => -vely correlated else no correlation
        dx, dy, C = 0, 0, 0
        x0, y0 = sample1[0], sample2[0]
        for x, y in zip(sample1[1:], sample2[1:]):
            if (x-x0)*(y-y0)>0:
                C+=1
            x0, y0 = x, y
        
        CCD = (2*C-N)/N
        if CCD>0:
            print(f"The coefficient of concurrent deviation(CCD),{CCD} > zero, so")
            print(" ")
            print("The samples are positively correlated to each other")
        elif CCD<0:
            print(f"The coefficient of concurrent deviation(CCD),{CCD} < zero, so")
            print(" ")
            print("The samples are negatively correlated to each other")
        else:
            print("The coefficient of concurrent deviation(CCD) = zero, so")
            print(" ")
            print("The samples are not correlated to each other")
        
        # Plot the scatter diagram
        plt.scatter(sample1, sample2)
        plt.title("The scatter plot")
        plt.xlabel("sample1")
        plt.ylabel("sample2")
        plt.show() 
            
          
    elif method == 2:
        print("Finding the coorelation using Karl pearson method...")
        print(" ")
        print("'r' is called as the correlation coefficient, if 0.75=<r<=1 => highly correlated")
        print(" ")
        print("if 0.25=<r<.75 => moderately correlated")
        print(" ")
        print("if 0=<r<.25 => low correlation")
        print(" ")
        
        s1_mean, s2_mean = np.mean(sample1), np.mean(sample2)
        
        denominator = np.sqrt(np.sum((sample1 - s1_mean)**2)*np.sum((sample2 - s2_mean)**2))
        
        r = np.sum((sample1 - s1_mean)*(sample2 - s2_mean))/denominator
        
        if 0.75<=r<=1:
            print(f"The value of r is {r} => The samples are Highly Correlated")
            print(" ")
            
        elif 0.25<=r<0.75:
            print(f"The value of r is {r} => The samples are Moderately Correlated")
            print(" ")
        
        else:
            print(f"The value of r is {r} => The samples have Low Correlation")
            print(" ")
    
    elif method == 3:
        print("Finding the coorelation Spearman's rank correlation method...")
        print(" ")
        rank_sample1, rank_sample2 = rankdata(sample1), rankdata(sample2)
        
        print("rank of sample1",rank_sample1 )
        print(" ")
        print("rank of sample2",rank_sample2 )
        print(" ")
        
        # for spearman's method we find, r= 1 - (6*sum(D**2))/(N(N**2-1)).
        # 'r' is the measure of rank correlation between the samples.
        # where, D= difference between the rank of the corresponding values in the samples
        # r=1 => samples are monotonically related
        # r=-1 => samples are monotonically related
        # for r>0 => the samples has similar rank.
        # for r<0 => the samples has dissimilar rank.
        
        # finding th value of 'r'
        r = 1 - (6*np.sum((rank_sample1 - rank_sample2)**2))/(N*(N**2 - 1))
        
        if r>0:
            print(f"The value of r is {r} => The ranks of the samples are similar=> positively Correlated")
            print(" ")
            if r==1:
                print("samples are monotonically related")
                print(" ")
            
        elif r<0:
            print(f"The value of r is {r} => The ranks of the samples are dissimilar=> negaitively Correlated")
            print(" ")
            
    else:
        print("Run the code again and select correct method to calculate the correlation")
        print(" ")
     


# In[12]:


find_correlation()

