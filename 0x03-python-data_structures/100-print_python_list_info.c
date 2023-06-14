#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/object.h"
#include "/usr/include/python3.4/listobject.h"
#include <stdio.h>

/**
 * print_python_list_info - prints basic info

 * @p: Pyobject list
 */
void print_python_list_info(PyObject *p)
{
	int length = 0;
	int k = 0;
	PyObject *ob_ject;
	PyListObject *info = (PyListObject *) p;

	length = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", (int) info->allocated);

	for (; k < length; ++k)
	{
		ob_ject = PyList_GET_ITEM(p, k);
		printf("Element %d: %s\n", k, ob_ject->ob_type->tp_name);
	}
	return;
}
