#include "lists.h"

int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n != temp2->n)
			return (0);
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}

listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;
	listint_t *second_half, *prev_of_slow = *head;
	listint_t *midnode = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_of_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}

		second_half = reverse_list(&slow);
		prev_of_slow->next = NULL;

		res = compare_lists(*head, second_half);

		reverse_list(&second_half);

		if (midnode != NULL)
		{
			prev_of_slow->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_of_slow->next = second_half;
	}

	return (res);
}

