Xcoord = 0
Ycoord = 70.0
Dtool = 10.0
Zcoord = 1.0
Zinc = 1.0
Zfinal = -33.0
Diameter = 62.0
ToolOffset = 0.0
ToolNumber = 11

Xtarget = Xcoord + (Diameter / 2) - (Dtool / 2) + ToolOffset
Ytarget = Ycoord + (Diameter / 2) - (Dtool / 2) + ToolOffset
filename = f"D{Diameter}.mpf"

with open(filename, "w", encoding="utf-8") as f:

    f.write("G00 G71 G40 G17\n")
    f.write("G90\n")
    f.write("G54\n")
    f.write("G00 SUPA Z0.\n")

    f.write("R1=400; PLUNGE FEED RATE\n")
    f.write("R2=600; CUTTING FEED RATE\n")
    f.write(" ;\n")
    f.write(" ;\n")
    f.write(f" ;  TOOL NO.    :T{ToolNumber}\n")
    f.write(" ;  TOOL TYPE   : ENDMILL\n")
    f.write(f" ;  TOOL ID     : Концевая {Dtool}mm\n")
    f.write(" ;  TOOL DIA    : 10.0 LENGTH 57.0\n")
    f.write(f"T{ToolNumber}\n")
    f.write("M6\n")
    f.write("S3500 M03\n")
    f.write("D1\n")
    f.write(f"G00 X{Xcoord} Y{Ycoord}\n")
    f.write("Z10.\n")
    f.write("G01 Z1.0 F=R1\n")
    f.write(f"G01 X{Xtarget}\n")

    while Zcoord > Zfinal:
        Zcoord = Zcoord - Zinc
        Zcoord = round(Zcoord, 3)

        f.write(f"G02 Z{Zcoord} I-{Xtarget} J0 F=R1\n")

        if Zcoord == Zfinal:
            break

    f.write("G00 Z50.\n")
    f.write("M09\n")
    f.write("M05\n")
    f.write("G00 SUPA Z0.\n")
    f.write("G00 SUPA Z0. Y0.\n")
    f.write("M30\n")
    f.write("%\n")