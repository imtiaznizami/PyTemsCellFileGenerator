'''
Created on May 15, 2014

@author: imtiaz.nizami
@contact: imtiazan@gmail.com
@version: 0.1
@requires: Cell database file in the required format
@requires: Neighbor file in the required format

This script takes two 'csv' files as inputs and generates a TEMS readable cell file.
The two 'csv' inputs file formats are:

1. Cell Database File format:

CELL,CI,LAT,LON,ANT_DIRECTION,ANT_BEAM_WIDTH,ARFCN,BSIC,MCC,MNC,LAC
ABC1011,12341,24.30089209,67.53721882,0,40,64,26,410,6,235
ABC1012,12342,24.30089209,67.53721882,120,40,75,65,410,6,235
ABC1013,12343,24.30089209,67.53721882,240,40,71,11,410,6,235
.
.

2. Neighbor File format:

cell,neighbor
12341,23451
12341,34562
12341,45673
.
.

'''
import sys
from PyQt4 import QtGui
from window import Ui_MainWindow

import os.path
import csv
import io

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnInputCellFile.clicked.connect(self.btnInputCellFile_Clicked)
        self.ui.btnInputNeighborFile.clicked.connect(self.btnInputNeighborFile_Clicked)
        self.ui.btnGenerateCellFile.clicked.connect(self.btnGenerateCellFile_Clicked)
        self.ui.actionCellDatabaseFileFormat.triggered.connect(self.actionCellDatabaseFileFormat_Clicked)
        self.ui.actionNeighborFileFormat.triggered.connect(self.actionNeighborFileFormat_Clicked)
        self.ui.actionAbout.triggered.connect(self.actionAbout_Clicked)
        
    def btnInputCellFile_Clicked(self):
        self.ui.txtInputCellFile.setText(QtGui.QFileDialog.getOpenFileName(filter='CSV (*.csv);;All files (*.*)'))
              
    def btnInputNeighborFile_Clicked(self):
        self.ui.txtInputNeighborFile.setText(QtGui.QFileDialog.getOpenFileName(filter='CSV (*.csv);;All files (*.*)'))
            
    def actionCellDatabaseFileFormat_Clicked(self):
        QtGui.QMessageBox.information(None, 'Cell Database file Format', "CELL,CI,LAT,LON,ANT_DIRECTION,ANT_BEAM_WIDTH,ARFCN,BSIC,MCC,MNC,LAC")
        
    def actionNeighborFileFormat_Clicked(self):
        QtGui.QMessageBox.information(None, 'Neighbor file Format', "cell,neighbor")
        
    def actionAbout_Clicked(self):
        QtGui.QMessageBox.information(None, 'About', "Source code for this software can be found at:\nhttps://github.com/imtiaznizami/PyTemsCellFileGenerator")
        
    def btnGenerateCellFile_Clicked(self):
        fn_cel = self.ui.txtInputCellFile.text()
        fn_nbr = self.ui.txtInputNeighborFile.text()
        
        # check if file / folder names are valid
        if not os.path.isfile(fn_cel):
            QtGui.QMessageBox.information(None, 'Warning', "Cell file name is invalid. Aborting execution.")
            return
            
        if not os.path.isfile(fn_nbr):
            QtGui.QMessageBox.information(None, 'Warning', "Neighbor file name is invalid. Aborting execution.")
            return

        # read neighbor file into a dictionary
        # key: cell id
        # value: list of neighbors 
        dict_nbr = {}
        
        with open(fn_nbr, 'rt') as csvfile:
            reader_nbr = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader_nbr:
                if len(row) > 1:
                    if row[0] not in dict_nbr:
                        dict_nbr[row[0]] = []
                    
                    dict_nbr[ row[0].strip() ].append( row[1].strip() )   
        
        # read cell file and write to file like string
        output = io.StringIO()
        writer = csv.writer(output, delimiter = '\t', lineterminator='\n')
        writer.writerow(["2 TEMS_-_Cell_names"])
        lst_header = []
        flag = 1
        
        with open(fn_cel, 'rt') as f:
            reader = csv.DictReader(f) # read rows into a dictionary format
            for row in reader: # read a row as {column1: value1, column2: value2,...}                
                lst = list(row.values())
                for (k,v) in row.items(): # go over each column name and value  
                    if flag:
                        lst_header.append(k)                  
                    if k == 'CI':
                        if v in dict_nbr:
                            lst = lst + dict_nbr[v][:32]
                               
                if flag:
                    for n in range(1, 33):
                        lst_header.append("CI_N_%s" % (n,))
                    writer.writerow( lst_header )
                    flag = 0
                
                writer.writerow( lst )
        
        # write output file
        fn_out = QtGui.QFileDialog.getSaveFileName(filter='CEL (*.cel);;All files (*.*)')
        if not os.path.isdir(os.path.dirname(fn_out)):
            QtGui.QMessageBox.information(None, 'Warning', "Output file directory is invalid. Aborting execution.")
            return
        
        file_out = open(fn_out, "w")
        file_out.write(output.getvalue())
        file_out.close()
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())