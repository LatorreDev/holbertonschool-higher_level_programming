#include "lists.h"

/**
* check_cycle - entry point
* Return: 0 if is sucess
* @list: entry argument
*/

int check_cycle(listint_t *list)
{
	listint_t *x;
	listint_t *y;

	if (!list)
		return (0);
	x = list;
	y = list->next;
	while (x != y)
	{
		x = x->next;
		if (!x)
			return (0);
		y = y->next;
		if (!y)
			return (0);
		y = y->next;
		if (!y)
			return (0);
	}
	return (1);
}
