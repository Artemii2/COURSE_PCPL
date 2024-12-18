import json
from cm_timer import cm_timer_1
from field import field
from gen_random import gen_random
from print_result import print_result

path = "C:\ML course\ML-course\pclm\lab3\lab_python_fp\data_light.json"

with open(path, encoding="utf-8") as f:
    data = json.load(f)

@print_result
def f1(data):
    result=sorted(field(data,"job-name"))
    return result

@print_result
def f2(f1_result):
    return list(filter(lambda job: job.startswith("программист"), f1_result))

@print_result
def f3(f2_result):
    return list(map(lambda job: f"{job} с опытом Python", f2_result))

@print_result
def f4(f3_result):
    salaries = gen_random(len(f3_result), 100000, 200000)
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(f3_result, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))