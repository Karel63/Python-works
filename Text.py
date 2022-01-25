testTest1 = "I'm loving it."
testTest2 = "\x49\x20\x6d\x20\x6c\x6f\x76\x69\x6e\x67\x20\x69\x74\x2e"
testTest3 = """I'm 
loving it."""
testTest4 = "\tI'm loving it."
testTest5 = "You're loving it.N\b"
testTest6 = 'I\'m loving it.'

print(testTest1)
print(testTest2.upper())
print(testTest3.lower())
print(testTest4.strip())
print(testTest5.replace("You're", "I'm"))
print(testTest6.split(" "))
