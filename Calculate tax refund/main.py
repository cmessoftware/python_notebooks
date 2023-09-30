import numpy as np
import matplotlib.pyplot as plt

def calculate_minimum_purchase_amount():
    # Initialize the target refund amount
    target_refund = 18800
    
    # Initialize X with a small value and a step size
    X = 1000
    step = 1000
    refunds = []
    
    while True:
        # Calculate the accumulated refund over five cycles
        accumulated_refund = 0
        tax_refund = X
        for _ in range(5):
            # total_price = X * 1.21  # Calculate the total price including tax
            tax_refund =  tax_refund * 0.21  # Calculate the tax refund for this cycle
            accumulated_refund += tax_refund
            #X = tax_refund  # Calculate the new X for the next cycle
        
        print(f'Accumulate refund {accumulated_refund}')
        refunds.append(accumulated_refund)
        # Check if the accumulated refund is greater than or equal to the target
        if accumulated_refund >= target_refund:
            return X,refunds
        
        # If not, increment X with the step size and continue the search
        X += step
       

def show_accumulate_refunds(refunds):
    # data to be plotted
    x = np.arange(1, len(refunds)+1)
    
    # plotting
    plt.title("Accumulate Refunds")
    plt.xlabel("Cycles")
    plt.ylabel("$")
    plt.plot(x, refunds, color ="red")
    plt.show()
    
# Calculate and print the minimum initial purchase amount
minimum_purchase_amount,refunds = calculate_minimum_purchase_amount()
print(f"Minimum initial purchase amount: ${minimum_purchase_amount:.2f}")
show_accumulate_refunds(refunds)