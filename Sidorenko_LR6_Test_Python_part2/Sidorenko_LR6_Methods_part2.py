
def cut_info(cut):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        new_cut = str(cut)
        if len(new_cut) == 3 and new_cut[1] == "-":
            if new_cut[0] in alphabet and new_cut[2] in alphabet:
                return True
        return False
    except ValueError:
        return False

def one_or_more(cut):
    if cut_info(cut):
        new_cut = str(cut)
        if new_cut[0] == new_cut[2]:
            return True
    return False


def a_to_z(cut):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    flag = False
    printout = ''
    if cut_info(cut):
        new_cut = str(cut)
        if one_or_more(new_cut):
            print(new_cut[0])
            return new_cut[0]
        else:
            for i in alphabet:
                if new_cut[0] == i:
                    flag = True
                elif new_cut[2] == i:
                    flag = False
                    printout += i
                if flag:
                    printout += i
            print(printout)
            return printout
    return None
