def write_file(file_name, ch1, ch2):
    if len(ch2) != len(ch2):
        print("FUCK MOTHERFUCK")

    with open(file_name, 'w') as f:
        for i in range(len(ch1)):
            row = str(ch1[i]) + '\t' +str(ch2[i])+'\r'
            f.write(row)
    return
    
def read_file(file_name):
    ch1 = []
    ch2 = []
    with open(file_name, 'r') as f:
        for row in f:
            row_str = row[:-1]
            row_splt = row_str.split('\t')
            ch1.append(float(row_splt[0]))
            ch2.append(float(row_splt[1]))
    return ch1, ch2 #ch1[offset:], ch2[offset:]

def write_file_noncontact(file_name, signals, center_roi):
    '''The type of signal is dict ({0:[], 1:[], 2:[], 3:[], 4[]})'''
    with open(file_name, 'w') as f:
        for i in range(len(signals[0])):
            row = ''
            for j in range(len(signals)):
                row = row + str(signals[j][i]) + '\t'
            row += str(center_roi[i]) + '\r'
            f.write(row)
    return

def read_file_noncontact(file_name, seg1, seg2):
    sig1 = []
    sig2 = []
    center_sig = []
    with open(file_name, 'r') as f:
        for row in f:
            row_splt = row.split('\t')
            sig1.append(float(row_splt[seg1]))
            sig2.append(float(row_splt[seg2]))
            center_sig.append(float(row_splt[-1]))
    return sig1, sig2, center_sig
