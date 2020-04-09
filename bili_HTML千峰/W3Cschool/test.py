import time, configparser

conf = configparser.ConfigParser()
path = r'D:\LATTE_Project_3\core\test_cases\section4\NB_hdd_ssd_test_plan\cookie.ini'
conf.read(path, encoding='utf-8')


def get_ini(values):
    """

    Args:
        values: 传入ini字符

    Returns:
    Examples:
         get_ini(values = "password")
    """
    conf = configparser.ConfigParser()
    conf.read(path)
    return conf.get("section1", values)


def set_ini(name, values):
    """

    Args:
        name: 传入ini变量值
        values: 修改ini变量值

    Returns:
    Examples:
        set_ini(name = 12345678,values = 123456789)
    """
    conf = configparser.ConfigParser()
    conf.read(path)
    conf.set("section1", name, values)
    conf.write(open(path, 'w+'))
print(1)