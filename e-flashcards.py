import sys
import fileinput
# importing csv module
import csv
import codecs 

# ==================================csv file operations


# csv file name
filename = "input.csv"
 
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with codecs.open(filename, 'r', encoding='utf-8', errors='ignore' ) as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
 
 

from csv import reader, writer 
with open('input.csv' , encoding='utf-8' , errors='ignore') as f, open('temp.dat', 'w' , encoding='utf-8' , errors='ignore') as fw: 
    writer(fw, delimiter='|').writerows(zip(*reader(f, delimiter=';')))
    
    
   
   
   
   
   
   

    
    
# creating a variable and storing the text
# that we want to search
search_text = "|"

# creating a variable and storing the text
# that we want to add
replace_text = "\",\""

# Opening our text file in read only
# mode using the open() function
with open(r'temp.dat', 'r', encoding='utf-8' , errors='ignore') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()

	# Searching and replacing the text
	# using the replace() function
	data = data.replace(search_text, replace_text)

# Opening our text file in write only
# mode to write the replaced content
with open(r'temp.dat', 'w', encoding='utf-8' , errors='ignore') as file:

	# Writing the replaced data in our
	# text file
	file.write(data)

# Printing Text replaced
print("Text replaced")








 
# reading temp file
with open('temp.dat', 'r', encoding='utf-8' , errors='ignore') as file:

     
    TargetLang = file.readline()
    TargetLang = TargetLang.replace('\n','')
    file.readline()
    Phonetics = file.readline()
    Phonetics = Phonetics.replace('\n','')
    file.readline()
    Meaning =   file.readline()
    Meaning = Meaning.replace('\n','')

print(TargetLang)
print(Phonetics)
print(Meaning)



#$=========================================
# Arduino file construction
  
# Opening a file
file1 = codecs.open('upload.ino', 'w', encoding='utf-8' , errors='ignore')
# Writing a string to file
file1.write("int NumberOfWords = "+str(csvreader.line_num)+"; \n\n" )

file1.write("#include <Arduino.h> \n#include <U8g2lib.h> \n#ifdef U8X8_HAVE_HW_SPI \n#include <SPI.h> \n#endif \n#ifdef U8X8_HAVE_HW_I2C \n#include <Wire.h> \n#endif \n\n") 
  

# Writing a string to file
file1.write("char *TargetLang[] = {\""+TargetLang+"\"};\n" )
file1.write("char *Phonetics[] = {\""+Phonetics+"\"};\n" )
file1.write("char *Meaning[] = {\""+Meaning+"\"};\n\n\n" )

file1.write("#ifdef U8X8_HAVE_HW_SPI \n#include <SPI.h> \n#endif \n#ifdef U8X8_HAVE_HW_I2C \n#include <Wire.h> \n#endif\n\n" )

file1.write("//U8G2_SSD1306_128X32_UNIVISION_1_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);   // Adafruit ESP8266/32u4/ARM Boards + FeatherWing OLED\n\n" )
file1.write("U8G2_SSD1306_128X32_UNIVISION_F_SW_I2C u8g2(U8G2_R0, /* clock=*/ 14, /* data=*/ 2, /* reset=*/ 4);   // Adafruit Feather M0 Basic Proto + FeatherWing OLED\n\n" )


file1.write("void setup(void) {\n\n\n" )
file1.write("u8g2.begin();\n" )
file1.write("u8g2.enableUTF8Print();   // enable UTF8 support for the Arduino print() function\n" )
file1.write("}\n" )

file1.write("void loop(void) {\n\n\n" )

file1.write("int counter = random(NumberOfWords);\n" )

file1.write("u8g2.setFontDirection(0);\n" )

file1.write("u8g2.firstPage();\n" )
file1.write("  do {\n" )



file1.write("    u8g2.setFont(u8g2_font_wqy16_t_gb2312); // Chinese font\n  \n" )
file1.write("    //u8g2.setFont(u8g2_font_b16_t_japanese3); // japanese3: Lerning Level 1-6 font \n" )
file1.write("    u8g2.setCursor(0, 15);\n" )

file1.write("    u8g2.print(TargetLang[counter]);   \n" )
file1.write("    //u8g2.setFont(u8g2_font_b12_b_t_japanese1); //japanese3: Lerning Level 1-6 font\n" )
file1.write("    u8g2.setFont(u8g2_font_wqy12_t_gb2312a); // Chinese font\n" )

file1.write("    u8g2.setCursor(60, 15);\n" )

file1.write("    u8g2.print(Phonetics[counter]);   // Pinyin\n" )

file1.write("    u8g2.setCursor(0, 30);\n" )

file1.write("    u8g2.print(Meaning[counter]);   // English\n" )


file1.write("  } while ( u8g2.nextPage() );\n" )


file1.write("  delay(5000); \n" )

file1.write("  ESP.deepSleep(1e6); }//esp wont wate up since D0 and RST pins are not connected,\n" )
