class BaseConversion:
    def __init__(self, base, value):
        self.base = base
        self.value = value

    def to_decimal(self):
        coefficient_list = []
        digit_coefficients = []
        digit_powers = range(len(self.value))
        for power in digit_powers:
            coefficient_val = self.base ** power
            coefficient_list.append(coefficient_val)
        digit_val = []
        for i in coefficient_list[::-1]:
            digit_coefficients.append(i)
        for i in range(len(self.value)):
            val = digit_coefficients[i] * self.value[i]
            digit_val.append(val)

        decimal_val = sum(digit_val)
        return decimal_val
    
    def from_decimal(self):
        division_list = []
        remainder_list = []
        hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

        first_div = self.value // self.base
        division_list.append(first_div)
        first_mod = self.value % self.base
        remainder_list.append(first_mod)
        div = first_div
        while div > 0:  # Loop keeps dividing until the quotient is 0
            div = division_list[-1] // self.base
            mod = division_list[-1] % self.base
            division_list.append(div)
            remainder_list.append(mod)

        mod_list = remainder_list[::-1]

        for i in range(len(mod_list)):
            if mod_list[i] >= 10:  # Checks if there is a two digit remainder in the modulo list
                replace_remainder = hex_dict[mod_list[i]]
                mod_list[i] = replace_remainder
                result_val = ''.join([str(values) for values in mod_list])
                return result_val
            else:
                result_val = ''.join([str(values) for values in mod_list])
                return result_val

    def hex_to_decimal(self):
        hex_conversion = []
        hex_letters = ['A', 'B', 'C', 'D', 'E', 'F']
        hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

        if self.value in hex_letters:  # This returns the result if the user input was only a letter (A-F)
            result = hex_dict[self.value]
            return result
        else:
            val_list = [i for i in str(self.value)]  # [1, A]
            for i in range(len(val_list)):
                if val_list[i] in hex_letters:
                    hex_val = hex_dict[val_list[i]]
                    val_list[i] = hex_val

            placeholder_val = list(map(int, val_list))
            rev = reversed(placeholder_val)
            new_val_list = []
            for r in rev:
                new_val_list.append(r)
            hex_result = []
            for i in range(len(new_val_list)):
                hex_val = self.base ** i
                hex_conversion.append(hex_val)
                temp = new_val_list[i] * hex_conversion[i]
                hex_result.append(temp)

            result = sum(hex_result)
            return result
