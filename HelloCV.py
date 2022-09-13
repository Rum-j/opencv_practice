import cv2


def vcheck():
    return "hello, openCV" f"{cv2.__version__}"


if __name__ == "__main__":  # pragma: no cover
    ret = vcheck()
    print(ret)
