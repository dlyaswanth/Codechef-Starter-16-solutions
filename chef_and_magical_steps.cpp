/*
Question 
Chef has a new customer and he wants to prepare his order as soon as possible. While preparing, he sees that the mint sauce is finished. He has to run upstairs to get it from other kitchen. Chef is currently on the Xth stair. He has to climb all the way up to the Yth

stair in minimum number of steps. In one step, Chef can do one of the following things:

    Climb a single stair. ( i.e go from the Xth

stair to the (X+1)th
stair. )
Climb two stairs only if the final stair falls at a prime number position. ( i.e. go from the Xth
stair to the (X+2)th stair, only if (X+2

    ) is a prime number)

Help Chef reach the Yth
stair from the Xth

stair in minimum number of steps.

See Explanation for more clarity.

Note: The input files are large. The use of Fast I/O is recommended.
Input Format

    The first line contains an integer T

denoting the number of test cases. The T
test cases then follow.
The first line of each test case contains X
and Y

    denoting the starting stair and ending stair respectively.

Output Format

    Output a single integer representing minimum number of steps chef can take to reach from Xth

to Yth stair.
*/
#include <iostream>
#include <cmath>
using namespace std;
int isprime(int number)
{
    int i=2;
    while (i*i<=number)
    {
        if (number%i==0)
        return 0;
        i+=1;
    }
    return 1;
}
int main() 
{
	int rows;
	scanf("%d",&rows);
	while (rows>0)
	{
	    int a,b,steps=0;
	    scanf("%d %d",&a,&b);
	    while(a<b)
	    {
	        if (isprime(a+2)==1)
	        a+=2;
	        else
	        a+=1;
	        steps+=1;
	    }
	    printf("%d\n",steps);
	    rows--;
	}
	return 0;
}
// Note: Time Limit Exceed.
