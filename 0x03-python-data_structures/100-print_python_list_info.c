#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Print information about a Python list
 * @p: PyObject representing a list
 *
 * Description: This function prints the size, allocated memory, and type of
 * each element in a Python list.
 */
void print_python_list_info(PyObject *p)
{
Py_ssize_t size, allocated, i;
PyObject *item;

size = PyList_Size(p);
allocated = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}
