import numpy as np
import sys

with open(sys.argv[1], 'r') as f:

    line_one = f.readline().split()
    num_features = line_one[0]
    a_size = line_one[1]
    b_size = line_one[2]
    c_size = line_one[3]
    feature_a_total = 0
    feature_b_total = 0
    feature_c_total = 0
    for i in range(int(a_size)):
        line = f.readline().split()
        feature_a_total += float(line[0])
        feature_b_total += float(line[1])
        feature_c_total += float(line[2])

    feature_a_avg = feature_a_total/float(a_size)
    feature_b_avg = feature_b_total/float(a_size)
    feature_c_avg = feature_c_total/float(a_size)
    class_a_avg = [feature_a_avg, feature_b_avg, feature_c_avg]
    print "-----------------------------------------------------"
    print "Class A average:",class_a_avg


    feature_a_total = 0
    feature_b_total = 0
    feature_c_total = 0
    for i in range(int(a_size), (int(a_size)+int(b_size))):
        line = f.readline().split()
        feature_a_total += float(line[0])
        feature_b_total += float(line[1])
        feature_c_total += float(line[2])

    feature_a_avg = feature_a_total/float(b_size)
    feature_b_avg = feature_b_total/float(b_size)
    feature_c_avg = feature_c_total/float(b_size)
    class_b_avg = [feature_a_avg, feature_b_avg, feature_c_avg]
    print "-----------------------------------------------------"
    print "Class B average:",class_b_avg

    feature_a_total = 0
    feature_b_total = 0
    feature_c_total = 0
    for i in range((int(a_size)+int(b_size)), (int(a_size)+int(b_size)+int(c_size))):
        line = f.readline().split()
        feature_a_total += float(line[0])
        feature_b_total += float(line[1])
        feature_c_total += float(line[2])

    feature_a_avg = feature_a_total/float(c_size)
    feature_b_avg = feature_b_total/float(c_size)
    feature_c_avg = feature_c_total/float(c_size)
    class_c_avg = [feature_a_avg, feature_b_avg, feature_c_avg]
    print "-----------------------------------------------------"
    print "Class C average:",class_c_avg
    print "-----------------------------------------------------"

    vector_ab = [class_b_avg[0] - class_a_avg[0], class_b_avg[1] - class_a_avg[1], class_b_avg[2] - class_a_avg[2]]
    # print "vector a->b:", vector_ab
    vector_ac = [class_c_avg[0] - class_a_avg[0], class_c_avg[1] - class_a_avg[1], class_c_avg[2] - class_a_avg[2]]
    vector_bc =  [class_c_avg[0] - class_b_avg[0], class_c_avg[1] - class_b_avg[1], class_c_avg[2] - class_b_avg[2]]
    # print "vector a->c:", vector_ac
    # print "vector b->c:", vector_bc

    # mid_ab = [(class_a_avg[0]+class_b_avg[0])/2, (class_a_avg[1]+class_b_avg[1])/2, (class_a_avg[2]+class_b_avg[2])/2]
    # mid_ac = [(class_a_avg[0]+class_c_avg[0])/2, (class_a_avg[1]+class_c_avg[1])/2, (class_a_avg[2]+class_c_avg[2])/2]
    # mid_bc = [(class_c_avg[0]+class_b_avg[0])/2, (class_c_avg[1]+class_b_avg[1])/2, (class_c_avg[2]+class_b_avg[2])/2]
    #
    # dis_ab = np.dot(vector_ab, mid_ab)
    # dis_ac = np.dot(vector_ac, mid_ac)
    # dis_bc = np.dot(vector_bc, mid_bc)

    # print "Discriminants:", dis_ab, dis_ac, dis_bc

correct_guess = 0
incorrect_guess = 0
total = 0


'''
---------
Class A
---------
Guessed Class A: Increase A's TP, Increase B/C TN
Guessed Class B (INCORRECT): Increase A's FN, Increase B's FP, Increase C's TN
Guessed Class C (INCORRECT): Increase A's FN, Increase C's FP, Increase B's TN

---------
Class B
---------
Guessed Class A (INCORRECT): Increase B's FN, Increase A's FP, Increase C's TN
Guessed Class B: Increase B's TP, Increase A/B TN
Guessed Class C (INCORRECT): Increase B's FN, Increase C's FP, Increase B's TN

---------
Class C
---------
Guessed Class A (INCORRECT): Increase C's FN, Increase A's FP, Increase B's TN
Guessed Class B (INCORRECT): Increase C's FN, Increase B's FP, Increase C's TN
Guessed Class C: Increase C's TP, Increase B/C TN

'''
# TP, TN, FP, FN
a_stats = [0, 0, 0, 0]
b_stats = [0, 0, 0, 0]
c_stats = [0, 0, 0, 0]



with open(sys.argv[2], 'r') as f:
    line_one = f.readline().split()

    for i in range(int(line_one[1])):
        estimated = "A"
        line = f.readline().split()
        print i, line, "A"
        diff_a = [class_a_avg[0]-float(line[0]), class_a_avg[1]-float(line[1]),class_a_avg[2]-float(line[2])]
        diff_a = np.linalg.norm(diff_a)

        diff_b = [class_b_avg[0]-float(line[0]), class_b_avg[1]-float(line[1]),class_b_avg[2]-float(line[2])]
        diff_b = np.linalg.norm(diff_b)

        diff_c = [class_c_avg[0]-float(line[0]), class_c_avg[1]-float(line[1]),class_c_avg[2]-float(line[2])]
        diff_c = np.linalg.norm(diff_c)

        differences = [diff_a, diff_b, diff_c]
        result = np.amin(differences)
        # print differences
        # print result
        if(result == diff_a):
            print 'Given Class A data, Predicted: A - TRUE'
            correct_guess += 1
            a_stats[0] += 1
            b_stats[1] += 1
            c_stats[1] += 1
        elif(result == diff_b):
            print 'Predicted: B - FALSE'
            incorrect_guess += 1
            a_stats[3] += 1
            b_stats[2] += 1
            c_stats[1] += 1
        elif(result == diff_c):
            print 'Predicted: C - FALSE'
            incorrect_guess += 1
            a_stats[3] += 1
            b_stats[1] += 1
            c_stats[2] += 1

    second_range = int(line_one[1]) + int(line_one[2])

    for i in range(int(line_one[1]), second_range):
        estimated = "B"
        line = f.readline().split()
        print i, line
        diff_a = [class_a_avg[0]-float(line[0]), class_a_avg[1]-float(line[1]),class_a_avg[2]-float(line[2])]
        diff_a = np.linalg.norm(diff_a)

        diff_b = [class_b_avg[0]-float(line[0]), class_b_avg[1]-float(line[1]),class_b_avg[2]-float(line[2])]
        diff_b = np.linalg.norm(diff_b)

        diff_c = [class_c_avg[0]-float(line[0]), class_c_avg[1]-float(line[1]),class_c_avg[2]-float(line[2])]
        diff_c = np.linalg.norm(diff_c)

        differences = [diff_a, diff_b, diff_c]
        result = np.amin(differences)
        # print differences
        # print result
        if(result == diff_a):
            print 'Given Class B data, Predicted: A - FALSE'
            incorrect_guess += 1
            a_stats[2] += 1
            b_stats[3] += 1
            c_stats[1] += 1
        elif(result == diff_b):
            print 'Given Class B data, Predicted: B - TRUE'
            correct_guess += 1
            a_stats[1] += 1
            b_stats[0] += 1
            c_stats[1] += 1
        elif(result == diff_c):
            print 'Given Class B data, Predicted: C - FALSE'
            incorrect_guess += 1
            a_stats[1] += 1
            b_stats[3] += 1
            c_stats[2] += 1

    for i in range(second_range, 75):
        estimated = "C"
        line = f.readline().split()
        print i, line
        diff_a = [class_a_avg[0]-float(line[0]), class_a_avg[1]-float(line[1]),class_a_avg[2]-float(line[2])]
        diff_a = np.linalg.norm(diff_a)

        diff_b = [class_b_avg[0]-float(line[0]), class_b_avg[1]-float(line[1]),class_b_avg[2]-float(line[2])]
        diff_b = np.linalg.norm(diff_b)

        diff_c = [class_c_avg[0]-float(line[0]), class_c_avg[1]-float(line[1]),class_c_avg[2]-float(line[2])]
        diff_c = np.linalg.norm(diff_c)

        differences = [diff_a, diff_b, diff_c]
        result = np.amin(differences)
        # print differences
        # print result
        if(result == diff_a):
            print 'Given Class C data, Predicted: A - FALSE'
            incorrect_guess += 1
            a_stats[2] += 1
            b_stats[1] += 1
            c_stats[3] += 1
        elif(result == diff_b):
            print 'Given Class C data, Predicted: B - FALSE'
            incorrect_guess += 1
            a_stats[1] += 1
            b_stats[2] += 1
            c_stats[3] += 1
        elif(result == diff_c):
            print 'Given Class C data, Predicted: C - TRUE'
            correct_guess += 1
            a_stats[1] += 1
            b_stats[1] += 1
            c_stats[0] += 1

        total = i + 1

print "--------------------------------------------------------------------"
print "Summary"
print "--------------------------------------------------------------------"
print "Total Guesses:", total
print "Correct Guesses:", correct_guess
print "Incorrect Guesses:", incorrect_guess

print a_stats
print b_stats
print c_stats

TPR_a = a_stats[0]/float(line_one[1])
TPR_b = b_stats[0]/float(line_one[1])
TPR_c = c_stats[0]/float(line_one[3])

FPR_a = a_stats[2]/float(float(line_one[2])+float(line_one[3]))
FPR_b = b_stats[2]/float(float(line_one[1])+float(line_one[3]))
FPR_c = c_stats[2]/float(float(line_one[1])+float(line_one[2]))

error_a = float(a_stats[2]+a_stats[3])/float(float(line_one[1])+float(line_one[2])+float(line_one[3]))
error_b = float(b_stats[2]+b_stats[3])/float(float(line_one[1])+float(line_one[2])+float(line_one[3]))
error_c = float(c_stats[2]+c_stats[3])/float(float(line_one[1])+float(line_one[2])+float(line_one[3]))

# dividie by tp + fp [0] + [2]
precision_a = a_stats[0]/float(a_stats[0]+a_stats[2])
precision_b = b_stats[0]/float(b_stats[0]+b_stats[2])
precision_c = c_stats[0]/float(c_stats[0]+c_stats[2])

TPR_avg = (TPR_a+TPR_b+TPR_c)/float(line_one[0])
FPR_avg = (FPR_a+FPR_b+FPR_c)/float(line_one[0])
error_avg = (error_a+error_b+error_c)/float(line_one[0])
precision_avg = (precision_a+precision_b+precision_c)/3

print "TPR AVG:", TPR_avg
print "FPR_avg:", FPR_avg
print "Error Avg", error_avg
print "Precision avg", precision_avg
