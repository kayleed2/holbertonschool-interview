#include <stdio.h>
#include <stdlib.h>
#include "palindrome.h"


int is_palindrome(unsigned long n)
{
	unsigned long reversed, remainder;
	unsigned long original = n;

    if (!n)
        return (0);

	while (n != 0)
	{
		remainder = n % 10;
		reversed = reversed * 10 + remainder;
		n /= 10;
	}

	if (original == reversed || original == 0)
		return (1);
	
	return (0);
}
