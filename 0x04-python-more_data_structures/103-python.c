#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Function outputs python lists's basic information
 * @p: a PyObject list object
*/
void print_python_list(PyObject *p)
{
	int size, allocate, j;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocate = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (j = 0; j < size; j++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", j, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[j]);
	}
}

/**
 * print_python_bytes - Function outputs basic info about python byte objects
 * @p: a PyObject list object
*/
void print_python_bytes(PyObject *p)
{
	unsigned char j, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
	{
		size = 10;
	}
	else
	{
		size = ((PyVarObject *)p)->ob_size + 1;
	}

	printf("  first %d bytes: ", size);

	for (j = 0; j < size; j++)
	{
		printf("%02hhx", bytes->ob_sval[j]);
		if (j == size - 1)
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}
