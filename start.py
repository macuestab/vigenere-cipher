import vigenereCipher    

numbers = [str(i) for i in range(0,10)]
checker_flag = True

# Run the code
print("What do you want with your message, encode it or decode it?")
codeOrDecode = input("Type \'encode\' or \'decode\': ").lower()
if codeOrDecode == "encode" or codeOrDecode == "decode":
    if codeOrDecode == "encode":
        message = input("Type your message to be encoded: ").lower()
        while checker_flag:
            keyword = input("What keyword do you want to give?: ").lower()
            total_numbers_in_keyword = 0
            for letter in keyword:
                total_numbers_in_keyword += numbers.count(letter) 
            if total_numbers_in_keyword == 0:
                checker_flag = False
            else:
                print("Provide a keyword without any number!")
        print("Encoding message.....")
        print(vigenereCipher.vigenere_coder(message, keyword))
    else:
        message = input("Type your message to be decoded: ").lower()
        while checker_flag:
            keyword = input("Type the keyword to decode the message: ").lower()
            total_numbers_in_keyword = 0
            for letter in keyword:
                total_numbers_in_keyword += numbers.count(letter) 
            if total_numbers_in_keyword == 0:
                checker_flag = False
            else:
                print("Provide a keyword without any number!")
        print("Decoding message.....")
        print(vigenereCipher.vigenere_decoder(message, keyword))
else:
    raise Exception("Please, choose one option between \'encode\' or \'decode\'.")