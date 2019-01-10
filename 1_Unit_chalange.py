

def adding_report(all_or_total):
	total = 0
	items = 'Items \n'
	while True:
		ux = input('Input an integer to add to the total or "Q" to quit ')
		if ux.isnumeric():
			ux = int(ux)
			total = total + ux
			if all_or_total.lower() == 'a':
				ux = str(ux)
				items = items + ux + '\n'
			else:
				pass
		elif ux.lower().startswith('q'):
			if all_or_total.lower() == 'a':
				print(items)
				total = str(total)
				print('\nTotal\n' + total + '\n')
				break
			else:
				total = str(total)
				print('\nTotal\n' + total + '\n')
				break
		else:
			print("Enter an integer or \"Q\":")
adding_report('a')
adding_report("T")



