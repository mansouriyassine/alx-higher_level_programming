#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to the Python object
 */
void print_python_string(PyObject *p)
{
if (PyUnicode_Check(p))
{
Py_ssize_t length = PyUnicode_GET_LENGTH(p);
const char *type = PyUnicode_IS_COMPACT_ASCII(p) ?
"compact ascii" : "compact unicode object";
const wchar_t *value = PyUnicode_AsWideCharString(p, NULL);

if (value != NULL)
{
printf("[.] string object info\n");
printf("  type: %s\n", type);
printf("  length: %ld\n", length);
printf("  value: %ls\n", value);
PyMem_Free((void *)value);
}
else
{
PyErr_Print();
}
}
else
{
printf("[.] string object info\n");
printf("  [ERROR] Invalid String Object\n");
}
}

/**
 * main - Entry point of the program
 *
 * Return: Always 0
 */
int main(void)
{
Py_Initialize();
PyObject *s = PyUnicode_DecodeUTF8("The spoon does not exist", 24, NULL);
print_python_string(s);
s = PyUnicode_DecodeUTF8("ложка не существует", 19, NULL);
print_python_string(s);
s = PyUnicode_DecodeUTF8("La cuillère n'existe pas", 24, NULL);
print_python_string(s);
s = PyUnicode_DecodeUTF8("勺子不存在", 5, NULL);
print_python_string(s);
s = PyUnicode_DecodeUTF8("숟가락은 존재하지 않는다.", 14, NULL);
print_python_string(s);
s = PyUnicode_DecodeUTF8("スプーンは存在しない", 10, NULL);
print_python_string(s);
s = PyBytes_FromString("The spoon does not exist");
print_python_string(s);
Py_Finalize();
return (0);
}
