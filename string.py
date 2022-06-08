def stringCompression(strs):

    freq = dict()

    for i in strs:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1


    stack = []

    for k, v in freq.items():
        stack.append(str(k))
        stack.append(str(v))

    return "".join(stack)

test1 = "aaabbbcc"
tes2 = "abb"

print(stringCompression(test1))