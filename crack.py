import hashlib
import quit

hash_pass = input("Enter an md5 hash > ")

wordlist = input("Enter your file name > ")

try:
	pass_file = open(wordlist, "r")
except:
	print("No file found")
	quit()
	
for word in pass_file:

	enc_word = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()
	
	
	
	print(word)
	print(digest)
	print(pass_hash)
	
	if digest == pass_hash:
	    print("Password found")
	    print("Password is" + word)
	    flag = 1
	    break
	    
if flag == 0:
    print("Password/paraphase is not in the list")
	
