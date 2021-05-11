#include <stdio.h>
#include <stdlib.h>

#include "header.h"

void reverse_string(char *str, int len)
{
	int i, j;
	char tmp;

	for (i = 0, j = len - 1; i < j; i++, j--)
	{
		tmp = str[i];
		str[i] = str[j];
		str[j] = tmp;
	}
}

int main()
{
	char s[] = "Daniela Ramirez";
	reverse_string(s, 15);
	printf("%s \n", s);
	return 0;
}