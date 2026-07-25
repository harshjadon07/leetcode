class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        current_line = []
        current_length = 0  # Combined length of words in current_line without spaces
        
        for word in words:
            # Check if adding this word (plus a mandatory 1-space separator) exceeds maxWidth
            if current_length + len(current_line) + len(word) > maxWidth:
                # Time to justify the completed line
                extra_spaces = maxWidth - current_length
                
                # Case 1: Line contains only 1 word
                if len(current_line) == 1:
                    res.append(current_line[0] + " " * extra_spaces)
                else:
                    # Case 2: Line contains multiple words (fully justify)
                    gaps = len(current_line) - 1
                    base_spaces = extra_spaces // gaps
                    remainder_spaces = extra_spaces % gaps
                    
                    line_str = ""
                    for i in range(gaps):
                        line_str += current_line[i]
                        # Give an extra remainder space to the leftmost slots
                        space_to_add = base_spaces + (1 if i < remainder_spaces else 0)
                        line_str += " " * space_to_add
                    line_str += current_line[-1]  # Append the last word
                    res.append(line_str)
                
                # Reset for the next line
                current_line = []
                current_length = 0
            
            current_line.append(word)
            current_length += len(word)
            
        # Case 3: Handle the very last line (must be left-justified)
        last_line_str = " ".join(current_line)
        trailing_spaces = maxWidth - len(last_line_str)
        res.append(last_line_str + " " * trailing_spaces)
        
        return res
