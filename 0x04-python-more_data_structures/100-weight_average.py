#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple (<score>, <weight>)
    Args:
        my_list: List of tuples where each tuple is (score, weight)
    Returns:
        The weighted average, or 0 if the list is empty
    """
    if not my_list:
        return 0
    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)
    return total_score / total_weight
