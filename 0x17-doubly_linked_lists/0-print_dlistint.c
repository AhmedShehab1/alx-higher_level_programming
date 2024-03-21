#include "lists.h"
/**
 * print_dlistint - Prints All Elements Of a dlistint_t list
 * @h: Pointer To Head Node
 *
 * Return: Number Of Elements
*/
size_t print_dlistint(const dlistint_t *h)
{
	int No_Of_Elements = 0;
	dlistint_t *temp = h;

	while (temp != NULL)
	{
		printf("%d", temp->n);
		No_Of_Elements++;
		temp = temp->next;
	}
	return (No_Of_Elements);
}
