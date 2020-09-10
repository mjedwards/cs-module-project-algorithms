'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    jar = [0] * n
    count = 0
    # print(jar)
    # Your code here
    if len(jar) > 0:
        count += 1
        if n == 0: 
            return 
        return eating_cookies(n - 1)
        
    return count

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 2

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

# n = 3, 3 + (3 - 1)
# n = 2, 2 + (2 - 1)
# n = 1, 1