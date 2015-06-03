# -*- coding: utf-8 -*-

test_list_1=["python", "-", "izm", ".", "com"]
print test_list_1

print "------------------------"

for i in test_list_1:
	print i

# --------------------------------------

print "こんにちは"

test_list_2 = []

test_list_2.append("python")
test_list_2.append("って")
test_list_2.append("難しい")

for i in test_list_2:
	print i.encode("shift_jis")
