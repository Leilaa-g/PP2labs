import re
word1 = """abbc, adbb, abbbbc, abb
a_bbbc, aahHello_b, sdgsSalem
IamaStudent
abbbb, abbbsgd, asd_saa
abbb, ab, b_a, Hello_world
khbkkjJJJbabbs, SalemAlem
sj_snsa, akbb"""

print("Exercise 1")
matches = re.findall(r"a.*?b", word1)
print(matches)

print("Exercise 2")
matches = re.findall(r"ab{2,3}", word1)
print(matches)

print("Exercise 3")
matches = re.findall(r"\b[a-z]+_[a-z]+\b", word1) 
print(matches)

print("Exercise 4")
matches = re.findall(r"[A-Z][a-z]+", word1)
print(matches)

print("Exercise 5")
matches = re.findall(r"a.*b", word1) 
print(matches)


word2 = """abbc_,abb baba
abb__acb_aa
MyNameIsAlmas
WritingPythonCode,ToUpdate"""

print("Exercise 6")
matches = re.sub(r"[., ]", ":", word2)
print(matches)

print("Exercise 7")
matches = re.sub(r"_", "", word2)
print(matches)

print("Exercise 8")
matches = re.findall(r"[A-Z][^A-Z]*", word2)
print(matches)

print("Exercise 9")
matches = re.findall(r"[A-Z][a-z]*", word2)
print(matches)

print("Exercise 10")
matches = re.sub(r"([A-Z])", r"_\1", word2).lower().lstrip("_")  
print(matches)