#include "lists.h"
/**
 * dlistint_len - Return Number Of Elements in a dlistint_t list
 * @h: Pointer To Head Node
 *
 * Return: Number Of Elements
*/
size_t dlistint_len(const dlistint_t *h)
{
	int No_Of_Elements = 0;
	dlistint_t *temp = h;

	while (temp != NULL)
	{
		No_Of_Elements++;
		temp = temp->next;
	}
	return (No_Of_Elements);
}
