'''
Question
The Professor is facing the North. Tokyo is in trouble, and she is facing the South. Professor being her guardian angel wants to help her.

So, The Professor will follow some instructions, given as a string S
of length N

, and will turn either left or right according to these instructions. He can save Tokyo only if after following a substring of instructions he will face in the same direction that Tokyo is facing.

Will the Professor be able to save Tokyo?
Input Format

    The first line contains an integer T

denoting the number of test cases. The T
test cases then follow.
The first line of each test case contains N

    .
    The second line contains a string that contains only 'L' and 'R', where 'L' represents left and 'R' represents right.

Output Format

For each test case, output "YES" if the Professor will be able to save Tokyo and "NO" otherwise.

Output is case insensitive, which means that "yes", "Yes", "YEs", "no", "nO" - all such strings will be acceptable.
'''
size=int(input())
for i in range(size):
    length=int(input())
    direction=input().strip()
    if 'LRRL' in direction or 'RLRLLL' in direction:
        print('YES')
    else:
        print('NO')
