#include <stddef.h>
#include "lists.h"

/**
 * compare_lists - Compares two linked lists.
 * @list1: Pointer to the head of the first list.
 * @list2: Pointer to the head of the second list.
 *
 * Return: 1 if the lists are identical, 0 otherwise.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return (0);

        list1 = list1->next;
        list2 = list2->next;
    }

    if (list1 == NULL && list2 == NULL)
        return (1);

    return (0);
}

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to a pointer to the head of the list.
 */
void reverse_list(listint_t **head)
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

    *head = prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr, *fast_ptr;
    listint_t *prev_slow_ptr, *mid_node;
    int is_palindrome = 1;

    slow_ptr = fast_ptr = *head;
    mid_node = NULL;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast_ptr != NULL && fast_ptr->next != NULL)
        {
            fast_ptr = fast_ptr->next->next;

            prev_slow_ptr = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        if (fast_ptr != NULL)
        {
            mid_node = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        prev_slow_ptr->next = NULL;
        reverse_list(&slow_ptr);

        is_palindrome = compare_lists(*head, slow_ptr);

        reverse_list(&slow_ptr);

        if (mid_node != NULL)
        {
            prev_slow_ptr->next = mid_node;
            mid_node->next = slow_ptr;
        }
        else
        {
            prev_slow_ptr->next = slow_ptr;
        }
    }

    return (is_palindrome);
}
