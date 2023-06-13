from prefect import flow, task

@task
def suma_1(x: int) -> int:
    return x + 1

@task
def suma_2(x: int) -> int:
    return 4 + x

@task
def suma_3(x: int) -> int:
    return 4 + x

@task
def suma_4(x: int) -> int:
    return 10 + x

@flow(name = "suma test")
def prefect_sum_flow():
    x = 1
    r1 = suma_1(x)
    r2 = suma_2(r1)
    r3 = suma_3(r2)
    r4 = suma_4(r3)
    resultado = r4
    return print(resultado)

if __name__ == '__main__':
    prefect_sum_flow()