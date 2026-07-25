class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize an empty stack to track directory names
        stack = []
        
        # Split the path by the slash character
        components = path.split('/')
        
        # Process each segment individually
        for portion in components:
            # Skip empty strings (from consecutive slashes) or current directory markers
            if portion == '' or portion == '.':
                continue
            # Go up one directory level if possible
            elif portion == '..':
                if stack:
                    stack.pop()
            # Push valid directory names onto the stack
            else:
                stack.append(portion)
                
        # Reconstruct the canonical absolute path
        return '/' + '/'.join(stack)
