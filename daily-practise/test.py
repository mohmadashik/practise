input=["abc(rtyh(dfgh)gghj(sdfgh)iuytre)", "adfgff)dfgh(dfghj)(dfghj"]
for word in input:
	stk = []
	result = []
	balanced = True
	for char in word:
		if char =='(':
			# print(char)
			stk.append(char)
		elif char == ')':
			print(stk)
			if len(stk)>0 and stk[-1] == '(':
				stk.remove('(')
			else	:
				print(stk)

				balanced = False
				result.append(None)
				break

	word.replace('(','')		
	word.replace(')','')		
	result.append(word)
print(result)
