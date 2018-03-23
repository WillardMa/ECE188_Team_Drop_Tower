import os.path
from os import listdir

import numpy as np
from matplotlib import pyplot as plt

while True:
    #Select text file
    fileName = "";

    folder = os.path.dirname(os.path.realpath(__file__));    #default to working directory

    fileNames = listdir(folder);   #get from output folder

    print(f"Listing outputs from {folder}")
    index = 0;
    for fileName in fileNames:  #Display file selection menu
        print(f"{index}. {fileName}")
        index += 1

    choice = int(input("Select file by index (-1 for quit):"));
    print();
    if choice is -1:
        break;
    fileName = f"{folder}\{fileNames[choice]}"



    #Start reading
    FGF1encoderCount = [];  #Floor Ground to Floor 1
    F1FGencoderCount = [];  #Floor 1 to Floor Ground    FROM BELOW
    FGF2encoderCount = [];  #Floor Ground to Floor 2
    F2FGencoderCount = [];  #Floor 2 to Floor Ground
    F1F2encoderCount = [];  #Floor 1 to Floor 2         FIRST VAL IS FROM BELOW, ELSE FROM ABOVE
    F2F1encoderCount = [];  #Floor 2 to Floor 1
    

    with open(fileName, "r") as file:
        
        print(f"reading from {fileName}...")
        file.readline();        #Skip first line, its a garbage value
        line = file.readline();
        while line is not "":   #readline returns "" at EOF
            if line is not "\n":    #not reading blankline
                val = line.strip().split(" ")[-1];  #format: "Floor X to Floor Y: Val"
                
                if "Ground Floor to Floor 1" in line:   
                    FGF1encoderCount.append(abs(int(val)));
                if "Floor 1 to Ground Floor" in line:   
                    F1FGencoderCount.append(abs(int(val)));
                if "Ground Floor to Floor 2" in line:   
                    FGF2encoderCount.append(abs(int(val)));
                if "Floor 2 to Ground Floor" in line:   
                    F2FGencoderCount.append(abs(int(val)));
                if "Floor 2 to Floor 1" in line:
                    F2F1encoderCount.append(abs(int(val)));
                if "Floor 1 to Floor 2" in line:
                    F1F2encoderCount.append(abs(int(val)));

            line = file.readline()  # read next line

        print(f"Done reading from {fileName}")
        print()
        


    print(f"FGF1encoderCount:\n{FGF1encoderCount}")
    print(f"F1FGencoderCount:\n{F1FGencoderCount}")
    print(f"FGF2encoderCount:\n{FGF2encoderCount}")
    print(f"F2FGencoderCount:\n{F2FGencoderCount}")
    print(f"F1F2encoderCount:\n{F1F2encoderCount}")
    print(f"F2F1encoderCount:\n{F2F1encoderCount}")
    print()

    #DATA ANALYSIS

    ##FGF1encoderCount
    print("FGF1 Data Analysis")
    ####Mean?
    mean = np.mean(np.array(FGF1encoderCount))
    print(f"The mean is {mean}")

    ####Standard Deviation?
    std = np.std(np.array(FGF1encoderCount))
    print(f"The Std is {std}")

    ####Max time diff??
    maximum = np.amax(np.array(FGF1encoderCount))
    print(f"The max is {maximum}")

    ####Min time diff??
    minimum = np.amin(np.array(FGF1encoderCount))
    print(f"The minimum is {minimum}")

    ####Max - Min range
    interval = maximum - minimum
    print(f"The max - min is {interval}")
    print()

    ##F1FGencoderCount
    print("F1FG Data Analysis")
    ####Mean?
    mean = np.mean(np.array(F1FGencoderCount))
    print(f"The mean is {mean}")

    ####Standard Deviation?
    std = np.std(np.array(F1FGencoderCount))
    print(f"The Std is {std}")

    ####Max time diff??
    maximum = np.amax(np.array(F1FGencoderCount))
    print(f"The max is {maximum}")

    ####Min time diff??
    minimum = np.amin(np.array(F1FGencoderCount))
    print(f"The minimum is {minimum}")

    ####Max - Min range
    interval = maximum - minimum
    print(f"The max - min is {interval}")
    print()

    ##FGF2encoderCount
    print("FGF2 Data Analysis")
    ####Mean?
    mean = np.mean(np.array(FGF2encoderCount))
    print(f"The mean is {mean}")

    ####Standard Deviation?
    std = np.std(np.array(FGF2encoderCount))
    print(f"The Std is {std}")

    ####Max time diff??
    maximum = np.amax(np.array(FGF2encoderCount))
    print(f"The max is {maximum}")

    ####Min time diff??
    minimum = np.amin(np.array(FGF2encoderCount))
    print(f"The minimum is {minimum}")

    ####Max - Min range
    interval = maximum - minimum
    print(f"The max - min is {interval}")
    print()

    ##F2FGencoderCount
    print("F2FG Data Analysis")
    ####Mean?
    mean = np.mean(np.array(F2FGencoderCount))
    print(f"The mean is {mean}")

    ####Standard Deviation?
    std = np.std(np.array(F2FGencoderCount))
    print(f"The Std is {std}")

    ####Max time diff??
    maximum = np.amax(np.array(F2FGencoderCount))
    print(f"The max is {maximum}")

    ####Min time diff??
    minimum = np.amin(np.array(F2FGencoderCount))
    print(f"The minimum is {minimum}")

    ####Max - Min range
    interval = maximum - minimum
    print(f"The max - min is {interval}")
    print()

    ##F1F2encoderCount
    print("F1F2 Data Analysis")
    ####Mean?
    mean = np.mean(np.array(F1F2encoderCount))
    print(f"The mean is {mean}")

    ####Standard Deviation?
    std = np.std(np.array(F1F2encoderCount))
    print(f"The Std is {std}")

    ####Max time diff??
    maximum = np.amax(np.array(F1F2encoderCount))
    print(f"The max is {maximum}")

    ####Min time diff??
    minimum = np.amin(np.array(F1F2encoderCount))
    print(f"The minimum is {minimum}")

    ####Max - Min range
    interval = maximum - minimum
    print(f"The max - min is {interval}")
    print()

    ##F2F1encoderCount
    print("F2F1 Data Analysis")
    ####Mean?
    mean = np.mean(np.array(F2F1encoderCount))
    print(f"The mean is {mean}")

    ####Standard Deviation?
    std = np.std(np.array(F2F1encoderCount))
    print(f"The Std is {std}")

    ####Max time diff??
    maximum = np.amax(np.array(F2F1encoderCount))
    print(f"The max is {maximum}")

    ####Min time diff??
    minimum = np.amin(np.array(F2F1encoderCount))
    print(f"The minimum is {minimum}")

    ####Max - Min range
    interval = maximum - minimum
    print(f"The max - min is {interval}")
    print()

    

    #Start plotting
    plt.figure();

    #FGF2encoderCount
    print(f"Plotting {FGF2encoderCount}...")
    plt.subplot(231)
    plt.title(f"FGF2encoderCount vs iteration #")
    plt.xlabel("Iteration number")
    plt.ylabel("Encoder Value")
    plt.plot(FGF2encoderCount, "bo");
    plt.show(block=False)

    #F2FGencoderCount
    print(f"Plotting {F2FGencoderCount}...")
    plt.subplot(232)
    plt.title(f"F2FGencoderCount vs iteration #")
    plt.xlabel("Iteration number")
    plt.ylabel("Encoder Value")
    plt.plot(F2FGencoderCount, "bo");
    plt.show(block=False)

    #F1FGencoderCount
    print(f"Plotting {F1FGencoderCount}...")
    plt.subplot(233)
    plt.title(f"F1FGencoderCount vs iteration #")
    plt.xlabel("Iteration number")
    plt.ylabel("Encoder Value")
    plt.plot(F1FGencoderCount, "bo");
    plt.show(block=False)

    #FGF1encoderCount
    print(f"Plotting {FGF1encoderCount}...")
    plt.subplot(234)
    plt.title(f"FGF1encoderCount vs iteration #")
    plt.xlabel("Iteration number")
    plt.ylabel("Encoder Value")
    plt.plot(FGF1encoderCount, "bo");
    plt.show(block=False)

    #F1F2encoderCount
    print(f"Plotting {F1F2encoderCount}...")
    plt.subplot(235)
    plt.title(f"F1F2encoderCount vs iteration #")
    plt.xlabel("Iteration number")
    plt.ylabel("Encoder Value")
    plt.plot(F1F2encoderCount, "bo");
    plt.show(block=False)

    #F2F1encoderCount
    print(f"Plotting {F2F1encoderCount}...")
    plt.subplot(236)
    plt.title(f"F2F1encoderCount vs iteration #")
    plt.xlabel("Iteration number")
    plt.ylabel("Encoder Value")
    plt.plot(F2F1encoderCount, "bo");
    plt.show(block=False)
    
    print();

plt.show();