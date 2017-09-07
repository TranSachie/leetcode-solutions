a = [1,3,2]

def nextPermutation(a):
	pivot=len(a)-1
	while pivot>0 and a[pivot]<a[pivot-1]:
		pivot-=1
	if pivot==0:
		print "This is the max permutation"
		return
	left_target = pivot-1
	right_target = len(a)-1
	while right_target>=pivot and a[right_target]<a[left_target]:
		right_target-=1
	right_target_val = a[right_target]
	print a, a[left_target], a[pivot], a[right_target]
	for i in range(right_target+1, len(a)):
		a[i-1] = a[i]
	a[len(a)-1] = a[left_target]
	a[left_target] = right_target_val
	print a






nextPermutation(a)