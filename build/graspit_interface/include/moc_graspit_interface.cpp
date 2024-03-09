/****************************************************************************
** Meta object code from reading C++ file 'graspit_interface.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.12.8)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../src/graspit_interface/include/graspit_interface.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'graspit_interface.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.12.8. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_GraspitInterface__GraspitInterface_t {
    QByteArrayData data[8];
    char stringdata0[214];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_GraspitInterface__GraspitInterface_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_GraspitInterface__GraspitInterface_t qt_meta_stringdata_GraspitInterface__GraspitInterface = {
    {
QT_MOC_LITERAL(0, 0, 34), // "GraspitInterface::GraspitInte..."
QT_MOC_LITERAL(1, 35, 26), // "emitRunPlannerInMainThread"
QT_MOC_LITERAL(2, 62, 0), // ""
QT_MOC_LITERAL(3, 63, 37), // "emitProcessPlannerResultsInMa..."
QT_MOC_LITERAL(4, 101, 29), // "emitBuildFeedbackInMainThread"
QT_MOC_LITERAL(5, 131, 22), // "runPlannerInMainThread"
QT_MOC_LITERAL(6, 154, 33), // "processPlannerResultsInMainTh..."
QT_MOC_LITERAL(7, 188, 25) // "buildFeedbackInMainThread"

    },
    "GraspitInterface::GraspitInterface\0"
    "emitRunPlannerInMainThread\0\0"
    "emitProcessPlannerResultsInMainThread\0"
    "emitBuildFeedbackInMainThread\0"
    "runPlannerInMainThread\0"
    "processPlannerResultsInMainThread\0"
    "buildFeedbackInMainThread"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_GraspitInterface__GraspitInterface[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       6,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       3,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   44,    2, 0x06 /* Public */,
       3,    0,   45,    2, 0x06 /* Public */,
       4,    0,   46,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       5,    0,   47,    2, 0x0a /* Public */,
       6,    0,   48,    2, 0x0a /* Public */,
       7,    0,   49,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void GraspitInterface::GraspitInterface::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<GraspitInterface *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->emitRunPlannerInMainThread(); break;
        case 1: _t->emitProcessPlannerResultsInMainThread(); break;
        case 2: _t->emitBuildFeedbackInMainThread(); break;
        case 3: _t->runPlannerInMainThread(); break;
        case 4: _t->processPlannerResultsInMainThread(); break;
        case 5: _t->buildFeedbackInMainThread(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (GraspitInterface::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GraspitInterface::emitRunPlannerInMainThread)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (GraspitInterface::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GraspitInterface::emitProcessPlannerResultsInMainThread)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (GraspitInterface::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GraspitInterface::emitBuildFeedbackInMainThread)) {
                *result = 2;
                return;
            }
        }
    }
    Q_UNUSED(_a);
}

QT_INIT_METAOBJECT const QMetaObject GraspitInterface::GraspitInterface::staticMetaObject = { {
    &QObject::staticMetaObject,
    qt_meta_stringdata_GraspitInterface__GraspitInterface.data,
    qt_meta_data_GraspitInterface__GraspitInterface,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *GraspitInterface::GraspitInterface::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *GraspitInterface::GraspitInterface::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_GraspitInterface__GraspitInterface.stringdata0))
        return static_cast<void*>(this);
    if (!strcmp(_clname, "Plugin"))
        return static_cast< Plugin*>(this);
    return QObject::qt_metacast(_clname);
}

int GraspitInterface::GraspitInterface::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 6;
    }
    return _id;
}

// SIGNAL 0
void GraspitInterface::GraspitInterface::emitRunPlannerInMainThread()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void GraspitInterface::GraspitInterface::emitProcessPlannerResultsInMainThread()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void GraspitInterface::GraspitInterface::emitBuildFeedbackInMainThread()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
