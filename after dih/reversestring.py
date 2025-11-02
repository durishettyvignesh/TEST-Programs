class py_reverse:
    def reverse_string(self, input_string):
        """
        Reverses the given input string.

        Parameters:
        input_string (str): The string to be reversed.

        Returns:
        str: The reversed string.
        """
        return input_string[::-1]
    
str1 = input("Enter a string to reverse: ")
reverser = py_reverse()
reversed_str = reverser.reverse_string(str1)
print("Reversed string:", reversed_str)
