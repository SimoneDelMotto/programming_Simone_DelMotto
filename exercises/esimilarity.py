def scoring(seq1, seq2):
	score=0
	for i in range(len(seq1)):
		if seq1[i] == seq2[i]:
			score += 1
		else:
			score -= 1
	return score

seq1= input("Insert first sequence: ")
seq2= input("Insert second sequence: ")
if len(seq1) != len(seq2):
	print("The sequences have not the same lenght")
else:
	print(scoring(seq1, seq2))
