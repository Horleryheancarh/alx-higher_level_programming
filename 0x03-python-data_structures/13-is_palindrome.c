#include "lists.h"

/**
 *reverse - reverses the second half of the list
 *@head: head of the second half
 *
 *Return: void
 */
void reverse(listint_t **head)
{
	listint_t *prev;
	listint_t *curr;
	listint_t *temp;

	prev = NULL;
	curr = *head;

	while (curr != NULL)
	{
		temp = curr->next;
		curr->next = prev;
		prev = curr;
		curr = temp;
	}

	*head = prev;
}

/**
 *compare - compare each integer of the list
 *@h1: head of first half
 *@h2: head of second half
 *
 *Return: 1 if are equals, 0 otherwise
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = h1;
	temp2 = h2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}

/**
 *is_palindrome - checks if a list is a palindrome
 *@head: pointer to head of list
 *
 *Return: 0 if its not a palindrome, 1 if its a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev;
	listint_t *half, *middle;
	int i;

	slow = fast = prev = *head;
	middle = NULL;
	i = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		half = slow;
		prev->next = NULL;
		reverse(&half);
		i = compare(*head, half);

		if (middle != NULL)
		{
			prev->next = middle;
			middle->next = half;
		}
		else
			prev->next = half;
	}

	return (i);
}
