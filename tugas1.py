import os

from termcolor import colored
import numpy



#get Ordo
class get_ordo_Input:
    def __init__(self):
        valid1 = False
        valid2 = False
        valid3 = False
        valid4 = False

        while valid1 == False:
            try:
                row_A = int(input("Masukan baris matriks A: "))
                self.row_A = row_A
                valid1 = True
            except ValueError:
                print(colored('Harap hanya memasukan angka!','red'))
                valid1 = False

        while valid2 == False:
            try:
                column_A = int(input("Masukan kolom matriks A: "))
                self.column_A = column_A
                valid2 = True
            except ValueError:
                print(colored('Harap hanya memasukan angka!','red'))
                valid2 = False

        while valid3 == False:
            try:
                row_B = int(input("Masukan baris matriks B: "))
                self.row_B = row_B
                valid3 = True
            except ValueError:
                print(colored('Harap hanya memasukan angka!','red'))
                valid3 = False

        while valid4 == False:
            try:
                column_B = int(input("Masukan kolom matriks B: "))
                self.column_B = column_B
                valid4 = True
            except ValueError:
                print(colored('Harap hanya memasukan angka!','red'))
                valid4 = False

        print("\n")


class get_Data_Matriks:
    def __init__(self, row_A,row_B,column_A,column_B):
        matrix_A = numpy.zeros(shape=(row_A, column_A), dtype=float)
        matrix_B = numpy.zeros(shape=(row_B, column_B), dtype=float)

        print(colored("Data Matriks A:",'blue'))
        for i in range(row_A):
            for i2 in range(column_A):
                valid = False
                while valid == False:
                    try:
                        data = float(input("masukan baris " + str(i+1) + " kolom " + str(i2 + 1) + ": "))
                        matrix_A[i,i2] = data
                        valid = True
                    except ValueError:
                        print(colored('Harap hanya memasukan angka!', 'red'))
                        valid = False

        print("\n")
        print(colored("Data Matriks B:", 'blue'))
        for j in range(row_B):
            for j2 in range(column_B):
                valid = False
                while valid == False:
                    try:
                        data2 = float(input("masukan baris " + str(j+1) + " kolom " + str(j2 + 1) + ": "))
                        matrix_B[j,j2] = data2
                        valid = True
                    except ValueError:
                        print(colored('Harap hanya memasukan angka!', 'red'))
                        valid = False

        print("\n")
        self.Matrix_A = matrix_A
        self.Matrix_B = matrix_B






def penjumlahan_matriks():

    print(colored("Penjumlahan matriks \n",'green', attrs=['bold']))
    getOrdo = get_ordo_Input()
    while getOrdo.row_A != getOrdo.row_B or getOrdo.column_A != getOrdo.column_B:
        print(colored('Ordo matriks A dan B tidak sama !', 'red'))
        getOrdo = get_ordo_Input()

    getMatriks = get_Data_Matriks(getOrdo.row_A,getOrdo.row_B,getOrdo.column_A,getOrdo.column_B)
    print(colored("Data matriks A:",'blue'))
    print(getMatriks.Matrix_A)
    print("\n")
    print(colored("Data matriks B:", 'blue'))
    print(getMatriks.Matrix_B)
    print("\n")
    print(colored("Matriks A+B:", 'blue'))
    matrix_A = numpy.zeros(shape=(getOrdo.row_A, getOrdo.column_A), dtype=float)
    for x in range(0, len(getMatriks.Matrix_A)):
        for y in range(0, len(getMatriks.Matrix_A[0])):
            data = (getMatriks.Matrix_A[x][y] + getMatriks.Matrix_B[x][y])
            matrix_A[x, y] = data

    print(matrix_A)
    print("\n")


def pengurangan_matriks():
    print(colored("Pengurangan matriks \n", 'green', attrs=['bold']))
    getOrdo = get_ordo_Input()
    while getOrdo.row_A != getOrdo.row_B or getOrdo.column_A != getOrdo.column_B:
        print(colored('Ordo matriks A dan B tidak sama !', 'red'))
        getOrdo = get_ordo_Input()

    getMatriks = get_Data_Matriks(getOrdo.row_A, getOrdo.row_B, getOrdo.column_A, getOrdo.column_B)
    print(colored("Data matriks A:", 'blue'))
    print(getMatriks.Matrix_A)
    print("\n")
    print(colored("Data matriks B:", 'blue'))
    print(getMatriks.Matrix_B)
    print("\n")

    print(colored("Matriks A-B:", 'blue'))
    matrix_A = numpy.zeros(shape=(getOrdo.row_A, getOrdo.column_A), dtype=float)
    matrix_B = numpy.zeros(shape=(getOrdo.row_A, getOrdo.column_A), dtype=float)

    for x in range(0, len(getMatriks.Matrix_A)):
        for y in range(0, len(getMatriks.Matrix_A[0])):
            data = (getMatriks.Matrix_A[x][y] - getMatriks.Matrix_B[x][y])
            matrix_A[x, y] = data

    print(matrix_A)
    print("\n")
    print(colored("Matriks B-A:", 'blue'))

    for x in range(0, len(getMatriks.Matrix_B)):
        for y in range(0, len(getMatriks.Matrix_B[0])):
            data = (getMatriks.Matrix_B[x][y] - getMatriks.Matrix_A[x][y])
            matrix_B[x, y] = data

    print(matrix_B)
    print("\n")

def perkalian_skalar():
    print(colored("Perkalian skalar matriks \n", 'green', attrs=['bold']))
    getOrdo = get_ordo_Input()
    getMatriks = get_Data_Matriks(getOrdo.row_A, getOrdo.row_B, getOrdo.column_A, getOrdo.column_B)
    skalar = float(input(colored("Masukan nilai skalar:\n", 'yellow')))
    matrix_A = numpy.zeros(shape=(getOrdo.row_A, getOrdo.column_A), dtype=float)
    matrix_B = numpy.zeros(shape=(getOrdo.row_B, getOrdo.column_B), dtype=float)

    print(colored("Data matriks A:", 'blue'))
    print(getMatriks.Matrix_A)
    print("\n")
    print(colored("Data matriks B:", 'blue'))
    print(getMatriks.Matrix_B)
    print("\n")

    print(colored("Matriks "+ str(skalar) +" * A:", 'blue'))
    for x in range(0, len(getMatriks.Matrix_A)):
        for y in range(0, len(getMatriks.Matrix_A[0])):
            data = (skalar * getMatriks.Matrix_A[x][y])
            matrix_A[x, y] = data

    print(matrix_A)
    print("\n")

    print(colored("Matriks "+ str(skalar) +" * B:", 'blue'))
    for x in range(0, len(getMatriks.Matrix_B)):
        for y in range(0, len(getMatriks.Matrix_B[0])):
            data = (skalar * getMatriks.Matrix_B[x][y])
            matrix_B[x, y] = data


    print(matrix_B)
    print("\n")




def determinan_matriks():
    print(colored("Determinan Matriks \n", 'green', attrs=['bold']))
    getOrdo = get_ordo_Input()
    while getOrdo.row_A != getOrdo.row_B or getOrdo.column_A != getOrdo.column_B:
        print(colored('Ordo matriks A dan B tidak sama !', 'red'))
        getOrdo = get_ordo_Input()
    while getOrdo.row_A > 3 or getOrdo.row_B > 3 or getOrdo.column_A > 3 or getOrdo.column_B > 3:
        print(colored('Ordo matriks terlalu besar !', 'red'))
        print(colored('Silakan gunakan ordo 2x2 atau 3x3 !', 'red'))
        getOrdo = get_ordo_Input()
    getMatriks = get_Data_Matriks(getOrdo.row_A, getOrdo.row_B, getOrdo.column_A, getOrdo.column_B)
    print(colored("Data matriks A:", 'blue'))
    print(getMatriks.Matrix_A)
    print("\n")
    print(colored("Data matriks B:", 'blue'))
    print(getMatriks.Matrix_B)
    print("\n")
    determinan_A = numpy.linalg.det(getMatriks.Matrix_A)
    determinan_B = numpy.linalg.det(getMatriks.Matrix_B)
    print(colored("Determinan Matriks A: " + str(determinan_A)+"\n", 'blue'))
    print(colored("Determinan Matriks B: " + str(determinan_B), 'blue'))


def perkalian_antar_matriks():
    print(colored("Perkalian antar matriks \n", 'green', attrs=['bold']))
    print("pilih opsi operasi:")
    print("1. A x B")
    print("2. B x A")

    try:
        modePerkalian = int(input(colored("Opsi: ", 'yellow')))
        print("\n")
        if modePerkalian == 1:
            print(colored("Perkalian Matriks A x B \n", 'green', attrs=['bold']))
            getOrdo = get_ordo_Input()
            while getOrdo.column_A != getOrdo.row_B:
                print(colored('Perkalian tidak bisa dilakukan', 'red'))
                print(colored('Kolom matriks A harus sama dengan baris matriks B!', 'red'))
                getOrdo = get_ordo_Input()

            getMatriks = get_Data_Matriks(getOrdo.row_A, getOrdo.row_B, getOrdo.column_A, getOrdo.column_B)
            print(colored("Data matriks A:", 'blue'))
            print(getMatriks.Matrix_A)
            print("\n")
            print(colored("Data matriks B:", 'blue'))
            print(getMatriks.Matrix_B)
            print("\n")
            matrix_A = numpy.zeros(shape=(getOrdo.row_A, getOrdo.column_B), dtype=float)
            for i in range(0, getOrdo.row_A):
                for j in range(0, getOrdo.column_B):
                    for k in range(0, getOrdo.column_A):
                        matrix_A[i][j] = matrix_A[i][j] + getMatriks.Matrix_A[i][k] * getMatriks.Matrix_B[k][j]
            print(colored("Data matriks A x B:", 'blue'))
            print(matrix_A)
            print("\n")
        elif modePerkalian == 2:
            print(colored("Perkalian matriks B x A \n", 'green', attrs=['bold']))
            getOrdo = get_ordo_Input()
            while getOrdo.column_A != getOrdo.row_B:
                print(colored('Perkalian tidak bisa dilakukan', 'red'))
                print(colored('Kolom matriks A harus sama dengan baris matriks B!', 'red'))
                getOrdo = get_ordo_Input()

            getMatriks = get_Data_Matriks(getOrdo.row_A, getOrdo.row_B, getOrdo.column_A, getOrdo.column_B)
            print(colored("Data matriks A:", 'blue'))
            print(getMatriks.Matrix_A)
            print("\n")
            print(colored("Data matriks B:", 'blue'))
            print(getMatriks.Matrix_B)
            print("\n")
            matrix_B = numpy.zeros(shape=(getOrdo.row_B, getOrdo.column_A), dtype=float)
            for i in range(0, getOrdo.row_B):
                for j in range(0, getOrdo.column_A):
                    for k in range(0, getOrdo.column_B):
                        matrix_B[i][j] = matrix_B[i][j] + getMatriks.Matrix_B[i][k] * getMatriks.Matrix_A[k][j]
            print(colored("Data matriks B x A:", 'blue'))
            print(matrix_B)
            print("\n")

    except ValueError:
        print(colored('Harap hanya memasukan angka!', 'red'))






if __name__ == '__main__':
    Arr = [[]]
    Brr = [[]]



    while(True):
        print(colored("Pilih salah satu menu", 'yellow'))
        print("1. Penjumlahan matriks")
        print("2. Pengurangan matriks")
        print("3. Perkalian skalar matriks")
        print("4. Determinan matriks")
        print("5. Perkalian antar matriks")
        print("6. Keluar")
        try:
            menu = int(input(colored("Masukan jenis menu yang anda inginkan : ", 'yellow')))
            print("\n")
            if menu == 1:
                penjumlahan_matriks()
            elif menu == 2:
                pengurangan_matriks()
            elif menu == 3:
                perkalian_skalar()
            elif menu == 4:
                determinan_matriks()
            elif menu == 5:
                perkalian_antar_matriks()
            elif menu == 6:
                print("Terimakasih dan sampai jumpa :-)")
                break
        except ValueError:
            print (colored('Harap hanya memasukan angka!', 'red'))













