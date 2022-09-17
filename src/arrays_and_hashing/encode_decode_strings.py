# Josue Lopez
# Sep 16, 2022
# https://www.lintcode.com/problem/659/

class Solution:

	"""	
	@params: takes a list of strings
	@returns: encodes list of strings into a single string
	"""
	def encode(self, strs: [str]) -> str:
		res = ""
		for i in strs:
			len_of_str = len(i)
			res += str(len_of_str) + "#" + i

		return res


	"""
	Given an encoded string, this algorithm reverses it
	to the original list of strings. Message
	"""
	def decode(self, encoded_s:str) -> [str]:
		# hold a returning list, 
		# but also index ptr starting @ 0
		decoded_strs, i = [], 0

		while i < len(encoded_s):
			#  first read how many chars the leading integer takes
			j = i
			while encoded_s[j] != "#":
				j += 1

			start_of_word, length = j+1, int(encoded_s[i:j])

			word = encoded_s[ start_of_word : start_of_word+length ]
			decoded_strs.append(word)

			## update i to MOVE to index j+1+length
			i = start_of_word + length

		return decoded_strs


if __name__ == "__main__":
	s = Solution()

	message = ['i', 'love', 'mcdonalds', 'fry', 'alooooot']
	print(message); print()

	encoded_s = s.encode(message)
	print(encoded_s); print()
	assert encoded_s == "1#i4#love9#mcdonalds3#fry8#alooooot"

	decoded_strs = s.decode(encoded_s)
	print(decoded_strs); print()
	assert decoded_strs == message
