# forcoding-Obfuscator
This is a script utilizing an obfuscation technique inspired by [this](https://i.blackhat.com/briefings/asia/2018/asia-18-bohannon-invoke_dosfuscation_techniques_for_fin_style_dos_level_cmd_obfuscation-wp.pdf) white paper. It basically takes the command you want to run, creates a set of unique characters and stores the index of each character of the original command. Then, it recreates the command by taking each index of the original command from the set of unique characters. At the end of the loop the original command has been reconstructed and thus, is called and executed.

## Examples
The command ```ping 8.8.8.8``` is obfuscated to the following command:  

![image](https://github.com/connar/forcoding-Obfuscator/assets/87579399/ba7e9633-38cf-4def-b995-ed4e357396f3)
