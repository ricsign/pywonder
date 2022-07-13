import re


def extract_names_from_file(fname, tag_class="_aaeq"):
    f = open(fname, "r+")
    raw_str = f.read()
    ret = []

    for location in re.finditer(tag_class, raw_str):
        location = location.start()
        location += len(tag_class) + 2  # add ">
        cur_name = ""
        while location < len(raw_str) and raw_str[location] != "<":
            cur_name += raw_str[location]
            location += 1
        ret.append(cur_name)

    return ret


def elems_in_arr1_notin_arr2(arr1, arr2):
    ret = []
    for elem in arr1:
        if elem in arr2:
            continue
        ret.append(elem)
    return ret


if __name__ == "__main__":
    followers_names = extract_names_from_file("../../followers.txt")
    following_names = extract_names_from_file("../../following.txt")

    ppl_not_following_back = elems_in_arr1_notin_arr2(following_names, followers_names)
    ppl_i_dont_follow_back = elems_in_arr1_notin_arr2(followers_names, following_names)

    print("People not following back you are: ")
    for i in ppl_not_following_back:
        print(i, end="; ")
    print("")
    print("People you don't back you are: ")
    for i in ppl_i_dont_follow_back:
        print(i, end="; ")
