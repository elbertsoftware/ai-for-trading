# Udacity - AI for Trading
# Term 2 - Lesson 16 - Quiz
# Quiz for Maximizing Information Gain
# For the following quiz, consider the data found in ml-bugs.csv
# consisting of twenty-four made-up insects measured on their length and color.
# Which of the following splitting criteria provides the most information gain for discriminating Mobugs from Lobugs?

import numpy as np


def two_group_entropy(first, total):                        
    return -(first/total*np.log2(first/total) +           
            (total-first)/total*np.log2((total-first)/total))

# 10 mobugs vs. 24 in total
total_entropy = two_group_entropy(10, 24)

# length < 17 mm -> group 1 has 15, group 2 has 9
g17_entropy = 15/24 * two_group_entropy(11,15) # 11 lobugs vs. 15 in total of group 1
g17_entropy += 9/24 * two_group_entropy(6,9)  # 6 mobugs vs. 9 in total of group 2    

information_gain = total_entropy - g17_entropy  # 0.1126
print(information_gain)