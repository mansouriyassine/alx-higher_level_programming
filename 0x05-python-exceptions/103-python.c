nclude <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
if (!PyList_Check(p))
{
printf("[ERROR] Invalid PyListObject\n");
return;
}

Py_ssize_t size = PyList_Size(p);
PyObject *item;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (Py_ssize_t i = 0; i < size; ++i)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}

void print_python_bytes(PyObject *p)
{
if (!PyBytes_Check(p))
{
printf("[ERROR] Invalid PyBytesObject\n");
return;
}

Py_ssize_t size = PyBytes_Size(p);
char *bytes_data = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %zd\n", size);
printf("  trying string: %s\n", bytes_data);

printf("  first %zd bytes: ", (size > 10) ? 10 : size);
for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
printf("%02hhx", bytes_data[i]);
if (i < 9 && i + 1 < size) {
printf(" ");
}
}
printf("\n");
}

void print_python_float(PyObject *p)
{
if (!PyFloat_Check(p))
{
printf("[ERROR] Invalid PyFloatObject\n");
return;
}

printf("[.] float object info\n");
printf("  value: %lf\n", ((PyFloatObject *)p)->ob_fval);
}
