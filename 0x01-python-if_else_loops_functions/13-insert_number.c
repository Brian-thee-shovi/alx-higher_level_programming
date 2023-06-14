#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts num into a linked list
 * @head: head of the llinked list
 * @number: num to be inserted in linked list
 * Return: address of new node or NULL -failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *temp;

	temp = *head;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while (temp->next != NULL)
	{
		if ((temp->next)->n >= number)
		{
			node->next = temp->next;
			temp->next = node;
			return (node);
		}
		temp = temp->next;
	}
	node->next = NULL;
	temp->next = node;
	return (node);
}
