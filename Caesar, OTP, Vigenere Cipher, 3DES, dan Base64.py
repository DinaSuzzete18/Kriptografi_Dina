import base64


def xor(s1, s2):
    xor_result = []

    for i in range(min(len(s1), len(s2))):
        xor_result.append(int(s1[i]) ^ int(s2[i]))  # xor

    return xor_result


hexa_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
    'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
}
hexa_to_char = {
    '61': 'a', '62': 'b', '63': 'c', '64': 'd', '65': 'e', '66': 'f', '67': 'g', '68': 'h', '69': 'i',
    '6a': 'j', '6b': 'k', '6c': 'l', '6d': 'm', '6e': 'n', '6f': 'o', '70': 'p', '71': 'q', '72': 'r', '73': 's',
    '74': 't', '75': 'u', '76': 'v', '77': 'w', '78': 'x', '79': 'y', '7a': 'z', '41': 'A', '42': 'B', '43': 'C',
    '44': 'D', '45': 'E', '46': 'F', '47': 'G', '48': 'H', '49': 'I', '4a': 'J', '4b': 'K', '4c': 'L', '4d': 'M',
    '4e': 'N',
    '4f': 'O', '50': 'P', '51': 'Q', '52': 'R', '53': 'S', '54': 'T', '55': 'U', '56': 'V', '57': 'W', '58': 'X',
    '59': 'Y', '5a': 'Z'
}
Sboxes = [
    {
        '000000': '1110', '000010': '0100', '000100': '1101', '000110': '0001', '001000': '0010', '001010': '1111',
        '001100': '1011', '001110': '1000',
        '010000': '0011', '010010': '1010', '010100': '0110', '010110': '1100', '011000': '0101', '011010': '1001',
        '011100': '0000', '011110': '0111',
        '000001': '0000', '000011': '1111', '000101': '0111', '000111': '0100', '001001': '1110', '001011': '0010',
        '001101': '1101', '001111': '0001',
        '010001': '1010', '010011': '0110', '010101': '1100', '010111': '1011', '011001': '1001', '011011': '0101',
        '011101': '0011', '011111': '1000',
        '100000': '0100', '100010': '0001', '100100': '1110', '100110': '1000', '101000': '1101', '101010': '0110',
        '101100': '0010', '101110': '1011',
        '110000': '1111', '110010': '1100', '110100': '1001', '110110': '0111', '111000': '0011', '111010': '1010',
        '111100': '0101', '111110': '0000',
        '100001': '1111', '100011': '1100', '100101': '1000', '100111': '0010', '101001': '0100', '101011': '1001',
        '101101': '0001', '101111': '0111',
        '110001': '0101', '110011': '1011', '110101': '0011', '110111': '1110', '111001': '1010', '111011': '0000',
        '111101': '0110', '111111': '1101'

    },
    {

        '000000': '1111', '000010': '0001', '000100': '1000', '000110': '1110', '001000': '0110', '001010': '1011',
        '001100': '0011', '001110': '0100',
        '010000': '1001', '010010': '0111', '010100': '0010', '010110': '1101', '011000': '1100', '011010': '0000',
        '011100': '0101', '011110': '1010',
        '000001': '0011', '000011': '1101', '000101': '0100', '000111': '0111', '001001': '1111', '001011': '0010',
        '001101': '1000', '001111': '1110',
        '010001': '1100', '010011': '0000', '010101': '0001', '010111': '1010', '011001': '0110', '011011': '1001',
        '011101': '1011', '011111': '0101',
        '100000': '0000', '100010': '1110', '100100': '0111', '100110': '1011', '101000': '1010', '101010': '0100',
        '101100': '1101', '101110': '0001',
        '110000': '0101', '110010': '1000', '110100': '1100', '110110': '0110', '111000': '1001', '111010': '0011',
        '111100': '0010', '111110': '1111',
        '100001': '1101', '100011': '1000', '100101': '1010', '100111': '0001', '101001': '0011', '101011': '1111',
        '101101': '0100', '101111': '0010',
        '110001': '1011', '110011': '0110', '110101': '0111', '110111': '1100', '111001': '0000', '111011': '0101',
        '111101': '1110', '111111': '1001'
    },
    {
        '000000': '1010', '000010': '0000', '000100': '1001', '000110': '1110', '001000': '0110', '001010': '0011',
        '001100': '1111', '001110': '0101',
        '010000': '0001', '010010': '1101', '010100': '1100', '010110': '0111', '011000': '1011', '011010': '0100',
        '011100': '0010', '011110': '1000',
        '000001': '1011', '000011': '0111', '000101': '0000', '000111': '1001', '001001': '0011', '001011': '0100',
        '001101': '0110', '001111': '1010',
        '010001': '0010', '010011': '1000', '010101': '0101', '010111': '1110', '011001': '1100', '011011': '1011',
        '011101': '1111', '011111': '0001',
        '100000': '1101', '100010': '0110', '100100': '0100', '100110': '1001', '101000': '1000', '101010': '1111',
        '101100': '0011', '101110': '0000',
        '110000': '1011', '110010': '0001', '110100': '0010', '110110': '1100', '111000': '0101', '111010': '1010',
        '111100': '1110', '111110': '0111',
        '100001': '0001', '100011': '1010', '100101': '1011', '100111': '0000', '101001': '0110', '101011': '1001',
        '101101': '1000', '101111': '0111',
        '110001': '0100', '110011': '1111', '110101': '1110', '110111': '0011', '111001': '1011', '111011': '0101',
        '111101': '0010', '111111': '1100'

    },
    {
        '000000': '0111', '000010': '1101', '000100': '1110', '000110': '0011', '001000': '0000', '001010': '0110',
        '001100': '1001', '001110': '1010',
        '010000': '0001', '010010': '0010', '010100': '1000', '010110': '0101', '011000': '1011', '011010': '1100',
        '011100': '0100', '011110': '1111',
        '000001': '1101', '000011': '1000', '000101': '1101', '000111': '0101', '001001': '0110', '001011': '1111',
        '001101': '0000', '001111': '0011',
        '010001': '0100', '010011': '0111', '010101': '0010', '010111': '1100', '011001': '0001', '011011': '1010',
        '011101': '1110', '011111': '1001',
        '100000': '1010', '100010': '0110', '100100': '1001', '100110': '0000', '101000': '1100', '101010': '1011',
        '101100': '0111', '101110': '1101',
        '110000': '1111', '110010': '0001', '110100': '0011', '110110': '1101', '111000': '0101', '111010': '0010',
        '111100': '1000', '111110': '0100',
        '100001': '0011', '100011': '1111', '100101': '0000', '100111': '0110', '101001': '1010', '101011': '0001',
        '101101': '1101', '101111': '1000',
        '110001': '1001', '110011': '0100', '110101': '0101', '110111': '1011', '111001': '1100', '111011': '0111',
        '111101': '0010', '111111': '1110'

    },
    {

        '000000': '0010', '000010': '1100', '000100': '0100', '000110': '0001', '001000': '0111', '001010': '1010',
        '001100': '1011', '001110': '0110',
        '010000': '1000', '010010': '0101', '010100': '0011', '010110': '1111', '011000': '1101', '011010': '0000',
        '011100': '1110', '011110': '1001',
        '000001': '1110', '000011': '1011', '000101': '0010', '000111': '1100', '001001': '0100', '001011': '0111',
        '001101': '1101', '001111': '0001',
        '010001': '0101', '010011': '0000', '010101': '1111', '010111': '1010', '011001': '0011', '011011': '1001',
        '011101': '1000', '011111': '0110',
        '100000': '0100', '100010': '0010', '100100': '0001', '100110': '1011', '101000': '1010', '101010': '1101',
        '101100': '0111', '101110': '1000',
        '110000': '1111', '110010': '1001', '110100': '1100', '110110': '0101', '111000': '0110', '111010': '0011',
        '111100': '0000', '111110': '0100',
        '100001': '1011', '100011': '1000', '100101': '1100', '100111': '0111', '101001': '0001', '101011': '1110',
        '101101': '0010', '101111': '1101',
        '110001': '0110', '110011': '1111', '110101': '0000', '110111': '1001', '111001': '1010', '111011': '0100',
        '111101': '0101', '111111': '0011'

    },

    {

        '000000': '1100', '000010': '0001', '000100': '1010', '000110': '1111', '001000': '1001', '001010': '0010',
        '001100': '0110', '001110': '1000',
        '010000': '0000', '010010': '1101', '010100': '0011', '010110': '0100', '011000': '1110', '011010': '0111',
        '011100': '0101', '011110': '1011',
        '000001': '1010', '000011': '1111', '000101': '0100', '000111': '0010', '001001': '0111', '001011': '1100',
        '001101': '1001', '001111': '0101',
        '010001': '0110', '010011': '0001', '010101': '1101', '010111': '1110', '011001': '0000', '011011': '1011',
        '011101': '0011', '011111': '1000',
        '100000': '1001', '100010': '1110', '100100': '1111', '100110': '0101', '101000': '0010', '101010': '1000',
        '101100': '1100', '101110': '0011',
        '110000': '0111', '110010': '0000', '110100': '0100', '110110': '1010', '111000': '0001', '111010': '1101',
        '111100': '1011', '111110': '0110',
        '100001': '0100', '100011': '0011', '100101': '0010', '100111': '1100', '101001': '1001', '101011': '0101',
        '101101': '1111', '101111': '1010',
        '110001': '1011', '110011': '1110', '110101': '0001', '110111': '0111', '111001': '0110', '111011': '0000',
        '111101': '1000', '111111': '1101'

    },

    {

        '000000': '0100', '000010': '1011', '000100': '0010', '000110': '1110', '001000': '1111', '001010': '0000',
        '001100': '1000', '001110': '1101',
        '010000': '0011', '010010': '1100', '010100': '1001', '010110': '0111', '011000': '0101', '011010': '1010',
        '011100': '0110', '011110': '0001',
        '000001': '1101', '000011': '0000', '000101': '1011', '000111': '0111', '001001': '0100', '001011': '1001',
        '001101': '0001', '001111': '1010',
        '010001': '1110', '010011': '0011', '010101': '0101', '010111': '1100', '011001': '0010', '011011': '1111',
        '011101': '1000', '011111': '0110',
        '100000': '0001', '100010': '0100', '100100': '1011', '100110': '1101', '101000': '1100', '101010': '0011',
        '101100': '0111', '101110': '1110',
        '110000': '1010', '110010': '1111', '110100': '0110', '110110': '1000', '111000': '0000', '111010': '0101',
        '111100': '1001', '111110': '0010',
        '100001': '0110', '100011': '1011', '100101': '1101', '100111': '1000', '101001': '0001', '101011': '0100',
        '101101': '1010', '101111': '0111',
        '110001': '1001', '110011': '0101', '110101': '0000', '110111': '1111', '111001': '1110', '111011': '0010',
        '111101': '0011', '111111': '1100'

    },

    {

        '000000': '1101', '000010': '0010', '000100': '1000', '000110': '0100', '001000': '0110', '001010': '1111',
        '001100': '1011', '001110': '0001',
        '010000': '1010', '010010': '1001', '010100': '0011', '010110': '1110', '011000': '0101', '011010': '0000',
        '011100': '1100', '011110': '0111',
        '000001': '0001', '000011': '1111', '000101': '1101', '000111': '1000', '001001': '1010', '001011': '0011',
        '001101': '0111', '001111': '0100',
        '010001': '1100', '010011': '0101', '010101': '0110', '010111': '1011', '011001': '0000', '011011': '1110',
        '011101': '1001', '011111': '0010',
        '100000': '0111', '100010': '1011', '100100': '0100', '100110': '0001', '101000': '1001', '101010': '1100',
        '101100': '1110', '101110': '0010',
        '110000': '0000', '110010': '0110', '110100': '1010', '110110': '1101', '111000': '1111', '111010': '0011',
        '111100': '0101', '111110': '1000',
        '100001': '0010', '100011': '0001', '100101': '1110', '100111': '0111', '101001': '0100', '101011': '1010',
        '101101': '1000', '101111': '1101',
        '110001': '1111', '110011': '1100', '110101': '1001', '110111': '0000', '111001': '0011', '111011': '0101',
        '111101': '0110', '111111': '1011'

    },

]


def Encrypt(binKey, binMsg):
    PC1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]

    tempPCList = []
    s = ""
    i = 0

    while (i <= len(PC1) - 1):
        tempPCList.append(binKey[PC1[i] - 1])
        i += 1

    # print("The key after the PC-1 \n")
    pc1K = s.join(tempPCList)
    #print("PC-1: ", pc1K)

    # ================================================================================

    # ====================== Shift the key in 16 rounds ==============================

    Kl0 = pc1K[:28]
    Kr0 = pc1K[-28:]

    kl1 = Kl0[1:28] + Kl0[0]
    kr1 = Kr0[1:28] + Kr0[0]

    kl2 = kl1[1:28] + kl1[0]
    kr2 = kr1[1:28] + kr1[0]

    kl3 = kl2[2:28] + kl2[0] + kl2[1]
    kr3 = kr2[2:28] + kr2[0] + kr2[1]

    kl4 = kl3[2:28] + kl3[0] + kl3[1]
    kr4 = kr3[2:28] + kr3[0] + kr3[1]

    kl5 = kl4[2:28] + kl4[0] + kl4[1]
    kr5 = kr4[2:28] + kr4[0] + kr4[1]

    kl6 = kl5[2:28] + kl5[0] + kl5[1]
    kr6 = kr5[2:28] + kr5[0] + kr5[1]

    kl7 = kl6[2:28] + kl6[0] + kl6[1]
    kr7 = kr6[2:28] + kr6[0] + kr6[1]

    kl8 = kl7[2:28] + kl7[0] + kl7[1]
    kr8 = kr7[2:28] + kr7[0] + kr7[1]

    kl9 = kl8[1:28] + kl8[0]
    kr9 = kr8[1:28] + kr8[0]

    kl10 = kl9[2:28] + kl9[0] + kl9[1]
    kr10 = kr9[2:28] + kr9[0] + kr9[1]

    kl11 = kl10[2:28] + kl10[0] + kl10[1]
    kr11 = kr10[2:28] + kr10[0] + kr10[1]

    kl12 = kl11[2:28] + kl11[0] + kl11[1]
    kr12 = kr11[2:28] + kr11[0] + kr11[1]

    kl13 = kl12[2:28] + kl12[0] + kl12[1]
    kr13 = kr12[2:28] + kr12[0] + kr12[1]

    kl14 = kl13[2:28] + kl13[0] + kl13[1]
    kr14 = kr13[2:28] + kr13[0] + kr13[1]

    kl15 = kl14[2:28] + kl14[0] + kl14[1]
    kr15 = kr14[2:28] + kr14[0] + kr14[1]

    kl16 = kl15[1:28] + kl15[0]
    kr16 = kr15[1:28] + kr15[0]

    Key1 = kl1 + kr1;
    Key2 = kl2 + kr2;
    Key3 = kl3 + kr3;
    Key4 = kl4 + kr4
    Key5 = kl5 + kr5;
    Key6 = kl6 + kr6;
    Key7 = kl7 + kr7;
    Key8 = kl8 + kr8
    Key9 = kl9 + kr9;
    Key10 = kl10 + kr10;
    Key11 = kl11 + kr11;
    Key12 = kl12 + kr12
    Key13 = kl13 + kr13;
    Key14 = kl14 + kr14;
    Key15 = kl15 + kr15;
    Key16 = kl16 + kr16
    #print("C1D1: ", Key1)
    #print("C2D2: ", Key2)
    #print("C3D3: ", Key3)
    #print("C4D4: ", Key4)
    #print("C5D5: ", Key5)
    #print("C6D6: ", Key6)
    #print("C7D7: ", Key7)
    #print("C8D8: ", Key8)
    #print("C9D9: ", Key9)
    #print("C10D10: ", Key10)
    #print("C11D11: ", Key11)
    #print("C12D12: ", Key12)
    #print("C13D13: ", Key13)
    #print("C14D14:", Key14)
    #print("C15D15: ", Key15)
    #print("C16D16: ", Key16)


    # ================================================================================

    # ========================== Enter the 16 sub keys on PC-2 =======================

    PC2 = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]

    tempPCList1 = [];
    tempPCList2 = [];
    tempPCList3 = [];
    tempPCList4 = [];
    tempPCList5 = [];
    tempPCList6 = [];
    tempPCList7 = [];
    tempPCList8 = [];
    tempPCList9 = [];
    tempPCList10 = [];
    tempPCList11 = [];
    tempPCList12 = [];
    tempPCList13 = [];
    tempPCList14 = [];
    tempPCList15 = [];
    tempPCList16 = [];

    s = ""
    i = 0

    while (i <= len(PC2) - 1):
        tempPCList1.append(Key1[PC2[i] - 1]);
        tempPCList2.append(Key2[PC2[i] - 1])
        tempPCList3.append(Key3[PC2[i] - 1]);
        tempPCList4.append(Key4[PC2[i] - 1])
        tempPCList5.append(Key5[PC2[i] - 1]);
        tempPCList6.append(Key6[PC2[i] - 1])
        tempPCList7.append(Key7[PC2[i] - 1]);
        tempPCList8.append(Key8[PC2[i] - 1])
        tempPCList9.append(Key9[PC2[i] - 1]);
        tempPCList10.append(Key10[PC2[i] - 1])
        tempPCList11.append(Key11[PC2[i] - 1]);
        tempPCList12.append(Key12[PC2[i] - 1])
        tempPCList13.append(Key13[PC2[i] - 1]);
        tempPCList14.append(Key14[PC2[i] - 1])
        tempPCList15.append(Key15[PC2[i] - 1]);
        tempPCList16.append(Key16[PC2[i] - 1])

        i += 1

    # print("The 16 sub keys for the encryption operartion are: \n")

    K1 = s.join(tempPCList1);
    K2 = s.join(tempPCList2)
    K3 = s.join(tempPCList3);
    K4 = s.join(tempPCList4)
    K5 = s.join(tempPCList5);
    K6 = s.join(tempPCList6)
    K7 = s.join(tempPCList7);
    K8 = s.join(tempPCList8)
    K9 = s.join(tempPCList9);
    K10 = s.join(tempPCList10)
    K11 = s.join(tempPCList11);
    K12 = s.join(tempPCList12)
    K13 = s.join(tempPCList13);
    K14 = s.join(tempPCList14)
    K15 = s.join(tempPCList15);
    K16 = s.join(tempPCList16)

    List_of_Keys = [
        K1, K2, K3, K4, K5, K6, K7, K8,
        K9, K10, K11, K12, K13, K14, K15, K16
    ]

    #print("K1=", " ", K1);
    #print("K2=", " ", K2);
    #print("K3=", " ", K3);
    #print("K4=", " ", K4);
    #print("K5=", " ", K5);
    #print("K6=", " ", K6);
    #print("K7=", " ", K7);
    #print("K8=", " ", K8);
    #print("K9=", " ", K9);
    #print("K10=", " ", K10);
    #print("K11=", " ", K11);
    #print("K12=", " ", K12);
    #print("K13=", " ", K13);
    #print("K14=", " ", K14);
    #print("K15=", " ", K15);
    #print("K16=", " ", K16);
    #print("\n")
    # preproses pesan
    # ======================== Enter message on IP array ============================

    IP = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]

    tempIPList = []
    s = ""
    i = 0

    while (i <= len(IP) - 1):
        tempIPList.append(binMsg[IP[i] - 1])
        i += 1

    # print("The message after the IP \n")
    msgIP = s.join(tempIPList)
    #print("IP: ", msgIP, "\n")

    # ===============================================================================

    L0 = msgIP[:32]
    R0 = msgIP[-32:]

    LeftSideList = [L0]
    RightSideList = [R0]

    for i in range(16):

        # print("Encryption:", " ", "Round", i + 1)
        LeftSideList.append(RightSideList[i])
        E = [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1
        ]

        tempERList = []
        s = ""
        m = 0
        R = RightSideList[i]

        while (m <= len(E) - 1):
            tempERList.append(R[E[m] - 1])
            m += 1

        ER = s.join(tempERList)
        #print("E(R(i)-1): ", ER)

        tempF = []
        s = ""
        SUB_KEY = List_of_Keys[i]

        for x in range(48):
            if (SUB_KEY[x] == '0' and ER[x] == '0' or SUB_KEY[x] == '1' and ER[x] == '1'):
                tempF.append('0')
            elif (SUB_KEY[x] == '0' and ER[x] == '1' or SUB_KEY[x] == '1' and ER[x] == '0'):
                tempF.append('1')

        xorV = s.join(tempF)
        #print('A1: ', xorV)

        divideR = [];
        start = 0;
        inc = 5;
        end = 47
        while (start <= end):
            divideR.append(xorV[start:inc + 1])
            start = inc + 1
            inc += 6

        tempSboxesList = []
        for p in range(len(divideR)):
            item = divideR[p]
            dict = Sboxes[p]
            tempSboxesList.append(dict[item])

        Results_of_Sboxes = s.join(tempSboxesList)
        #print("B1: ",  Results_of_Sboxes)

        P = [

            16, 7, 20, 21,
            29, 12, 28, 17,
            1, 15, 23, 26,
            5, 18, 31, 10,
            2, 8, 24, 14,
            32, 27, 3, 9,
            19, 13, 30, 6,
            22, 11, 4, 25
        ]

        counter = 0
        s = ''
        tempFList = []
        while (counter <= len(P) - 1):
            tempFList.append(Results_of_Sboxes[P[counter] - 1])
            counter += 1

        F = s.join(tempFList)
        #print("P(B1) =", " ",F)

        tempNewR = []
        s = ''
        PreviousL = LeftSideList[i]
        for n in range(32):
            if (F[n] == '0' and PreviousL[n] == '0' or F[n] == '1' and PreviousL[n] == '1'):
                tempNewR.append('0')
            elif (F[n] == '0' and PreviousL[n] == '1' or F[n] == '1' and PreviousL[n] == '0'):
                tempNewR.append('1')

        NextR = s.join(tempNewR)
        RightSideList.append(NextR)
        #print(NextR, "\n")

        # print("L =", " ",LeftSideList)
        # print("R =", " ",RightSideList)

        #print('R dan L',RightSideList[i + 1], " ", LeftSideList[i])

        if (i == 15):

            tempCipher = RightSideList[i + 1] + LeftSideList[i + 1]

            ipInverse = [
                40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25
            ]

            count = 0
            s = ''
            tempCipherList = []
            while (count <= len(ipInverse) - 1):
                tempCipherList.append(tempCipher[ipInverse[count] - 1])
                count += 1

            Cipher = s.join(tempCipherList)
            hasil = Cipher
            #print("Cipertext: ", hasil)
            # print("Ciphertext dalam biner :", hasil)
            result = ""
            b = int(hasil, 2)
            hdnum = hex(b)
            a = hdnum[2:].upper()
            # print("\nCipher text dalam hexadesimal ", a)
            # Chipertext dalam ASCII
            result = ""

            while Cipher:
                result += chr(int(Cipher[:8], 2))
                Cipher = Cipher[8:]
            # print("Cipher text Final =", " ", result)
            return hasil

            # while Cipher:
            # result += chr(int(Cipher[:8], 2))
            # Cipher = Cipher[8:]
            # print("Cipher text Final =", result)


def generateKey(string, key):
    key2 = list(key)
    if len(string) == len(key2):
        return (key2)
    else:
        for i in range(len(string) - len(key2)):
            key2.append(key2[i % len(key2)])
    return ("".join(key2))


def encryption(string, key):
    string1 = list(string)
    #print("string1:", string1)
    #print("Key:", key)
    encrypt_text = []
    for i in range(len(string1)):
        x = (ord(string1[i]) + ord(key[i]))
        #print("x[",i,"]: ", ord(string1[i]))
        #print("key[", i, "]: ", ord(key[i]))
        while x > 126:
            x -= 95
            #print("ENSKRIPSI VIGENERE1:", x)
        while x < 32:
            x += 95
            #print("ENSKRIPSI VIGENERE2:", x)
        encrypt_text.append(chr(x))
    #print("".join(encrypt_text))
    return ("".join(encrypt_text))


def decryption(encrypt_text, key):
    orig_text = []
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i]))
        while x > 126:
            x -= 95
        while x < 32:
            x += 95
        orig_text.append(chr(x))
    a = "".join(orig_text)

    return (a)


def Decrypt(binKey, binMsg):
    # ========== process key bits on a permutation array of 56 values ================

    PC1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]

    tempPCList = []
    s = ""
    i = 0

    while (i <= len(PC1) - 1):
        tempPCList.append(binKey[PC1[i] - 1])
        i += 1

    pc1K = s.join(tempPCList)

    # ================================================================================

    # ====================== Shift the key in 16 rounds ==============================

    Kl0 = pc1K[:28]
    Kr0 = pc1K[-28:]

    kl1 = Kl0[1:28] + Kl0[0]
    kr1 = Kr0[1:28] + Kr0[0]

    kl2 = kl1[1:28] + kl1[0]
    kr2 = kr1[1:28] + kr1[0]

    kl3 = kl2[2:28] + kl2[0] + kl2[1]
    kr3 = kr2[2:28] + kr2[0] + kr2[1]

    kl4 = kl3[2:28] + kl3[0] + kl3[1]
    kr4 = kr3[2:28] + kr3[0] + kr3[1]

    kl5 = kl4[2:28] + kl4[0] + kl4[1]
    kr5 = kr4[2:28] + kr4[0] + kr4[1]

    kl6 = kl5[2:28] + kl5[0] + kl5[1]
    kr6 = kr5[2:28] + kr5[0] + kr5[1]

    kl7 = kl6[2:28] + kl6[0] + kl6[1]
    kr7 = kr6[2:28] + kr6[0] + kr6[1]

    kl8 = kl7[2:28] + kl7[0] + kl7[1]
    kr8 = kr7[2:28] + kr7[0] + kr7[1]

    kl9 = kl8[1:28] + kl8[0]
    kr9 = kr8[1:28] + kr8[0]

    kl10 = kl9[2:28] + kl9[0] + kl9[1]
    kr10 = kr9[2:28] + kr9[0] + kr9[1]

    kl11 = kl10[2:28] + kl10[0] + kl10[1]
    kr11 = kr10[2:28] + kr10[0] + kr10[1]

    kl12 = kl11[2:28] + kl11[0] + kl11[1]
    kr12 = kr11[2:28] + kr11[0] + kr11[1]

    kl13 = kl12[2:28] + kl12[0] + kl12[1]
    kr13 = kr12[2:28] + kr12[0] + kr12[1]

    kl14 = kl13[2:28] + kl13[0] + kl13[1]
    kr14 = kr13[2:28] + kr13[0] + kr13[1]

    kl15 = kl14[2:28] + kl14[0] + kl14[1]
    kr15 = kr14[2:28] + kr14[0] + kr14[1]

    kl16 = kl15[1:28] + kl15[0]
    kr16 = kr15[1:28] + kr15[0]

    Key1 = kl1 + kr1;
    Key2 = kl2 + kr2;
    Key3 = kl3 + kr3;
    Key4 = kl4 + kr4
    Key5 = kl5 + kr5;
    Key6 = kl6 + kr6;
    Key7 = kl7 + kr7;
    Key8 = kl8 + kr8
    Key9 = kl9 + kr9;
    Key10 = kl10 + kr10;
    Key11 = kl11 + kr11;
    Key12 = kl12 + kr12
    Key13 = kl13 + kr13;
    Key14 = kl14 + kr14;
    Key15 = kl15 + kr15;
    Key16 = kl16 + kr16

    # ================================================================================

    # ========================== Enter the 16 sub keys on PC-2 =======================

    PC2 = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]

    tempPCList1 = [];
    tempPCList2 = [];
    tempPCList3 = [];
    tempPCList4 = [];
    tempPCList5 = [];
    tempPCList6 = [];
    tempPCList7 = [];
    tempPCList8 = [];
    tempPCList9 = [];
    tempPCList10 = [];
    tempPCList11 = [];
    tempPCList12 = [];
    tempPCList13 = [];
    tempPCList14 = [];
    tempPCList15 = [];
    tempPCList16 = [];

    s = ""
    i = 0

    while (i <= len(PC2) - 1):
        tempPCList1.append(Key1[PC2[i] - 1]);
        tempPCList2.append(Key2[PC2[i] - 1])
        tempPCList3.append(Key3[PC2[i] - 1]);
        tempPCList4.append(Key4[PC2[i] - 1])
        tempPCList5.append(Key5[PC2[i] - 1]);
        tempPCList6.append(Key6[PC2[i] - 1])
        tempPCList7.append(Key7[PC2[i] - 1]);
        tempPCList8.append(Key8[PC2[i] - 1])
        tempPCList9.append(Key9[PC2[i] - 1]);
        tempPCList10.append(Key10[PC2[i] - 1])
        tempPCList11.append(Key11[PC2[i] - 1]);
        tempPCList12.append(Key12[PC2[i] - 1])
        tempPCList13.append(Key13[PC2[i] - 1]);
        tempPCList14.append(Key14[PC2[i] - 1])
        tempPCList15.append(Key15[PC2[i] - 1]);
        tempPCList16.append(Key16[PC2[i] - 1])

        i += 1

    # print("The 16 sub keys for the encryption operartion are: \n")

    K1 = s.join(tempPCList1);
    K2 = s.join(tempPCList2)
    K3 = s.join(tempPCList3);
    K4 = s.join(tempPCList4)
    K5 = s.join(tempPCList5);
    K6 = s.join(tempPCList6)
    K7 = s.join(tempPCList7);
    K8 = s.join(tempPCList8)
    K9 = s.join(tempPCList9);
    K10 = s.join(tempPCList10)
    K11 = s.join(tempPCList11);
    K12 = s.join(tempPCList12)
    K13 = s.join(tempPCList13);
    K14 = s.join(tempPCList14)
    K15 = s.join(tempPCList15);
    K16 = s.join(tempPCList16)

    List_of_Keys = [
        K1, K2, K3, K4, K5, K6, K7, K8,
        K9, K10, K11, K12, K13, K14, K15, K16
    ]

    # ================================================================================

    # ============================ Message Processing ===============================

    # ==============================================================================

    # ======================== Enter message on IP array ============================

    IP = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    tempIPList = []
    s = ""
    i = 0

    while (i <= len(IP) - 1):
        tempIPList.append(binMsg[IP[i] - 1])
        i += 1

    # print("The message after the IP \n")
    msgIP = s.join(tempIPList)
    #print("IP1: ",msgIP, "\n")

    # ===============================================================================

    R16 = msgIP[:32]
    L16 = msgIP[-32:]

    LeftSideList = [R16]
    RightSideList = [L16]

    for i in range(16):

        # print("Decryption:", " ", "Round", i + 1)
        LeftSideList.append(RightSideList[i])
        E = [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1
        ]

        tempERList = []
        s = ""
        m = 0
        R = RightSideList[i]

        while (m <= len(E) - 1):
            tempERList.append(R[E[m] - 1])
            m += 1

        ER = s.join(tempERList)

        tempF = []
        s = ""
        SUB_KEY = List_of_Keys[15 - i]

        for x in range(48):
            if (SUB_KEY[x] == '0' and ER[x] == '0' or SUB_KEY[x] == '1' and ER[x] == '1'):
                tempF.append('0')
            elif (SUB_KEY[x] == '0' and ER[x] == '1' or SUB_KEY[x] == '1' and ER[x] == '0'):
                tempF.append('1')

        xorV = s.join(tempF)

        divideR = [];
        start = 0;
        inc = 5;
        end = 47
        while (start <= end):
            divideR.append(xorV[start:inc + 1])
            start = inc + 1
            inc += 6

        tempSboxesList = []
        for p in range(len(divideR)):
            item = divideR[p]
            dict = Sboxes[p]
            tempSboxesList.append(dict[item])

        Results_of_Sboxes = s.join(tempSboxesList)

        P = [

            16, 7, 20, 21,
            29, 12, 28, 17,
            1, 15, 23, 26,
            5, 18, 31, 10,
            2, 8, 24, 14,
            32, 27, 3, 9,
            19, 13, 30, 6,
            22, 11, 4, 25
        ]

        counter = 0
        s = ''
        tempFList = []
        while (counter <= len(P) - 1):
            tempFList.append(Results_of_Sboxes[P[counter] - 1])
            counter += 1

        F = s.join(tempFList)
        # print("F =", " ",F)

        tempNewR = []
        s = ''
        PreviousR = LeftSideList[i]
        for n in range(32):
            if (F[n] == '0' and PreviousR[n] == '0' or F[n] == '1' and PreviousR[n] == '1'):
                tempNewR.append('0')
            elif (F[n] == '0' and PreviousR[n] == '1' or F[n] == '1' and PreviousR[n] == '0'):
                tempNewR.append('1')

        NextL = s.join(tempNewR)
        RightSideList.append(NextL)
        # print(NextL, "\n")

        # print("L =", " ",LeftSideList)
        # print("R =", " ",RightSideList)

        # print(RightSideList[i + 1], " ", LeftSideList[i])

        if (i == 15):

            tempPlain = RightSideList[i + 1] + LeftSideList[i + 1]

            ipInverse = [
                40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25
            ]

            count = 0
            s = ''
            tempPlainList = []
            while (count <= len(ipInverse) - 1):
                tempPlainList.append(tempPlain[ipInverse[count] - 1])
                count += 1

            plain = s.join(tempPlainList)
            return plain


def leftrotate(string):
    r_rot = 1
    l_rot = 2
    temp = (l_rot - r_rot) % len(string)
    res = string[temp:] + string[: temp]
    return res


def rightrotate(string):
    r_rot = 1
    l_rot = 2
    temp = (r_rot - l_rot) % len(string)
    res = string[temp:] + string[: temp]
    return res


def encryptOTP(message, key):
    result = ""
    #print("message:", message)
    #print("key:", key)
    cipher_binary = xor(message, key)
    #print("XOR OTP:", cipher_binary)
    a = "".join(str(e) for e in cipher_binary)
    #print("a:", a)
    return a


def decryptOTP(cipher_text, key):
    binary_message = xor(cipher_text, key)
    a = "".join(str(e) for e in binary_message)
    result = ""
    Cipher = a
    # print(Cipher)
    while Cipher:
        result += chr(int(Cipher[:8], 2))
        Cipher = Cipher[8:]
    return a


abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']


def encode(kalimat, cipher_key):
    kalimat = kalimat.lower()
    hasil_encode = ''
    for karakter in kalimat:
        if karakter in abjad:
            index_lama = abjad.index(karakter)
            index_baru = (index_lama + cipher_key) % len(abjad)
            abjad_baru = abjad[index_baru]
            hasil_encode = hasil_encode + abjad_baru
        else:
            hasil_encode = hasil_encode + ' '
    return hasil_encode


def deskrip_encode(kalimat, cipher_key):
    kalimat = kalimat.lower()
    hasil_encode = ''
    for karakter in kalimat:
        if karakter in abjad:
            index_lama = abjad.index(karakter)

            index_baru = (index_lama - cipher_key) % len(abjad)
            abjad_baru = abjad[index_baru]
            hasil_encode = hasil_encode + abjad_baru
        else:
            hasil_encode = hasil_encode + ' '
    return hasil_encode


if __name__ == "__main__":
    pilihan = 0
    while pilihan == 0:
        print("Selamat datang di program Enkripsi")
        print("1. Enkripsi Kunci")
        print("2. Enkripsi Pesan")
        print("3. Dekripsi Pesan")
        print("4. Deskripsi Kunci")
        print("5. Keluar")
        q = input("Masukkan pilihan :")
        while q != '1' and q != '2' and q != '3' and q != '4' and q != '5' :
            print("Input yang anda masukkan salah ")
            q = input("Masukkan pilihan :")
        if q == '1':
            string = input("Masukkan plaintext kunci : ")
            keyword = input("Masukkan kunci           : ")
            shift_c = 0
            pin = 0
            for i in keyword:
                if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o':
                    pin = pin + 1
                    shift_c = shift_c + 1
                else:
                    pindah1 = leftrotate(keyword)
            b = 0
            print("pindah", pin)
            while pin > 0:
                pindah = rightrotate(keyword)
                keyword = pindah
                b = b + 1
                #print(pindah)
                #print(b)
                pin = pin - 1
            #print("pindah1: ", shift_c)
            print("")
            print("------ENKRIPSI KUNCI :: CAESAR--------")
            kalimat_hasil = encode(string, shift_c)
            hasilc = kalimat_hasil
            print('HASIL CAESAR CIPHER: ', kalimat_hasil)
            #string1 = "osqtyxiv"
            key2 = generateKey(hasilc, pindah)
            #print("key2: ", key2)
            kuncibiner = ''.join(format(ord(i), '08b') for i in key2)
            pesanbiner = ''.join(format(ord(i), '08b') for i in hasilc)
            #print("kuncipesan key biner: ", kuncibiner)
            #print("plainteks key biner: ", pesanbiner)
            print(" ")
            print("------ENKRIPSI KUNCI :: DES ROUND 1--------")

            encryptkeydes1 = Encrypt(kuncibiner, pesanbiner)
            hasil12 = encryptkeydes1
            #print("enskripsi DES: ", hasil12)
            # print("Ciphertext dalam biner :", hasil)
            result12 = ""
            b12 = int(hasil12, 2)
            hdnum12 = hex(b12)
            a12 = hdnum12[2:].upper()
            print("\nEnkripsi kunci (DES ROUND 1) [Hex] = ", a12)
            # Chipertext dalam ASCII
            result12 = ""

            while hasil12:
                result12 += chr(int(hasil12[:8], 2))
                hasil12 = hasil12[8:]
            print("Enkripsi kunci (DES ROUND 1) [ASCII] =", result12)
            # print(encryptkeydes1)
            print(" ")
            print("------ENKRIPSI KUNCI :: OTP----------------")

            keyOTP = encryptOTP(encryptkeydes1, kuncibiner)
            hasil14 = keyOTP
            b14 = int(hasil14, 2)
            hdnum14 = hex(b14)
            hexa14 = hdnum14[2:].upper()
            print("\nEnkripsi Kunci OTP [Hex]   =", hexa14)
            # print(Cipher)
            result14 = ''
            while hasil14:
                result14 += chr(int(hasil14[:8], 2))
                hasil14 = hasil14[8:]
            print("Enkripsi Kunci OTP [ASCII] =", result14)
            print(" ")
            print("------ENKRIPSI KUNCI :: DES ROUND 2--------")

            keydes2 = Encrypt(kuncibiner, keyOTP)
            hasil13 = keydes2
            # print("Ciphertext dalam biner :", hasil)
            result13 = ""
            b13 = int(hasil13, 2)
            hdnum13 = hex(b13)
            a13 = hdnum13[2:].upper()
            print("Enkripsi kunci (DES ROUND 2) [Hex]   =", a13)
            # Chipertext dalam ASCII
            result13 = ""

            while hasil13:
                result13 += chr(int(hasil13[:8], 2))
                hasil13 = hasil13[8:]
            print("Enkripsi kunci (DES ROUND 2) [ASCII] =", " ", result13)
            print(" ")
            print("--------------------------------------------------------")
            # print("| HASIL ENSKRIPSI KUNCI DALAM [HEX] : ", a13, "       |")
            print("| HASIL ENSKRIPSI KUNCI DALAM ASCII : ", result13, "        |")
            print("| HASIL ENSKRIPSI KUNCI DALAM HEXA  : ", a13,"|")
            print("--------------------------------------------------------")
            b = int(keydes2, 2)
            hdnum = hex(b)
            keyhexa = hdnum[2:].upper()
            # p = len(keyOTP)
            #print("Enkripsikunci", keyhexa)
            print("")
        elif q == '2':
            print("-------------------------------------------------------------")
            print("                     ENKRIPSI PLAIN TEXT                    ")
            teksplain = input("Masukkan plain text :")
            while len(teksplain) != 8:
                teksplain = input(
                    "Input yang anda masukkan harus sebanyak 8 huruf, silakan masukkan kembali plaintext : ")
            plaintekshex = teksplain.encode("utf-8").hex()
            result13 = input("Masukkan Kunci      :")
            # print("Plaintext dalam heksadesimal : ", plaintekshex)
            encrypt_text1 = encryption(teksplain, result13)
            print("----------------------------------------------------------")
            print("          PROSES ENKRIPSI VIGENERE ROUND 1               | ")
            print("Enkripsi Vigenere Round 1 :", encrypt_text1)
            keybaru1 = leftrotate(result13)
            # print("Kunci leftshift : ", keybaru1)
            string2 = rightrotate(encrypt_text1)
            # print("Teks rightshift : ", string2)
            print("----------------------------------------------------------")
            print("          PROSES ENKRIPSI VIGENERE ROUND 2               | ")
            encrypt_text2 = encryption(string2, keybaru1)
            print("Enkripsi Vigenere Round 2 :", encrypt_text2)
            print("Enkripsi kunci ",keybaru1)
            print("----------------------------------------------------------")
            print("          PROSES ENKRIPSI VIGENERE ROUND 3               | ")
            encrypt_text = encryption(encrypt_text2, keybaru1)
            print("Enkripsi Vigenere Round 3 :", encrypt_text)
            # binKey =kuncibaru
            # print("Kunci dalam biner", binKey)
            binKey = ''.join(format(ord(i), '08b') for i in keybaru1)

            binMsg = ''.join(format(ord(i), '08b') for i in encrypt_text)

            #print("Plain text dalam biner", binMsg)
            #print("Plain Key dalam biner", binKey)
            print("----------------------------------------------------------")
            print("                    PROSES ENKRIPSI DES                    ")
            chiperakhir = Encrypt(binKey, binMsg)
            hasil15 = chiperakhir
            # print(hasil15)
            # print("Ciphertext dalam biner :", hasil)
            result15 = ""
            b15 = int(hasil15, 2)
            hdnum15 = hex(b15)
            a15 = hdnum15[2:].upper()
            A15 = a15
            # Chipertext dalam ASCII
            result15 = ""

            while hasil15:
                result15 += chr(int(hasil15[:8], 2))
                hasil15 = hasil15[8:]
            print("Enkripsi PESAN DALAM DES [ASCII] =", result15)
            print("Enkripsi Pesan Dalam DES [Hex]   =", A15)
            keyhexfinal = keyhexa[2:] + keyhexa[: 2]
            print("Enkripsi kunci [ASCII]           =", keybaru1)
            print("enkripsi kunci [HEX]             = ", keyhexfinal)

            print("\n ---------------ENKRIPSI BASE 64 ----------------------------\n")
            b64 = base64.b64encode(bytes.fromhex(keyhexfinal)).decode()
            print("KUNCI TER-ENKRIPSI (CHIPERKEY) :", b64)
            b641 = base64.b64encode(bytes.fromhex(A15)).decode()
            print("PESAN TER-ENKRIPSI (CHIPERTEXT) :", b641)
            print("-----------------------------------------------------------")
            pilihan = 1
        if q == '3':
            chipstring = input("Masukkan Chipertext :")
            q21 = base64.b64decode(chipstring.encode()).hex()
            chipkey = input("Masukkan kunci : ")
            q22 = base64.b64decode(chipkey.encode()).hex()
            binchipkey = "{0:08b}".format(int(q22, 16)).zfill(64)
            hasil2 = binchipkey
            print("----------------------------------------------------------")
            print("             PROSES DEKRIPSI BASE64                       ")
            hasil99 = hasil2
            result99 = ''
            while hasil99:
                result99 += chr(int(hasil99[:8], 2))
                hasil99 = hasil99[8:]
            binchipstring = "{0:08b}".format(int(q21, 16)).zfill(64)
            hasil98 = binchipstring
            result98 = ''
            while hasil98:
                result98 += chr(int(hasil98[:8], 2))
                hasil98 = hasil98[8:]
            print("Hasil Dekripsi Pesan Base64 :", result98)
            print("Hasil Dekripsi kunci Base64 :", result99)

            print("----------------------------------------------------------")
            print("                PROSES DEKRIPSI DES                       ")
            plaindes = Decrypt(binchipkey, binchipstring)
            hasill22 = plaindes
            resultt44 = ''
            while hasill22:
                resultt44 += chr(int(hasill22[:8], 2))
                hasill22 = hasill22[8:]
            print("Hasil Dekripsi DES : ", resultt44)

            print("----------------------------------------------------------")
            print("          PROSES DEKRIPSI VIGENERE ROUND 1               ")
            result4 = ''
            while hasil2:
                result4 += chr(int(hasil2[:8], 2))
                hasil2 = hasil2[8:]
            # print(result4)

            desvig = decryption(resultt44, result4)
            print("Hasil deskrivisi vigenere Round 1", desvig)
            print("----------------------------------------------------------")
            print("          PROSES DEKRIPSI VIGENERE ROUND 2               ")
            desvig2 = decryption(desvig, result4)
            print("Dekripsi vigenere round 2 :", desvig2)
            keyasli = rightrotate(result4)
            string3 = leftrotate(desvig2)
            desvig1 = decryption(string3, keyasli)
            print("----------------------------------------------------------")
            print("          PROSES DEKRIPSI VIGENERE ROUND 3               ")
            print("Dekripsi Vigenere Round 3 : ", desvig1)
            print("----------------------------------------------------------")
            print("|                HASIL DEKRIPSI                        | ")
            print("Hasil Dekripsi (Plain Text) dalam ASCII :", desvig1)
            a = desvig1.encode("utf-8").hex()
            print("Hasil Dekripsi (Plain Text) dalam Heksadesimal : ", a)
            pilihan = 1
        if q == '4':
            pu = input("Masukkan CHIPERKEY : ")
            q2 = base64.b64decode(pu.encode()).hex()
            qu = input("masukkan kunci : ")
            pin1 = 0
            n = 0
            for i in qu:
                if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o':
                    pin1 = pin1 + 1
                    n = n + 1
                else:
                    pindah11 = leftrotate(qu)
            b1 = 0
            #print("pindah", pin1)
            while pin1 > 0:
                pindah11 = rightrotate(qu)
                qu = pindah11
                b1 = b1 + 1
                #print(pindah11)
                #print(b1)
                pin1 = pin1 - 1
            finalkey = rightrotate(q2)
            finalkey1 = rightrotate(finalkey)

            keymain = ''.join(format(ord(i), '08b') for i in pindah11)

            keychipbin = "{0:08b}".format(int(finalkey1, 16)).zfill(64)

            keylagi = generateKey(keychipbin, keymain)

            print("------------- DEKRIPSI DES ROUND 1 ---------------")
            decdes = Decrypt(keylagi, keychipbin)
            hasil1 = decdes
            b = int(hasil1, 2)
            hdnum = hex(b)
            a = hdnum[2:].upper()
            print("\nPlain Key dalam Heksadesimal [DES Round 1] ", a)
            result = ""

            while hasil1:
                result += chr(int(hasil1[:8], 2))
                hasil1 = hasil1[8:]
            print("Plain Key dalam ASCII [DES Round 1] =", " ", result)
            print("\n----------------- DEKRIPSI OTP --------------------")
            decOTP = decryptOTP(decdes, keylagi)

            hasill12 = decOTP
            b112 = int(hasill12, 2)
            hdnum112 = hex(b112)
            a112 = hdnum112[2:].upper()
            print("\nPlain Key dalam Heksadesimal [OTP] ", a112)
            result112 = ""

            while hasill12:
                result112 += chr(int(hasill12[:8], 2))
                hasill12 = hasill12[8:]
            print("Plain Key dalam ASCII [OTP] =", " ", result112)
            #print("decOTP: ", decOTP)
            print("------------- DEKRIPSI DES ROUND 2 ---------------")
            decdes1 = Decrypt(keylagi, decOTP)
            hasill = decdes1
            ba = int(hasill, 2)
            hdnuma = hex(ba)
            ac = hdnuma[2:].upper()
            print("\nPlain Key dalam hexadesimal [DES Round 2] :", ac)
            resultt = ""

            while hasill:
                resultt += chr(int(hasill[:8], 2))
                hasill = hasill[8:]
            kalimat_des = deskrip_encode(resultt, n)
            print("\nPlain Key dalam ASCII [DES Round 2] :", kalimat_des)
            print("\n----------------- DEKRIPSI CAESAR --------------------")
            print("\nDESKRIPSI KEY DALAM CAESAR: ", kalimat_des)
            print("------------- HASIL DEKRIPSI KUNCI ---------------")
            print("Plain Key dalam ASCII =", " ", kalimat_des)
            pilihan = 1

        if q == '5':
            print("TERIMA KASIH")
            pilihan = 1
