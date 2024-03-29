#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_GET_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	trying_str = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", trying_str);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" %02hhx", trying_str[i]);
	}

	printf("\n");
}
