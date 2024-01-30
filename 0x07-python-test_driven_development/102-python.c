#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: PyObject string object.
 */
void print_python_string(PyObject *p)
{
	/* Check if p is a valid string */
	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n  [ERROR] Invalid String Object\n");
		return;
	}

	/* Print the string type, length, and contents */
	printf("[.] string object info\n");
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}
