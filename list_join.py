if __name__ == '__main__':
    N = int(input())
    result=[]
    for i in range(N):
        cmd, *parm = input().split()
        if cmd == 'print':
            print(result)
        else:
            exec(f'result.{cmd}({",".join(parm)})')
