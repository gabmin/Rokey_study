import re

p = re.compile("[ab]")
print(p.match("a"))
print(p.match("before"))
print(p.match("dude"))

p = re.compile("[0-9]")
print(p.match("5"))

p = re.compile("[^0-9]")
print(p.match("5"))

p = re.compile(r"[\^0-9]")
print(p.match("^"))

p = re.compile(r"\d")
print(p.match("5"))

p = re.compile(r"\s")
print(p.match("\n"))

p = re.compile("a.b")
print(p.match("abb"))

p = re.compile("ca*t")
print(p.match("caaaaat"))

p = re.compile("ca+t")
print(p.match("ct"))

p = re.compile("ca{2}t")
print(p.match("caat"))

print("---------------")

p = re.compile("^hello")
print(p.match("hello world"))
print(p.match(" hello world"))
print(p.match("\nhello world"))
print(p.match("dello world"))

print("---------------")

p = re.compile("world$")
print(p.match("hello world"))
print(p.search("hello world"))
print(p.match("hello world!"))
print(p.match("hello world\n"))
print(p.match("hello world$"))
