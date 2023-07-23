import re

text = "my name is steve. is this on steve? yes it is steve."
text1 = "steve"
# srch = "steve" in text
# print(srch)

a = re.search("steve", text)
# print(a.start())
# print(a.end())
# print(a.group())

pattern = re.compile("steve")
pattern2 = re.compile("my name")

b = pattern.search(text)
c = pattern.findall(text)
d = pattern.fullmatch(text1)
e = pattern2.match(text)
print(b.group())
print(c)
print(d)
print(e)
# https://regex101.com/