# Define function 

def string_with_scrub(line): 

     

    # Separate main string and characters needing to be scrubbed using comma 

    sep = line.split(',') 

     

    # Return original line if it doesn't contain a comma 

    if len(sep) != 2: 

        return line.strip()   

     

    # define main string and characters to scrub 

    main = sep[0].strip()   

    scrub = sep[1].strip()   

  

    # Iteratively replace scrub characters in main string with blanks to create new string 

    for char in scrub: 

        main = main.replace(char, "")   

  

    # This will return without any leading/trailing whitespace 

    return main.strip() 

  

# Test function 

    # Test 1

test1 = string_with_scrub("how are you, abc") 

print(test1)  

  

    # Test 2

test2 = string_with_scrub("hello world, def") 

print(test2) 
