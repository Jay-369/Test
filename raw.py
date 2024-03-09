import re
r= "this is a \n new line"
rw= r"this is \n new line"
#print(r)
#print(rw)

pt = r'\d+'
text="hai 123 heloow 345 bye 678"
match=re.search(pt,text)
if(match):
    print(match.group())

match=re.findall(pt,text)
print(match)

new_text=re.sub(pt,'x',text)
print(new_text)

a="my adhar numer is 1233-4546-3573 and my other number is 0988-5674-8635"

adhar=r'\d{4}-\d{4}-\d{4}'

no=re.search(adhar,a)
if no:
    print(no.group)
no=re.findall(adhar,a)
print(no)


pattern=r'\b[\w\.]+@[\w\.-]+\.\w+\b'

paragraph = "You can reach me at john.doe@gmail.com or jane_smith@gmail.com for any inquiries sreeram.mr@entri.me."


mail_addresses = re.findall(pattern, paragraph)

print(mail_addresses)