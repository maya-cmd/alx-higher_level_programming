#include "lists.h"
#include <stddef.h>

/**
 * rev_list - Function reverses a linked list
 * @head: A linked list's head node
 *
 * Return: a lst that has been reversed
*/

listint_t *rev_list(listint_t *head)
{
	listint_t *old = NULL;
	listint_t *new = head;
	listint_t *next = NULL;

	while (new != NULL)
	{
		next = new->next;
		new->next = old;
		old = new;
		new = next;
	}

	return (old);
}

/**
 * is_palindrome - Function confirms if a singly linked list is a plaindrome
 * @head: A linked list's head node
 *
 * Return: 0 if not palindrome and 1 if is palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *slower_ptr = *head;
	listint_t *faster_ptr = *head;
	listint_t *half_two;
	listint_t *old_slow_ptr = *head;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (faster_ptr != NULL && faster_ptr->next != NULL)
		{
			faster_ptr = faster_ptr->next->next;
			old_slow_ptr = slower_ptr;
			slower_ptr = slower_ptr->next;
		}

		if (faster_ptr != NULL)
		{
			slower_ptr = slower_ptr->next;
		}

		half_two = rev_list(slower_ptr);

		while (*head != NULL && half_two != NULL)
		{
			if ((*head)->n != half_two->n)
			{
				is_palindrome = 0;
				break;
			}
			*head = (*head)->next;
			half_two = half_two->next;
		}

		half_two = rev_list(half_two);
		old_slow_ptr->next = half_two;
	}

	return (is_palindrome);
}
