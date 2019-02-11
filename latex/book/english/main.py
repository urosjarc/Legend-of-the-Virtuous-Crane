def main():
	newText = []
	with open('answer') as file:
		lines = file.readlines()
		for i, line in enumerate(lines):
			if line.endswith('medskip\n'):
				txt = line.replace('\\medskip\n', '')
				lines = '\\textbf{' + txt + '}\\medskip\n'
				print(lines)


if __name__ == '__main__':
	main()
	print('finish')