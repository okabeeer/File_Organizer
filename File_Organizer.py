import os

n = input("enter (all/Images/Videos/Music/Documents/Compressed/Programs/Others):")
n = n.lower()

files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]

im = 0
vi = 0
do = 0
mu = 0
co = 0
pro = 0
oth = 0

if n == "all":
    for i in files:
        name, extension = os.path.splitext(i)
        extension = extension.lower()

        if extension in (".jpg", ".png", ".gif", ".jfif"):
            folder = "Images"
            if os.path.exists(folder):
                if i in os.listdir(os.path.join(os.getcwd(), folder)):
                    new_name = f"{name}_1{extension}"
                    while os.path.exists(os.path.join(os.getcwd(), folder, new_name)):
                        name += "_1"
                        new_name = f"{name}{extension}"
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), new_name))
                    os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), folder, new_name))
                    im += 1
                else:
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                    im += 1
            else:
                os.mkdir(folder)
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                im += 1

        elif extension in (".mp4", ".mkv", ".avi"):
            folder = "Videos"
            if os.path.exists(folder):
                if i in os.listdir(os.path.join(os.getcwd(), folder)):
                    new_name = f"{name}_1{extension}"
                    while os.path.exists(os.path.join(os.getcwd(), folder, new_name)):
                        name += "_1"
                        new_name = f"{name}{extension}"
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), new_name))
                    os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), folder, new_name))
                    vi += 1
                else:
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                    vi += 1
            else:
                os.mkdir(folder)
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                vi += 1

        elif extension in (".pdf", ".docx", ".txt", ".ppt"):
            folder = "Documents"
            if os.path.exists(folder):
                if i in os.listdir(os.path.join(os.getcwd(), folder)):
                    new_name = f"{name}_1{extension}"
                    while os.path.exists(os.path.join(os.getcwd(), folder, new_name)):
                        name += "_1"
                        new_name = f"{name}{extension}"
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), new_name))
                    os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), folder, new_name))
                    do += 1
                else:
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                    do += 1
            else:
                os.mkdir(folder)
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                do += 1

        elif extension in (".mp3", ".wav"):
            folder = "Music"
            if os.path.exists(folder):
                if i in os.listdir(os.path.join(os.getcwd(), folder)):
                    new_name = f"{name}_1{extension}"
                    while os.path.exists(os.path.join(os.getcwd(), folder, new_name)):
                        name += "_1"
                        new_name = f"{name}{extension}"
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), new_name))
                    os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), folder, new_name))
                    mu += 1
                else:
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                    mu += 1
            else:
                os.mkdir(folder)
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                mu += 1

        elif extension in (".zip", ".rar", ".7z"):
            folder = "Compressed"
            if os.path.exists(folder):
                if i in os.listdir(os.path.join(os.getcwd(), folder)):
                    new_name = f"{name}_1{extension}"
                    while os.path.exists(os.path.join(os.getcwd(), folder, new_name)):
                        name += "_1"
                        new_name = f"{name}{extension}"
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), new_name))
                    os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), folder, new_name))
                    co += 1
                else:
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                    co += 1
            else:
                os.mkdir(folder)
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                co += 1

        elif extension in (".exe", ".msi"):
            folder = "Programs"
            if os.path.exists(folder):
                if i in os.listdir(os.path.join(os.getcwd(), folder)):
                    new_name = f"{name}_1{extension}"
                    while os.path.exists(os.path.join(os.getcwd(), folder, new_name)):
                        name += "_1"
                        new_name = f"{name}{extension}"
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), new_name))
                    os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), folder, new_name))
                    pro += 1
                else:
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                    pro += 1
            else:
                os.mkdir(folder)
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                pro += 1

        else:
            folder = "Others"
            if os.path.exists(folder):
                if os.path.isfile(os.path.join(os.getcwd(), i)):
                    if i in os.listdir(os.path.join(os.getcwd(), folder)):
                        new_name = f"{name}_1{extension}"
                        while os.path.exists(os.path.join(os.getcwd(), folder, new_name)):
                            name += "_1"
                            new_name = f"{name}{extension}"
                        os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), new_name))
                        os.rename(os.path.join(os.getcwd(), new_name), os.path.join(os.getcwd(), folder, new_name))
                        oth += 1
                    else:
                        os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                        oth += 1
            else:
                os.mkdir(folder)
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), folder, i))
                oth += 1

print(f"{im} to Images")
print(f"{vi} to Videos")
print(f"{do} to Documents")
print(f"{mu} to Music")
print(f"{co} to Compressed")
print(f"{pro} to Programs")
print(f"{oth} to Others")

input("click any button to exit")
