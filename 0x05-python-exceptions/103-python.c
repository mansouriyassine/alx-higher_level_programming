#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = PyBytes_Size(p);
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (i = 0; i < 10 && i < size; ++i)
        printf("%02x ", (unsigned char)bytes->ob_sval[i]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, i;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; ++i)
    {
        PyObject *item = list->ob_item[i];
        const char *type_name = item->ob_type->tp_name;

        printf("Element %zd: %s\n", i, type_name);
        if (strcmp(type_name, "bytes") == 0)
            print_python_bytes(item);
    }
}

void print_python_float(PyObject *p)
{
    PyFloatObject *float_obj = (PyFloatObject *)p;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", float_obj->ob_fval);
}
