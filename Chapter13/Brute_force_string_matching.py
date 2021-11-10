def brute_force(text, pattern):
    l1 = len(text)      # The length of the text string
    l2 = len(pattern)   # The length of the pattern 
    i = 0
    j = 0               # looping variables are set to 0
    flag = False        # If the pattern doesn't appear at all, then set this to false and execute the last if statement
    while i < l1:         # iterating from the 0th index of text
        j = 0
        count = 0    
        # Count stores the length upto which the pattern and the text have matched
        while j < l2:
            if i+j < l1 and text[i+j] == pattern[j]:  
        # statement to check if a match has occurred or not
                count += 1     # Count is incremented if a character is matched 
            j += 1
        if count == l2:   # it shows a matching of pattern in the text 
                print("\nPattern occurs at index", i) 
                # print the starting index of the successful match
                flag = True 
                # flag is True as we wish to continue looking for more matching of pattern in the text. 
        i += 1
    if not flag: 
        # If the pattern doesn't occurs at all, means no match of pattern in the text string
        print('\nPattern is not at all present in the array')


brute_force('acbcabccababcaacbcac','acbcac')         # function call
