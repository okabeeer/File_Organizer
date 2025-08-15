import os

files=os.listdir(os.getcwd())
pcnt=1
vcnt=1
dcnt=1
mcnt=1
ocnt=1
for i in files:
    name,extension = os.path.splitext(i)
    if extension == ".jpg" or extension == ".png" or extension == ".gif":
        if os.path.exists("Images"):
            if i in os.listdir(os.path.join(os.getcwd(),"Images")):
                new_name=f"{name}_{pcnt}{extension}"
                os.rename(i,f"{name}_{pcnt}{extension}")
                os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), "Images", new_name))
                pcnt+=1
            else:
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), "Images", i))
        else:
            os.mkdir("Images")
            os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), "Images", i))
    elif extension == ".mp4" or extension == ".mkv":
        if os.path.exists("Videos"):
            if i in os.listdir(os.path.join(os.getcwd(), "Videos")):
                new_name = f"{name}_{vcnt}{extension}"
                os.rename(i, f"{name}_{pcnt}{extension}")
                os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), "Videos", new_name))
                vcnt+=1
            else:
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), "Videos", i))
        else:
            os.mkdir("Videos")
            os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), "Videos", i))
    elif extension == ".pdf" or extension== ".docx" or extension== ".txt":
        if os.path.exists("Documents"):
            if i in os.listdir(os.path.join(os.getcwd(), "Documents")):
                new_name = f"{name}_{pcnt}{extension}"
                os.rename(i, f"{name}_{dcnt}{extension}")
                os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), "Documents", new_name))
                dcnt+=1
            else:
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), "Documents", i))
        else:
            os.mkdir("Documents")
            os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), "Documents", i))
    elif extension == ".mp3" or extension== ".wav":
        if os.path.exists("Music"):
            if i in os.listdir(os.path.join(os.getcwd(), "Music")):
                new_name = f"{name}_{pcnt}{extension}"
                os.rename(i, f"{name}_{mcnt}{extension}")
                os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), "Music", new_name))
                mcnt+=1
            else:
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), "Music", i))
        else:
            os.mkdir("Music")
            os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), "Music", i))
    else:
        if os.path.exists("Others"):
            if os.path.isfile(i):
                if i in os.listdir(os.path.join(os.getcwd(), "Others")):
                    new_name = f"{name}_{ocnt}{extension}"
                    os.rename(i, f"{name}_{ocnt}{extension}")
                    os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), "Others", new_name))
                    ocnt+=1
                else:
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), "Others", i))
        else:
            os.mkdir("Others")
            os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), "Others", i))