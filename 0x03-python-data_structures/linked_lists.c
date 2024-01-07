#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current = h;
    size_t n = 0;

    while (current)
    {
        printf("%d\n", current->n);
        current = current->next;
        n++;
    }

    return n;
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element, or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new = malloc(sizeof(listint_t));
    listint_t *current;

    if (new == NULL)
        return NULL;

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
    {
        *head = new;
    }
    else
    {
        current = *head;
        while (current->next)
            current = current->next;
        current->next = new;
    }

    return new;
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head)
    {
        current = head;
        head = head->next;
        free(current);
    }
}

