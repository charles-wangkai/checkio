#!/usr/bin/env python3

def search(weights, index, left_sum):
    if index == len(weights):
        return abs(sum(weights) - left_sum * 2)
    
    return min(search(weights, index + 1, left_sum), search(weights, index + 1, left_sum + weights[index]))

def checkio(data):
    return search(data, 0, 0)
    
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
