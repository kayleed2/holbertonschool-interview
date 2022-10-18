#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


int is_palindrome(listint_t **head)
{
    if (!head || !*head)
        return (1);

    return (palindrome_utility(head, *head));
}

/**
 * palindrome_utility - uses recursion to check palindrome
 *
 * @start: left of palindrome
 * @right: right to mid of palindrome
 *
 * Return: 1 if palindrome, else 0
 */
int palindrome_utility(listint_t **start, listint_t *right)
{
	if (!right)
		return (1);

	if (!palindrome_utility(start, right->next))
		return (0);

	if (right->n != (*start)->n)
		return (0);

	*start = (*start)->next;

	return (1);
}
