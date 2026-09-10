class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            # if len(s) > 9:
            encoded_str += str(len(s)) + "#" + s
            # else:
            #     encoded_str += "#0" + str(len(s)) + s


        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i 

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length

            res.append(s[i:j])

            i = j

        return res

        # chars_left = 0
        # curr_word = ""

        # i = 1

        # # for i in range(1, len(s)):
        # while i < len(s):
        #     if i < len(s) - 1 and s[i - 1] == "#" and s[i].isdigit() and s[i+1]:
        #         chars_left = (int(s[i]) * 10) + int(s[i+1])
        #         j = 2

        #         while chars_left > 0:
        #             curr_word += s[i + j]
        #             chars_left -= 1
        #             j += 1

        #         decoded_list.append(curr_word)
        #         curr_word = ""
        #         i += j
        #     else:
        #         i += 1

        # return decoded_list



        
