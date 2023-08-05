"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #8 - Optimize Scan (optimizescan.py)


Author: Chris Lai

Difficulty Level: 5/10

Prompt: A RACECAR with an IR camera and LIDAR has been tasked to scan a certain area around 
a secret lab. In the image below, the RACECAR’s traversal pattern is provided with the following details:

- The RACECAR will always start from the charging ports as seen in “C”.
- The RACECAR will then travel to points “A” or “B” based on the transition distance variable “tdist”. 
- The RACECAR scans the area between itself and the lab (what is this????) and travels between points “A” and “B” based on the scanning distance variable “sdist”.
- Once the RACECAR reaches the other checkpoint (A or B), it returns to the charging port “C”.

Assume that the RACECAR uses 250mAh on average for every 1 meter of travel (including for motors + scanning).
If the RACECAR has a battery capacity determined by the variable “battcap” (in mAh), determine the maximum 
area (in meters squared, as represented by tdist * sdist) that the RACECAR could scan on one full charge.
Do not import any libraries to solve this problem.

Constraints: Do not import any libraries to solve this problem.
Solve this question in one line!

Test Cases:
Input: 125000 ; Output: 31250.00
Input: 10000 ; Output: 200.00
Input: 404 ; Output: 0.33
"""

class Solution:    
    def optimizescan(self, battcap):
        # Input type: Integer
        # return type: float

        #TODO: Write code below to return a float with the solution to the prompt.
        # 250 mAh
        return (battcap / 250.0) ** 2 / 8.0

def main():
    battcap = int(input())

    tc1 = Solution()
    ans = tc1.optimizescan(battcap)
    print("%.2f" % ans)

if __name__ and "__main__":
    main()
