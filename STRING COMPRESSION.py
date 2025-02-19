class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0  # Where to write the compressed result
        i = 0  # Pointer to read characters
        
        while i < len(chars):
            char = chars[i]
            count = 0

            # Count occurrences of chars[i]
            while i < len(chars) and chars[i] == char:
                count += 1
                i += 1
            
            # Write character
            chars[write] = char
            write += 1

            # Write count if more than 1
            if count > 1:
                for digit in str(count):  # Convert count to string and write each digit
                    chars[write] = digit
                    write += 1
        
        return write  # The new length of chars
