#include <stdio.h>

int main()
{
	int a, b; //�Է°�
	int resultAdd, resultSub, resultMult, resultDiv, resultRem; //�����
	scanf("%d""%d", &a, &b);
	resultAdd = a + b;
	resultSub = a - b;
	resultMult = a * b;
	resultDiv = a / b;
	resultRem = a % b;
	printf("%d\n%d\n%d\n%d\n%d", resultAdd, resultSub, resultMult, resultDiv, resultRem);
	return 0;
}