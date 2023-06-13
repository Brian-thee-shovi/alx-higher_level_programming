#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints basic info
 * @p: Pyobject list
 */
void print_python_list_info(PyObject *p)
{
	unsigned int index;
	unsigned int length;
	unsigned int locate;
	PyTypeObject *type;
	const char *num;

	if (p == NULL)
		return;
	length = (unsigned int) PyList_Size(p);
	locate = (unsigned int) ((PyListObject *)p)->locate;
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] locate = %d\n", locate);

	for (index = 0; index < length; index++)
	{
		type = PyList_GET_ITEM(p, index)->ob_type;
		num = type->tp_name;
		printf("Element %d: %s\n", index, num);
	}
}
