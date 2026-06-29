def temp_conversion(temp,unit): 
    if unit == 'C':
        return temp * 9/5 + 32 
    elif unit == 'F':
        return (temp-32) * 5/9
    else:
        return None
    
print(temp_conversion(27, 'C')) 
print(temp_conversion(66, 'F'))  
