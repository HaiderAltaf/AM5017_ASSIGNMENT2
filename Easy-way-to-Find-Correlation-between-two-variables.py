#!/usr/bin/env python
# coding: utf-8

# ### Find the Correlation using python code

# There are three methods to find the correlation between two data samples
# 1. Scatter Diagram 
# 2. Karl pearson method
# 3. Spearman's rank Correlation method

# ### Creating a python function to find correlation using anyone of the above methods

# In[ ]:


def find_correlation():
    
    # importing the required libraries
    import numpy as np
    import math
    import pandas as pd
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
    print("DATA PROCESSING==>>")
    # Asking the user, how the user want to feed data to find correlation between two variables.
    # Define the ANSI escape sequence for red color
    RED = "\033[1;31m"

    # Define the ANSI escape sequence to reset the color back to normal
    RESET = "\033[0m"
    print(RED,"Enter 1 for manual data entry, 2 if data is in csv file and 3 if data is in excel file: ",RESET)
    data_type = int(input())
    print(" ")
    
    if data_type ==1:
        
        # Taking the value of number of data in each sample(same for sample-1 and sample-2)
        N = int(input('What is the number of data in each sample: '))
        print(" ")

        # Enter the values in sample-1(a list)
        sample1 = [int(input(f'enter the value-{i} in sample1:')) for i in range(1,N+1)]
        print(" ")

        # Enter the values in sample-1(a list)
        sample2 = [int(input(f'enter the value-{i} in sample2:')) for i in range(1,N+1)]
        print(" ")
        print("sample1: ",sample1)
        print(" ")
        print("sample2: ",sample2)
        print(" ")
        
    elif data_type == 2:
        
        #Finding the path of the data
        path = input("Enter the path of the CSV file: ").replace('"', '')
        print(" ")

        try:
            # read the CSV file using pandas
            df = pd.read_csv(path)
            # display the data frame
            print(RED, "First five rows of your data are: ", RESET)
            print(" ")
            print(df.head())
            print(" ")
        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")
            
        #Asking user to find the correlation between samples of which variable
        print("We will find the correlation between the two variables")
        print(" ")
        column1 = int(input("Enter the column number of first variable: "))
        column2 = int(input("Enter the column number of second variable: "))
        
        print(" ")
        # finding the number of samples in the file
        N = len(df.iloc[:,column1-1])
        print(" ")
        # Values of first variable
        sample1= df.iloc[:,column1-1]
        print("The first five rows of sample1: ")
        print(sample1.head())
        print(" ")
        # Values of second variable
        sample2= df.iloc[:,column2-1]
        print("The first five rows of sample2: ")
        print( sample2.head())
        print(" ")
        
    elif data_type == 3:
        path = input("Enter the path of the excel file: ").replace('"', '')
        print(" ")

        try:
            # read the CSV file using pandas
            df = pd.read_excel(path)
            # display the data frame
            print(RED, "First five rows of your data are: ", RESET)
            print(" ")
            print(df.head())
            print(" ")
        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")
            
        #Asking user to find the correlation between samples of which variable
        print("We will find the correlation between the two variables")
        print(" ")
        column1 = int(input("Enter the column number of first variable: "))
        column2 = int(input("Enter the column number of second variable: "))
        
        print(" ")
        # finding the number of samples in the file
        N = len(df.iloc[:,column1-1])
        print(" ")
        # Values of first variable
        sample1= df.iloc[:,column1-1]
        print("The first five rows of sample1: ")
        print(sample1.head())
        print(" ")
        # Values of second variable
        sample2= df.iloc[:,column2-1]
        print("The first five rows of sample2: ")
        print( sample2.head())
        print(" ")
    
    
    # asking the method to find the correlation
    print("Selecting the method to find the correlation between the two samples")
    print(" ")
    print(RED, "Enter 1 for scatter plot, 2 for karl pearson, 3 for spearman's rank method: ",RESET)
    method = int(input())
    print(" ")
    

    # converting list to numpy array
    sample1, sample2 = np.array(sample1), np.array(sample2)
    
    ## FINDING THE CORRELATION BETWEEN THE ENTERED DATA
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
#         print("'r' is called as the correlation coefficient, if 0.75=<r<=1 => highly correlated")
#         print(" ")
#         print("if 0.25=<r<.75 => moderately correlated")
#         print(" ")
#         print("if 0=<r<.25 => low correlation")
#         print(" ")
        
        s1_mean, s2_mean = np.mean(sample1), np.mean(sample2)
        
        denominator = np.sqrt(np.sum((sample1 - s1_mean)**2)*np.sum((sample2 - s2_mean)**2))
        
        r = np.sum((sample1 - s1_mean)*(sample2 - s2_mean))/denominator
        
        if 0.75<=r<=1:
            print(f"The value of r is {r} => The samples are Highly Positive Correlated")
            print(" ")
            
        elif 0.25<=r<0.75:
            print(f"The value of r is {r} => The samples are Moderately Positive Correlated")
            print(" ")
        
        elif 0.25>=r>0:
            print(f"The value of r is {r} => The samples have Low Positive Correlation")
            print(" ")
            
        if -0.75>= r >= -1:
            print(f"The value of r is {r} => The samples are High negative Correlated")
            print(" ")
            
        elif -0.25>=r>-0.75:
            print(f"The value of r is {r} => The samples are Moderate negative Correlated")
            print(" ")
        
        elif -0.25<=r<0:
            print(f"The value of r is {r} => The samples have Low negative Correlation")
            print(" ")
        
        elif r==0:
            print(f"The value of r is {r} => The samples have No Correlation")
            print(" ")
    
    elif method == 3:
        print("Finding the coorelation using the Spearman's rank correlation method...")
        print(" ")
        rank_sample1, rank_sample2 = rankdata(sample1), rankdata(sample2)
        
        #print("rank of sample1",rank_sample1 )
        #print(" ")
        #print("rank of sample2",rank_sample2 )
        #print(" ")
        
        # for spearman's method we find, r= 1 - (6*sum(D**2))/(N(N**2-1)).
        # 'r' is the measure of rank correlation between the samples.
        # where, D= difference between the rank of the corresponding values in the samples
        # r=1 => samples are monotonically related
        # r=-1 => samples are monotonically related
        # for r>0 => the samples has similar rank.
        # for r<0 => the samples has dissimilar rank.
        
        # finding th value of 'r'
        r = 1 - (6*np.sum((rank_sample1 - rank_sample2)**2))/(N*(N**2 - 1))
        
        # find the probable error
        prob_error = 0.6745*(1- r*r)/np.sqrt(N)
        
        if r>0:
            print(f"The value of r is {r} => The ranks of the samples are similar=> positively Correlated")
            print(" ")
            print("Probable error: ",prob_error)
            print(" ")
            if r==1:
                print("samples are monotonically related")
                print(" ")
                  
        if r<0:
            print(f"The value of r is {r} => The ranks of the samples are dissimilar=> negaitively Correlated")
            print(" ")
            print("Probable error: ",prob_error)
            print(" ")
            
        if np.abs(r) > 6*prob_error:
            print("The Correlation is highly significance as r > 6*Probable error")
                
        if np.abs(r) <= 6*prob_error:
            print("The Correlation is not significance as r <= 6*Probable error")
            
    else:
        print("Run the code again and select correct method to calculate the correlation")
        print(" ")
     


# In[ ]:


find_correlation()


# In[ ]:




