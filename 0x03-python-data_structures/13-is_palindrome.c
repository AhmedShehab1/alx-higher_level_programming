#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - Checks Wether Singly LL
 * is a palindrome
 * @head: Address of Pointer To First Node
 *
 * Return: 1 if palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *Start, *End, *Temp;
	int Flag = 0;

	if ((*head) == NULL)
	{
	return (1);
	}
	End = NULL;
	Start = *head;
	for (; ; Start = Start->next, End = Temp)
	{
	Temp = Start;
	while (Temp->next != End)
		Temp = Temp->next;
	if (Temp->n != Start->n)
	{
		Flag = 1;
		break;
	}
	if (Start->next == Temp || Start == Temp)
		break;
	}
	if (Flag == 1)
	return (0);
	return (1);
}
