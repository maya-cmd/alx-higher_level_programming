#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Function outputs  PyFloatObject data
 * @p:The PyObject
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_bytes - Function outputs PyBytesObject
 * @p: The PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, j = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (j < size + 1 && j < 10)
	{
		printf(" %02hhx", str[j]);
		j++;
	}
	printf("\n");
}
/**
 * print_python_list - Function outputs PyListObject data
 * @p: The PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int j = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (j < size)
		{
			item = PyList_GET_ITEM(p, j);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			j++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
