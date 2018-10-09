
#include "Python.h"

static PyObject* longest(PyObject *self, PyObject *value) {
    #if PY_MAJOR_VERSION < 3
      PyObject* module = PyImport_ImportModule("__builtin__");
    #else
      PyObject* module = PyImport_ImportModule("builtins");
    #endif
    if (!module)
        return NULL;

    PyObject* module_dict = PyModule_GetDict(module);
    PyObject* len = PyDict_GetItemString(module_dict, "len");
    if (!len) {
        Py_DECREF(module);
        return NULL;
    }
    PyObject* max = PyDict_GetItemString(module_dict, "max");
    if (!max) {
        Py_DECREF(module);
        return NULL;
    }
    Py_DECREF(module);

    PyObject* args = PyTuple_New(1);
    if (!args) {
        return NULL;
    }
    Py_INCREF(value);
    PyTuple_SetItem(args, 0, value);

    PyObject* kwargs = PyDict_New();
    if (!kwargs) {
        Py_DECREF(args);
        return NULL;
    }
    PyDict_SetItemString(kwargs, "key", len);

    PyObject* result = PyObject_Call(max, args, kwargs);

    Py_DECREF(args);
    Py_DECREF(kwargs);

    return result;
}

PyDoc_STRVAR(longest_doc, "Docstring for longest function.");

static struct PyMethodDef module_functions[] = {
    {"longest", longest, METH_O, longest_doc},
    {NULL, NULL}
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "componentry._componentry", /* m_name */
    NULL,             /* m_doc */
    -1,               /* m_size */
    module_functions, /* m_methods */
    NULL,             /* m_reload */
    NULL,             /* m_traverse */
    NULL,             /* m_clear */
    NULL,             /* m_free */
};
#endif

static PyObject* moduleinit(void) {
    PyObject *module;

#if PY_MAJOR_VERSION >= 3
    module = PyModule_Create(&moduledef);
#else
    module = Py_InitModule3("componentry._componentry", module_functions, NULL);
#endif

    if (module == NULL)
        return NULL;

    return module;
}

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC init_componentry(void) {
    moduleinit();
}
#else
PyMODINIT_FUNC PyInit__componentry(void) {
    return moduleinit();
}
#endif

