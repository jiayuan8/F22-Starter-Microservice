import json
from columbia_student_resource import ColumbiaStudentResource


def t1():

    res = ColumbiaStudentResource.get_by_key('jl5957')
    print(json.dumps(res, indent=2, default=str))


if __name__ == "__main__":
    print("\n\n Use test_rest.py instead of this file. \n\n")
    t1()
