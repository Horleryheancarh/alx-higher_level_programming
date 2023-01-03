#include "lists.h"

/**
 *insert_node - insert node at a given position
 *@head: head of a list
 *@number: index to insert the new node
 *
 *Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *curr;
	listint_t *prev;

	curr = *head;
	temp = malloc(sizeof(listint_t));

	if (temp == NULL)
		return (NULL);

	while (curr != NULL)
	{
		if (curr->n > number)
			break;

		prev = curr;
		curr = curr->next;
	}

	temp->n = number;

	if (*head == NULL)
	{
		temp->next = curr;
		*head = temp;
	}
	else
	{
		temp->next = curr;
		if (curr == *head)
			*head = temp;
		else
			prev->next = temp;
	}

	return (temp);
}
