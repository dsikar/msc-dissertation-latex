def build_table(network, id, skip):
    """
    Build deliverables' table latex string for MSc project
    Inputs:
        network: string, network name
        id: integer, network id
        skip: integer, number of ids to skip
    Outputs:
        None
    """
  numrows = 16
  offset = ( id - 1) * numrows + skip
  strnum = str(id)
  # strnum = '5' # network

  # HEADER

  print('% ' + network + "\r\n")

  print("\\begin{table}[]")
  print("\\begin{center}")
  print("\\begin{tabular}{|l|l|l|l|l|l|}")
  print("\\hline")
  print("\\multicolumn{6}{|c|}{Deliverables - " + network + "} \\\\ \\hline\r\n")
  print("ID & Task &  Network/Model & Data/Sim & Deliverable & Description \\\\ \\hline\\hline")

  print(str(1 + offset) + " & Train & N" + strnum + " & D1 & N" + strnum + "M1 & Model \\\\ \\hline")
  print(str(2 + offset) + " & Test & N" + strnum + "M1 & S1 & N" + strnum + "R1 & Metric \\\\ \\hline")
  print(str(3 + offset) + " & Test & N" + strnum + "M1 & S2 & N" + strnum + "R2 & Metric \\\\ \\hline")
  print(str(4 + offset) + " & Test & N" + strnum + "M1 & S3 & N" + strnum + "R3 & Metric \\\\ \\hline\\hline\r\n")

  print(str(5 + offset) + " & Train & N" + strnum + " & D2 & N" + strnum + "M2 & Model \\\\ \\hline")
  print(str(6 + offset) + " & Test & N" + strnum + "M2 & S1 & N" + strnum + "R3 & Metric \\\\ \\hline")
  print(str(7 + offset) + " & Test & N" + strnum + "M2 & S2 & N" + strnum + "R4 & Metric \\\\ \\hline")
  print(str(8 + offset) + " & Test & N" + strnum + "M2 & S3 & N" + strnum + "R5 & Metric \\\\ \\hline\\hline\r\n")

  print(str(9 + offset) + " & Train & N" + strnum + " & D3 & N" + strnum + "M3 & Model \\\\ \\hline")
  print(str(10 + offset) + " & Test & N" + strnum + "M3 & S1 & N" + strnum + "R7 & Metric \\\\ \\hline")
  print(str(11 + offset) + " & Test & N" + strnum + "M3 & S2 & N" + strnum + "R8 & Metric \\\\ \\hline")
  print(str(12 + offset) + " & Test & N" + strnum + "M3 & S3 & N" + strnum + "R9 & Metric \\\\ \\hline\\hline\r\n")

  print(str(13 + offset) + " & Train & N" + strnum + " & D4 & N" + strnum + "M4 & Model \\\\ \\hline")
  print(str(14 + offset) + " & Test & N" + strnum + "M4 & S1 & N" + strnum + "R10 & Metric \\\\ \\hline")
  print(str(15 + offset) + " & Test & N" + strnum + "M4 & S2 & N" + strnum + "R11 & Metric \\\\ \\hline")
  print(str(16 + offset) + " & Test & N" + strnum + "M4 & S3 & N" + strnum + "R12 & Metric \\\\ \\hline \r\n")

  print("\\end{tabular}")
  print("\\end{center}")
  print("\\caption{Deliverables-" + network +"}")
  print("\\label{Deliverables-" + network +"}")
  print("\\end{table}")

nets = ['NVIDIA', 'AlexNet', 'VGGNet', 'InceptionNet', 'ResNet']
for i in range(0, len(nets)):
  print('\r\n%%%%%%%%%%%%%%%%%%%%%%%%\r\n')
  build_table(nets[i], i + 1, 12)
