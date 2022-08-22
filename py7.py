s=input("Input space seperated sequence of words:")
words=[word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))