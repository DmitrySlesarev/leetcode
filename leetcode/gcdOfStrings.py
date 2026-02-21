class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """That's my correct solution"""

        for s in str1, str2:
            if not isinstance(s, str):
                raise TypeError(f"The param {s=} must be of 'str' type")
            if s.isspace():  # or: s.strip() == " ":
                raise ValueError(f"The param {s=} must be of non-zero length")

        str1, str2 = str1.strip(), str2.strip()

        def get_gcd(bigger_text, smaller_text):

            gcd = list(smaller_text)

            while gcd:

                btm = len(bigger_text) // len(gcd)
                if "".join(gcd) * btm == bigger_text:

                    stm = len(smaller_text) // len(gcd)
                    if "".join(gcd) * stm == smaller_text:
                        break

                gcd.pop()

            return "".join(gcd)

        try:
            if len(str1) > len(str2):
                return get_gcd(str1, str2)
            else:
                return get_gcd(str2, str1)

        except Exception as e:
            print(f"Something went wrong: {e}")

        return ""

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        """ By Deepseek """
        # Mathematical insight: If str1 + str2 == str2 + str1, then a GCD exists
        if str1 + str2 != str2 + str1:
            return ""

        # Find the GCD of the lengths
        from math import gcd
        gcd_length = gcd(len(str1), len(str2))

        # Return the substring that is the GCD
        return str1[:gcd_length]

    def gcdOfStrings3(self, str1: str, str2: str) -> str:
        """ Also, Deepseek"""
        # Input validation (though not required by LeetCode)
        for s in [str1, str2]:
            if not isinstance(s, str):
                raise TypeError(f"The parameter must be of 'str' type")
            if not s:  # Empty string check
                raise ValueError(f"String should be non-zero length")

        str1, str2 = str1.strip(), str2.strip()

        # Check if a GCD exists
        if str1 + str2 != str2 + str1:
            return ""

        # Calculate GCD of lengths
        len1, len2 = len(str1), len(str2)

        # Find GCD using Euclidean algorithm
        while len2:
            len1, len2 = len2, len1 % len2

        # Return the GCD string
        return str1[:len1]


if __name__ == "__main__":
    c = Solution()
    print(f"{c.gcdOfStrings("ABCABC", "ABC")=}")
    print(f"{c.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")=}")

    print(f"{c.gcdOfStrings2("ABCABC", "ABC")=}")
    print(f"{c.gcdOfStrings2("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")=}")

    print(f"{c.gcdOfStrings3("ABCABC", "ABC")=}")
    print(f"{c.gcdOfStrings3("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")=}")



