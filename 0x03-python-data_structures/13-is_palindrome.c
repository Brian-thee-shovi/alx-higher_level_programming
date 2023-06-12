#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
/**
 * reverse_listint - func that reverses a singly linked list
 * @head: pointer to a pointer
 * Return: pointer to the reversed singly linked list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head;
	listint_t *next_node;
	listint_t *prev_node = NULL;

	while (node)
	{
		next_node = node->next;
		node->next = prev_node;
		prev_node = node;
		node = next_node;
	}
	*head = prev_node;
	return (*head);
}
/**
 * is_palindrome - checks if singly list is a palindrome
 * @head: pointer to a pointer
 * Return: zero if palindrome and 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *k, *verse, *kati;
	size_t size = 0;
	size_t kim = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	k = *head;
	while (k)
	{
		size++;
		k = k->next;
	}
	k = *head;

	while (kim < (size / 2) - 1)
	{
		k = k->next;
		kim++;
	}
	if ((size % 2) == 0 && k->n != k->next->n)
		return (0);
	k = k->next->next;
	verse = reverse_listint(&k);
	kati = verse;

	k = *head;
	while (verse)
	{
		if (k->n != verse->n)
			return (0);
		k = k->next;
		verse = verse->next;
	}
	reverse_listint(&kati);
	return (1);
}


