#include "lists.h"
/**
 * check_cycle - Checks If A Singly linked
 * list has a cycle in it
 * @list: pointer to the linked list
 *
 * Return: 1 if cycle exist 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *temp;
	short int flag = 0;

	temp = list;
	while (temp != NULL)
	{
		if (temp->next == list)
		{
			flag = 1;
			break;
		}
		temp = temp->next;
	}
	if (flag == 1)
		return (flag);
	return (flag);
}
