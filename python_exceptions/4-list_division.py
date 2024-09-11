#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try;
            res.append(my_list_1[i], my_list_2[i])
        except IndexError:
            print()
        except ZeroDivisionError:
            print()
        except TypeError:
            print()
        finally:
            res.append(0)
    return res
