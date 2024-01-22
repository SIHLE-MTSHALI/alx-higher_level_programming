#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list pointer
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	const char *type;

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	for (i = 0; i < size; i++)
	{
		type = PyList_GetItem(p, i)->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject byte object pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", string[i] & 0xff);
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: PyObject float object pointer
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	printf("  value: %g\n", value);
}

