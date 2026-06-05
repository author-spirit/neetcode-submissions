class Solution:

    def encode(self, strs: List[str]) -> str:

        # Encode the list of strings to one single stirng
        # convert all ascii characters to code
        # for each string prepare encoded format
        # 1. get the ascii codes
        # 2. combine all the codes by comma separated enclosed within () braces
        # 3. merge all encoded string to one big text separated by comma 

        if len(strs) == 0:
            return ""

        encoded_str = []
        for txt in strs:
            codes = [ord(c) for c in txt]

            # '#len|code|code|code|','#len
            code_txt = "#" + str(len(codes)) + "|"
            for i, code in enumerate(codes):
                code_txt += str(code) + ("|" if i != len(codes) -1 else "")
            encoded_str.append(code_txt)

        return ",".join(encoded_str)

    def decode(self, s: str) -> List[str]:

        # reverse process
        # 1. split all encoded string by comma
        # 2. again split the individual encoded string split by "|"
        # 3. get the ascii character of code and join into one word

        if not s:
            return []

        decoded_list = []
        encoded_list = s.split(",")

        print("endcoded", encoded_list)
        for encoded_txt in encoded_list:
            decoded_txt = ""
            ascii_codes = encoded_txt.split("|")
            length = int(ascii_codes[0].replace("#", ""))
            
            if length > 0:
                for code in ascii_codes[1:]:
                    decoded_txt += chr(int(code))
            
            decoded_list.append(decoded_txt)

        return decoded_list