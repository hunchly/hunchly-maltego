# hunchly-maltego
Maltego transforms for Hunchly
**Hunchly Maltego Setup Guide**

Revision: 1.1

Date: April 19, 2021
Author: Justin Seitz

Contact: support@hunch.ly

The Hunchly Maltego transforms are local transforms. As Paterva puts it, local transforms are trickier to deploy than remote transforms and require additional setup.

There is a video detailing these steps you can view here: [https://support.hunch.ly/article/47-1-using-the-hunchly-maltego-transforms](https://support.hunch.ly/article/47-1-using-the-hunchly-maltego-transforms)

## Installing the Hunchly Transform Set

Download Python 3.8 or newer if you don't have it:

 Windows: [https://www.python.org/downloads/](https://www.python.org/downloads/)
 Mac OSX: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Linux: run this command in the terminal

`sudo apt-get install python3 python3-pip`

Download the Hunchly transforms from here and decompress the zip file:

[https://www.hunch.ly/resources/maltego-hunchly.zip](https://www.hunch.ly/resources/maltego-hunchly.zip)

In the **python** folder there is a file named **config.py.** Open this file with a text editor and change the location of the HunchlyAPI. Here are the common paths on most systems:

### Windows:

 `hunchly\_api\_path = "C:\\Program Files (x86)[\\Hunchly](//Hunchly/) 2\\Dashboard\\HunchlyAPI.exe"`

### Mac OSX:

 `hunchly\_api\_path = "/Applications/Hunchly2.app/Contents/MacOS/HunchlyAPI"`

### Linux:

 `hunchly\_api\_path = "/usr/lib/hunchly/HunchlyAPI"`

## Configuration of Maltego

Now we need to import the Hunchly Maltego configuration file. From the Maltego menu select **Import -\> Configuration**

![image](https://github.com/hunchly/hunchly-maltego/assets/102674898/5d63006d-9dec-4632-8a0f-1eb3bc6e252c)

Browse to the **hunchlyconfiguration.mtz** file that is provided in the zip file download. Follow the directions to import all Hunchly entities, transforms and the single Hunchly machine.

Now that the configuration is imported we need to configure the location for each of the Python scripts. This is a pain in the arse, but there is no other automatic way of doing it.

 Click on the **Transforms** ribbon and then click the **Transform Manager** button.

 In the new dialog type in **hunchly** to filter to only show the Hunchly transforms.

![image](https://github.com/hunchly/hunchly-maltego/assets/102674898/8d73cedc-1f33-4905-aab7-aaae9ed1dd4b)


Select the first transform in the list and then click the … button beside the **Working Directory** option. Here you need to specify the location of where the Hunchly Maltego transforms are. This is the location of the decompressed zip file you downloaded.

 ![image](https://github.com/hunchly/hunchly-maltego/assets/102674898/6fa5f063-4d36-4811-9788-a1dec5253fb0)


 Once you have put the correct path in, I suggest you copy the path to your clipboard so that you can paste it in place for each transform.

Work your way down the list of Hunchly transforms and set the path for each of them.


## Using The Hunchly Transforms

The simplest way to get started is to drag a Hunchly case entity onto your Maltego graph, and set its name to match a case name in your Hunchly database. You can then run transforms against it or run the "Hunchly Full Case Extraction" machine which will pull all of the information for a case into your graph.
