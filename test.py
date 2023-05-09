def test() -> tuple[bool, int, str]:
    return (True, 1, "ok")


if __name__ == "__main__":
    flag, num, msg = test()

    print(flag)
    print(num)
    print(msg)
