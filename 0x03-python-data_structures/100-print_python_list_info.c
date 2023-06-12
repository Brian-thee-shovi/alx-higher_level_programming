#include <stdio.h>
#include "/usr/include/python3.4/object.h"
#include "usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/Python.h"

/**
 * print_python_list_info - prints basic info
 * @p: Pyobject list
 */
void print_python_list_info(PyObject *p)
{
	int size = 0;
	int yy = 0;
	PyObject *ob_ject;
	PyListObject *hey = (PylistObject *) p;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int) hey->allocated);

	for (; yy < size; ++yy)
	{
		ob_ject = PyList_GET_ITEM(p, yy);
		printf("Element %d: %s\n", yy, ob_ject->ob_type->tp_name)
	}
return;
}
