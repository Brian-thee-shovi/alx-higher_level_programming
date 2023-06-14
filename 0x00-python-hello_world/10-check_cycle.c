#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks  if a singly linked list has a cycle in it.
 * @list: list being checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *line = list;
	listint_t *other = list;
	int result = 0;

	while ((line && other) && other->next)
	{
		line = line->next;
		if (other->next || other->next->next)
			other = other->next->next;
		else
			break;
		if (line == other)
		{
			result = 1;
			break;
		}
	}
	return (result);
}
