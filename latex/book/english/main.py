def main():

	count = 0
	with open('answer.tex') as file:
		lines = file.readlines()

		lines = ['\\vspace*{1.2cm}\n'] + lines

		for i, line in enumerate(lines):
			if line.endswith('medskip\n'):
				count += 1

				if count % 14 == 0:
					pagebreak = '\\vfill\\pagebreak\\vspace*{1.2cm}\n'

				else:
					pagebreak = '\n'
				txt = line.replace('\\medskip\n', '')
				lines[i] = '\\textit{' + txt + '}\\medskip' + pagebreak


			elif not line.isspace() and not line.startswith('\\'):
				txt = line.replace('\n', '')
				lines[i] = '\\textbf{' + txt + '}\n'


		with open('answer_new.tex', 'w') as file:
			file.writelines(lines)



if __name__ == '__main__':
	main()
	print('finish')