def countdown(i):
    """利用递归进行倒计时，当i=1时为基线条件"""

    if i == 1:
        print(i)
        return

    print(i)
    countdown(i-1)

countdown(8)
