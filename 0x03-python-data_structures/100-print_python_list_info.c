#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Function outputs basic info about python lists
 * @p: a Pyobject list
*/

void print_python_list_info(PyObject *p)
{
	int size = Py_Size(p);
	int j, allocate;
	PyListObject *obj;

	allocate = ((PyListObject *)p) ->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);
	
	for (j = 0; j < size; j++)
		printf("Element %d: ", j);
		obj = PyList_GetItem(p, j);       
		printf("%s\n", Py_TYPE(obj)->tp_name);
}
