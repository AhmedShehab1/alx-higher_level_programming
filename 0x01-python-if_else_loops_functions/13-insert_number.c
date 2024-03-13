#include "lists.h"
/**
 * insert_node - Insert A Number Into a Sorted
 * Singly Linked List
 * @head: Pointer To Pointer to Start of The Linked List
 * @number: Number To Be Added To Inserted Node
 *
 * Return: Address of new node or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	if (head == NULL)
		return (NULL);
	temp = *head;
	if (temp->n > number)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (new);
		new->n = number;
		new->next = temp;
	}
	while (temp->next != NULL)
	{
		if ((temp->n < number) && (temp->next->n > number))
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (new);
			new->n = number;
			new->next = temp->next;
			temp->next = new;
			break;
		}
		temp = temp->next;
	}
	if (temp->next == NULL)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (new);
		new->next = NULL;
		new->n = number;
		temp->next = new;
	}
	return (new);
}
