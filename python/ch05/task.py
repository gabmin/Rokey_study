# nums = [10, 20, 30]
#
# for i in nums:
#     print(i)

# price_list = [100, 200, 300]
#
# for price in price_list:
#     print(price + 10)


# animals_list = ["dog", "cat", "parrot"]
#
# for animal in animals_list:
#     print(animal, len(animal))


# word_list = ["가", "나", "다", "라"]
#
# for word in range(1, len(word_list)):
#     print(word_list[word])


# number_list = [3, -20, -3, 44]
#
# for number in number_list:
#     if number < 0:
#         print(number)


# for year in range(2002, 2051, 4):
#     print(year)


# num = 0
# total = 0
#
# while num <= 100:
#     total += num
#     num += 1
#
# print(total)


odd_list = []
even_list = []

for num in range(1, 31):
    if num % 2 != 0:
        odd_list.append(num)
    else:
        even_list.append(num)

print(odd_list)
print(even_list)
