filename=str(input("Enter the filename : "))
type_dict={"py":"Python","txt":"Text file","doc":"Document","mp4":"Video","mp3":"Audio","png":"Image","jpeg":"image","pdf":"Portable file format"}
#more pairs of file formats can be added eg : pptx : PowerPoint Presentation , xls : Excel file , gif : Graphics interchange format, etc
filename=filename.split(".")
name=str(filename[-1])
for key,value in type_dict.items():
    if name == key :
        ext_type=value
print("The extension of the file is : ",value)
