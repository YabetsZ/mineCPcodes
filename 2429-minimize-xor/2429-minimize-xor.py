class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_set_bits = num2.bit_count()
        num1_set_bits = num1.bit_count()
        # handle the three cases

        if num1_set_bits == num2_set_bits:
            return num1
        elif num1_set_bits > num2_set_bits:
            rem, until = num1_set_bits - num2_set_bits, -1
            for i in range(num1.bit_length()):
                if num1 & (1<<i) != 0:
                    rem -= 1
                if rem == 0:
                    until = i
                    break
            return num1 & ~(2**(until+1)-1)
        else:
            rem, ptr =  num2_set_bits - num1_set_bits, 0
            while rem > 0:
                if num1 & (1<<ptr) == 0:
                    num1 |= 1<<ptr
                    rem -= 1
                ptr += 1
            return num1
            
        