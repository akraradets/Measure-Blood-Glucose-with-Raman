import os

def limite_spectrum_range(path:str, upper_bound:float, lower_bound:float):
    new_content:list[str] = []
    with open(file=path, mode="r+") as f:
        for idx, line in enumerate(f.readlines()):
            if(line[0] == "#"): 
                new_content.append(line)
                continue
            splitted = line.rstrip().split('\t')
            spectrum = float(splitted[0])
            value = float(splitted[1])
            if spectrum > upper_bound: continue
            if spectrum < lower_bound: break
            new_content.append(line)
        f.seek(0,0)
        f.writelines(new_content)
        f.truncate()

def add_meta_to_text(path:str):
    filename:str = os.path.split(path)[1]
    filename, ext = os.path.splitext(filename)
    spiltted = filename.split("_")
    assert len(spiltted) in [11,12], f"{filename} does not have the expected format."
    # ['wrist', '600', '785 nm', '10 s', '1', '2023', '10', '30', '15', '16', '43', '01']
    target = spiltted[0]
    gating = spiltted[1]
    laser = spiltted[2]
    exposition = spiltted[3].split(' ')[0]
    accumulation = spiltted[4]
    year = spiltted[5]
    month = spiltted[6]
    day = spiltted[7]
    hour = spiltted[8]
    minute = spiltted[9]
    second = spiltted[10]
    #Acquired=30.10.2023 15:34:55
    date = f"{day}.{month}.{year} {hour}:{minute}:{second}"
    with open(path,'r+') as f:
        content = f.read()
        assert content.count('#') == 0, f"{path} already contains meta data."
        f.seek(0,0) #get to the first position
        f.write(f"#Sample={target}\n")
        f.write(f"#Laser={laser}\n")
        #Grating=600
        f.write(f"#Grating={gating}\n")
        #Exposition=10
        f.write(f"#Exposition={exposition}\n")
        #Accumulation=1
        f.write(f"#Accumulation={accumulation}\n")
        #Acquired=30.10.2023 15:32:13
        f.write(f"#Acquired={date}\n")
        f.write(content)