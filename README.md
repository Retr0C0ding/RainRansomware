# RainRansomware
Hello. Were you interested in the name of the project? Do you like cryptography? Want to meet new ransomwares? I'm developing this. You already know the name, and I chose it because most of these malwares act in the machine like acid rain. I chose AES encryption with a 32-byte key. Very simple. You, if you know, can help me to increase some resources. And one more thing: the first version is being developed in Python and will be passed to the C ++ language later. I need help to compile the code in py to get an exe file. If you know how to do that, it will be very helpful. For now Rain acts like this:

- Create some python libraries (pycrypto, glob, platform, etc)
- Check if the OS of the infected machine is Linux or Windows
- Create some useful files for malware persistence and for disablement of UAC (only Windows, for the time being)
- Imports the encryption key and encrypts files with extensions determined in three main directories and which are usually used to store the most important files (Desktop, Documents and Downloads)
- Change the background image of the Desktop, changing it to the project logo
- Provides encrypting the entire partition

Do you have suggestions? Leave them there. All you can do the project will be properly grateful, since test the source code to improve the most important resources.
