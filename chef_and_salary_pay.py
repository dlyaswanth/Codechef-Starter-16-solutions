'''
Question 
Given the schedule of Chef for 30 days (A binary string of length 30 where '0' denotes that Chef was on leave and '1' denotes Chef was working on that day). Chef gets X−

Rs for every day he worked. As working continuously for a long time is hectic so Company introduced the following policy to give a bonus to its employees.

The company will check the longest streak for which an employee has worked and will award Y−

Rs for every day of that streak as a bonus. Calculate the salary received by Chef (including the bonus).

Note: Rs represents the currency of Chefland, and if there are two or more longest streaks of the same length, only one is counted for the bonus.
Input Format

    The first line contains an integer T

denoting the number of test cases. The T
test cases then follow.
The first line of each test case contains X
and Y

    .
    Second line contains a binary string (i.e it contains only ‘0’ / ‘1’), where '0' denotes that Chef was on leave and '1' denotes Chef was working on that day.

Output Format

    For each testcase, output in a single line answer to the problem. i.e The salary received by Chef (including the bonus).

'''

size=int(input())
for i in range(size):
    x,y=map(int,input().split())
    days=input().strip()
    salary=(days.count('1')*x)
    temp,flg=0,1;
    for i in range(len(days)):
        if i<len(days)-1:
            if days[i]=='1' and days[i+1]=='1':
                flg+=1;
            else:
                if temp<flg:
                    temp=flg;
                flg=1;
        else:
            if days[i-1]=='1' and days[i]=='1':
                flg+1;
            if temp<flg:
                temp=flg;
    salary+=(temp*y)
    print(salary)
